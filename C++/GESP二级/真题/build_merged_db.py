#!/usr/bin/env python3
"""
从 scratch/GESP二级真题/ 下 10 份 PDF 提取编程题
→ 合并 JSON + 图片目录

用法: python3 build_merged_db.py
"""

import json, os, re, subprocess, shutil, sys, glob

BASE = "/run/media/fslong/media/01-Projects/mdgesp/scratch/GESP二级真题"
OUT_JSON = os.path.join(BASE, "GESP二级编程题汇总.json")
OUT_IMG = os.path.join(BASE, "GESP二级编程题汇总-图片")

PDFS = sorted([
    f for f in os.listdir(BASE)
    if f.startswith("GESP二级") and f.endswith("-真题.pdf")
], reverse=True)  # 倒序: newest first

YEAR_MON_MAP = {
    "202312": "2023年12月", "202403": "2024年3月", "202406": "2024年6月",
    "202409": "2024年9月", "202412": "2024年12月", "202503": "2025年3月",
    "202506": "2025年6月", "202509": "2025年9月", "202512": "2025年12月",
    "202603": "2026年3月",
}

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return r.returncode, r.stdout.strip(), r.stderr.strip()

def month_from(name):
    m = re.search(r'(\d{6})', name)
    return m.group(1) if m else "unknown"

def safe(text):
    """filename-safe."""
    text = re.sub(r'[^\w\s\u4e00-\u9fff]', '', text)
    text = re.sub(r'\s+', '_', text)
    if len(text) > 30:
        text = text[:30]
    return text.strip('_')

def get_total_pages(pdf_path):
    rc, out, _ = run(f"pdfinfo \"{pdf_path}\" | grep Pages")
    if rc == 0:
        m = re.search(r'Pages:\s*(\d+)', out)
        if m: return int(m.group(1))
    return 0

def extract_page_texts(pdf_path, total_pages):
    """return dict page_num→text"""
    d = {}
    for pn in range(1, total_pages + 1):
        tmp = f"/tmp/gesp2_pp{pn}.txt"
        rc, _, _ = run(f"pdftotext -layout -f {pn} -l {pn} \"{pdf_path}\" {tmp}")
        if rc == 0 and os.path.exists(tmp):
            with open(tmp) as f: d[pn] = f.read()
            os.unlink(tmp)
    return d

def find_programming_pages(page_texts, full_text):
    """
    Return (sec_page, q1_pages_list, q2_pages_list)
    Detects "三、编程题" then 1、/2、 markers (Chinese punct only)
    """
    sorted_pages = sorted(page_texts.keys())

    # Find 三、编程题 page
    sec_page = None
    for pn in sorted_pages:
        if '三、编程题' in page_texts[pn]:
            sec_page = pn
            break

    if sec_page is None:
        # fallback: try last few pages
        for pn in reversed(sorted_pages):
            if '编程题' in page_texts[pn]:
                sec_page = pn
                break

    q1_pages, q2_pages = [], []
    q1_started, q2_started = False, False

    for pn in sorted_pages:
        if sec_page and pn < sec_page:
            continue
        txt = page_texts[pn].replace('\f', ' ')

        has_q1 = bool(re.search(r'(?m)^1[、]', txt))
        has_q2 = bool(re.search(r'(?m)^2[、]', txt))

        if has_q1 and not q1_started:
            q1_started = True
        if has_q2 and q1_started and not q2_started:
            q2_started = True

        if q1_started and not q2_started:
            q1_pages.append(pn)
        elif q2_started:
            q2_pages.append(pn)

    # Fallback: everything after last q1 page = q2
    if q1_pages and not q2_pages:
        last_q1 = max(q1_pages)
        for pn in sorted_pages:
            if pn > last_q1:
                q2_pages.append(pn)

    return sec_page, q1_pages, q2_pages

def extract_images(pdf_path, month, q1_pages, q2_pages):
    """
    Extract embedded images from PDF using pdfimages.
    Returns dict: page_num → [filename1, filename2, ...]
    """
    tmpdir = f"/tmp/gesp2_extract_{month}"
    os.makedirs(tmpdir, exist_ok=True)

    rc, _, err = run(f"pdfimages -png \"{pdf_path}\" \"{tmpdir}/img\"")
    if rc != 0:
        print(f"    pdfimages error: {err}")
        # try jpg fallback
        run(f"pdfimages -j \"{pdf_path}\" \"{tmpdir}/img\"")

    # Get page-to-image mapping
    img_page_map = {}  # page → list of image indices
    rc, out, _ = run(f"pdfimages -list \"{pdf_path}\"")
    if rc == 0:
        for line in out.split('\n'):
            parts = line.split()
            if len(parts) >= 2 and parts[0].isdigit():
                page = int(parts[0])
                idx = int(parts[1])
                if page not in img_page_map:
                    img_page_map[page] = []
                img_page_map[page].append(idx)

    # Collect image files
    img_files = sorted(glob.glob(f"{tmpdir}/img-*.png") + glob.glob(f"{tmpdir}/img-*.jpg"))
    
    # Map index → filepath
    idx_to_file = {}
    for fp in img_files:
        base = os.path.basename(fp)
        m = re.search(r'img-0*(\d+)', base)
        if m:
            idx_to_file[int(m.group(1))] = fp

    result = {}  # page → [fn1, fn2, ...]
    all_q_pages = list(set(q1_pages + q2_pages))

    for page in sorted(all_q_pages):
        if page in img_page_map:
            for idx in img_page_map[page]:
                if idx in idx_to_file:
                    src = idx_to_file[idx]
                    # determine which question
                    if page in q1_pages and page not in q2_pages:
                        qn = 1
                    else:
                        qn = 2

                    ext = os.path.splitext(src)[1]
                    # use original page-based naming for now
                    fname = f"{month}-q{qn}_p{page}_img{idx}{ext}"
                    if page not in result:
                        result[page] = []
                    result[page].append((fname, src))

    return result

def parse_question(full_text, qnum, month):
    """
    Parse question from full text.
    Only searches after "三、编程题" section.
    Returns dict with title, sections, etc.
    """
    lines = full_text.split('\n')

    # Find "三、编程题" section first
    sec_start = None
    for i, line in enumerate(lines):
        if '三、编程题' in line:
            sec_start = i
            break
    if sec_start is None:
        return None

    # Now search for question title ONLY after the programming section heading
    q_start = None
    q_title = "未知题目"
    for i in range(sec_start, len(lines)):
        s = lines[i].strip()
        if qnum == 1:
            m = re.match(r'^1[、．]\s*(.+)$', s)
        else:
            m = re.match(r'^2[、．]\s*(.+)$', s)
        if m:
            q_title = m.group(1).strip()
            q_start = i
            break

    if q_start is None:
        return None

    # Find end: next question or end
    q_end = len(lines)
    for i in range(q_start + 1, len(lines)):
        s = lines[i].strip()
        if qnum == 1:
            m = re.match(r'^2[、．]', s)
        else:
            # Q2: end at EOF
            m = None
        if m:
            q_end = i
            break

    q_lines = lines[q_start:q_end]
    q_text = '\n'.join(q_lines)

    # Parse sections
    sections = {"preamble": []}
    current_key = "preamble"

    # Split by 【xxx】 markers
    pat = re.compile(r'【([^】]+)】')
    parts = pat.split(q_text)

    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        if i % 2 == 0:
            # content
            if current_key not in sections:
                sections[current_key] = []
            sections[current_key].append(part)
        else:
            current_key = part
            if current_key not in sections:
                sections[current_key] = []

    # Also look for "注意事项" or "注意：" without 【】
    # Handle "注意事项：" patterns
    for key in ["注意事项", "注意"]:
        if key not in sections:
            m = re.search(rf'{key}[：:]\s*(.*?)(?=\n\n|\Z)', q_text, re.DOTALL)
            if m:
                sections[key] = [m.group(1).strip()]

    # Build structured result
    result = {
        "title": q_title,
        "preamble": "",
        "description": "",
        "input_desc": "",
        "output_desc": "",
        "samples": [],
        "explanation": "",
        "notes": "",
        "has_reference": False,
    }

    for key, vals in sections.items():
        text = "\n".join(vals).strip()
        text = re.sub(r'[ \t]+', ' ', text)
        text = text.replace('\f', ' ')

        if key == "preamble":
            result["preamble"] = text
        elif key in ("题目描述",):
            result["description"] += text + "\n"
        elif key == "输入描述":
            result["input_desc"] = text
        elif key == "输出描述":
            result["output_desc"] = text
        elif key == "输入样例":
            # Could be multiple samples
            result["samples"].append({"input": text, "output": ""})
        elif key == "输出样例":
            if result["samples"] and not result["samples"][-1]["output"]:
                result["samples"][-1]["output"] = text
            else:
                result["samples"].append({"input": "", "output": text})
        elif key in ("样例解释", "提示"):
            result["explanation"] += text + "\n"
        elif key in ("注意事项", "注意"):
            result["notes"] = text
        elif key == "参考程序":
            result["has_reference"] = True

    return result

def build_content(qd, month, qn, page_images, q_pages):
    """
    Build markdown content for the question, with image references.
    """
    parts = []

    # Description (if preamble has content not in description)
    desc = qd.get("description", "").strip()
    preamble = qd.get("preamble", "").strip()

    # Combine preamble + description
    combined = ""
    if preamble:
        # Remove the title line "1、xxx" from preamble
        preamble_clean = re.sub(r'^\d+[、．]\s*.*?\n', '', preamble).strip()
        if preamble_clean:
            combined += preamble_clean + "\n"
    if desc:
        combined += desc

    if combined:
        parts.append(combined.strip())

    # Input description
    if qd.get("input_desc"):
        inp = qd["input_desc"]
        parts.append(f"**输入描述**\n\n{inp}")
        # Add input variable setup image if present
        imgs = _get_page_images_for_heading(page_images, q_pages, "输入")
        for fn, desc_text in imgs:
            parts.append(f"![{desc_text}]({fn})")

    # Output description
    if qd.get("output_desc"):
        outp = qd["output_desc"]
        parts.append(f"**输出描述**\n\n{outp}")
        imgs = _get_page_images_for_heading(page_images, q_pages, "输出")
        for fn, desc_text in imgs:
            parts.append(f"![{desc_text}]({fn})")

    # Samples
    for i, sm in enumerate(qd.get("samples", [])):
        if sm.get("input"):
            parts.append(f"**输入样例{i+1}**\n```\n{sm['input']}\n```")
        if sm.get("output"):
            parts.append(f"**输出样例{i+1}**\n```\n{sm['output']}\n```")

    # Explanation
    if qd.get("explanation"):
        exp = qd["explanation"].strip()
        parts.append(f"**样例解释**\n\n{exp}")

    # Notes
    if qd.get("notes"):
        notes = qd["notes"].strip()
        parts.append(f"**注意事项**\n\n{notes}")

    return "\n\n".join(parts)

def _get_page_images_for_heading(page_images, q_pages, keyword):
    """Get images from pages that match a keyword context."""
    result = []
    for pn in sorted(q_pages):
        if pn in page_images:
            for fn, src in page_images[pn]:
                desc = f"图：{keyword}相关"
                result.append((fn, desc))
    return result

def build_correct_answer(month, qn, page_images, q_pages):
    """
    Build correct_answer field with reference program images.
    """
    parts = []
    for pn in sorted(q_pages):
        if pn in page_images:
            for fn, src in page_images[pn]:
                parts.append(f"![参考程序]({fn})")
    if not parts:
        return "见参考程序"
    return "\n\n".join(parts)

def main():
    os.makedirs(OUT_IMG, exist_ok=True)

    all_questions = []
    seen_img_names = set()  # avoid dup image names

    for pdf_name in PDFS:
        month = month_from(pdf_name)
        pdf_path = os.path.join(BASE, pdf_name)

        if not os.path.exists(pdf_path):
            print(f"[SKIP] {pdf_name} not found")
            continue

        print(f"\n{'='*60}")
        print(f"[{month}] {pdf_name}")

        total = get_total_pages(pdf_path)
        print(f"  Pages: {total}")

        # Extract full text
        ft = f"/tmp/gesp2_{month}_full.txt"
        rc, _, _ = run(f"pdftotext -layout \"{pdf_path}\" {ft}")
        if rc != 0:
            print(f"  ERROR: pdftotext failed"); continue
        with open(ft) as f:
            full_text = f.read()

        # Extract page-by-page texts
        page_texts = extract_page_texts(pdf_path, total)

        # Find programming pages
        sec_page, q1_pages, q2_pages = find_programming_pages(page_texts, full_text)
        print(f"  Sec page: {sec_page}")
        print(f"  Q1 pages: {q1_pages}")
        print(f"  Q2 pages: {q2_pages}")

        # Extract images
        page_images = extract_images(pdf_path, month, q1_pages, q2_pages)
        img_count = sum(len(v) for v in page_images.values())
        print(f"  Images extracted: {img_count} (in {len(page_images)} pages)")

        # Parse Q1 and Q2
        d1 = parse_question(full_text, 1, month)
        d2 = parse_question(full_text, 2, month)

        if not d1:
            print(f"  WARNING: Q1 not found!"); continue

        print(f"  Q1: {d1['title']}")
        print(f"  Q2: {d2['title'] if d2 else 'N/A'}")

        # Process images: copy to output dir with proper names
        for qi, (qd, qpages) in enumerate([(d1, q1_pages), (d2, q2_pages)], 1):
            if not qd:
                continue

            q_images_for_content = []  # images used in content
            q_images_for_answer = []   # images used in correct_answer

            for pn in sorted(qpages):
                if pn not in page_images:
                    continue

                for idx, (orig_fname, src_path) in enumerate(page_images[pn]):
                    # Determine image role
                    # Pages with 参考程序 → answer images, else content images
                    page_txt = page_texts.get(pn, "")
                    is_ref = "参考程序" in page_txt

                    desc = safe(qd['title'])
                    ext = os.path.splitext(orig_fname)[1]

                    # Build filename: {month}-{qn}_{desc}_{purpose}.{ext}
                    purpose = "参考程序" if is_ref else "示意图"
                    new_fname = f"{month}-{qi}_{desc}_{purpose}{ext}"

                    # Handle duplicates
                    if new_fname in seen_img_names:
                        base, ext2 = os.path.splitext(new_fname)
                        new_fname = f"{base}_{idx}{ext2}"
                    seen_img_names.add(new_fname)

                    # Copy to output
                    dest = os.path.join(OUT_IMG, new_fname)
                    if not os.path.exists(dest) or os.path.getsize(src_path) != os.path.getsize(dest):
                        shutil.copy2(src_path, dest)

                    if is_ref:
                        q_images_for_answer.append(new_fname)
                    else:
                        q_images_for_content.append(new_fname)

            # Build content with proper image references
            content_parts = []

            # Title line
            content_parts.append(f"# {qd['title']}")

            # Description
            pre = qd.get("preamble", "")
            pre_clean = re.sub(r'^\d+[、．]\s*.*?\n', '', pre).strip()
            desc = qd.get("description", "").strip()
            combined_desc = ""
            if pre_clean:
                combined_desc += pre_clean + "\n"
            if desc:
                combined_desc += desc
            if combined_desc:
                content_parts.append(combined_desc.strip())

            # Input description + images
            if qd.get("input_desc"):
                inp = qd["input_desc"]
                content_parts.append(f"**输入描述**\n\n{inp}")
                # Add content images on this page
                for fn in q_images_for_content:
                    if "输入" in os.path.splitext(fn)[0] or True:
                        content_parts.append(f"![输入示意图]({fn})")

            # Output description + images
            if qd.get("output_desc"):
                outp = qd["output_desc"]
                content_parts.append(f"**输出描述**\n\n{outp}")
                for fn in q_images_for_content:
                    # Only add if not already referenced in input
                    if not any(f"({fn})" in p for p in content_parts):
                        content_parts.append(f"![输出示意图]({fn})")

            # Samples
            for i, sm in enumerate(qd.get("samples", [])):
                if sm.get("input"):
                    content_parts.append(f"**输入样例{i+1}**\n```\n{sm['input']}\n```")
                if sm.get("output"):
                    content_parts.append(f"**输出样例{i+1}**\n```\n{sm['output']}\n```")

            # Explanation
            if qd.get("explanation"):
                exp = qd["explanation"].strip()
                content_parts.append(f"**样例解释**\n\n{exp}")

            # Notes
            if qd.get("notes"):
                notes = qd["notes"].strip()
                content_parts.append(f"**注意事项**\n\n{notes}")

            content = "\n\n".join(content_parts)

            # Build correct_answer
            answer_parts = []
            if q_images_for_answer:
                for fn in q_images_for_answer:
                    answer_parts.append(f"![参考程序]({fn})")
            else:
                answer_parts.append("见参考程序")
            correct_answer = "\n\n".join(answer_parts)

            # Collect all images for this question
            all_imgs = list(set(q_images_for_content + q_images_for_answer))

            q_entry = {
                "title": qd["title"],
                "content": content,
                "question_type": "programming",
                "options": {},
                "url": "",
                "correct_answer": correct_answer,
                "score": 25,
                "explanation": "",
                "images": all_imgs,
                "exam_date": month,
            }
            all_questions.append(q_entry)
            print(f"  → Q{qi}: {qd['title']} (images: {len(all_imgs)})")

    # Sort by exam_date descending
    all_questions.sort(key=lambda q: q["exam_date"], reverse=True)

    # Build combined JSON
    ym = year_month_from_exams(all_questions)
    
    merged = {
        "title": f"图形化(Scratch)等级考试2级 历年真题",
        "description": "GESP Scratch二级 历年编程题数据库。包含10份真题卷共20道编程题。",
        "time_limit": 90,
        "pass_score": 60,
        "questions": all_questions,
    }

    with open(OUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    # Summary
    print(f"\n{'='*60}")
    print(f"[DONE] {OUT_JSON}")
    print(f"[DONE] Images in: {OUT_IMG}")
    print(f"[DONE] Total questions: {len(all_questions)}")

    # Verify
    errors = []
    if len(all_questions) != 20:
        errors.append(f"Expected 20 questions, got {len(all_questions)}")

    # Check all referenced images exist
    for q in all_questions:
        for img in q.get("images", []):
            img_path = os.path.join(OUT_IMG, img)
            if not os.path.exists(img_path):
                errors.append(f"Missing image: {img}")

    # Check JSON validity
    try:
        with open(OUT_JSON) as f:
            json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"JSON parse error: {e}")

    if errors:
        print(f"\n[ERRORS]")
        for e in errors:
            print(f"  ❌ {e}")
    else:
        print(f"\n[OK] All 20 questions, all images present, JSON valid!")

def year_month_from_exams(questions):
    """Extract year range from questions dates."""
    dates = sorted(set(q.get("exam_date", "") for q in questions), reverse=True)
    if dates:
        return f"{dates[-1][:4]}~{dates[0][:4]}"
    return ""

if __name__ == "__main__":
    main()

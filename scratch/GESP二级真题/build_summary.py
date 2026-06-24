#!/usr/bin/env python3
"""
从10份PDF提取编程题，生成汇总JSON+图片。
"""

import json
import os
import re
import subprocess
import glob

BASE_DIR = "/run/media/fslong/media/01-Projects/mdgesp/scratch/GESP二级真题"
IMG_DIR = os.path.join(BASE_DIR, "GESP二级编程题汇总-图片")
OUTPUT_JSON = os.path.join(BASE_DIR, "GESP二级编程题汇总.json")

PDF_NAMES = [
    "GESP二级202603-真题.pdf",
    "GESP二级202512-真题.pdf",
    "GESP二级202509-真题.pdf",
    "GESP二级202506-真题.pdf",
    "GESP二级202503-真题.pdf",
    "GESP二级202412-真题.pdf",
    "GESP二级202409-真题.pdf",
    "GESP二级202406-真题.pdf",
    "GESP二级202403-真题.pdf",
    "GESP二级202312-真题.pdf",
]

def month_from(pdf_name):
    m = re.search(r'(\d{6})', pdf_name)
    return m.group(1) if m else "unknown"

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr

def get_total_pages(pdf_path):
    rc, out, _ = run(f"pdfinfo \"{pdf_path}\" | grep Pages")
    if rc == 0:
        m = re.search(r'Pages:\s+(\d+)', out)
        if m:
            return int(m.group(1))
    return 0

def extract_text_per_page(pdf_path, total_pages):
    text_per_page = {}
    for pn in range(1, total_pages + 1):
        tmpfile = f"/tmp/gesp2_pp{pn}.txt"
        rc, _, _ = run(f"pdftotext -layout -f {pn} -l {pn} \"{pdf_path}\" {tmpfile}")
        if rc == 0 and os.path.exists(tmpfile):
            with open(tmpfile, 'r') as f:
                text_per_page[pn] = f.read()
            os.unlink(tmpfile)
    return text_per_page

def find_q_boundaries(full_text):
    """
    Find Q1 and Q2 within programming section.
    CRITICAL: uses Chinese comma "、" or full-width period "．" to distinguish
    from ASCII "1." used in numbered notes lists.
    Returns (q1_text, q2_text) from title line onward.
    """
    lines = full_text.split('\n')

    # Find 三、编程题
    sec = None
    for i, line in enumerate(lines):
        if '三、编程题' in line:
            sec = i
            break
    if sec is None:
        return None, None

    # Find Q1: "1、" or "1．" (Chinese punct only, NOT ASCII "1.")
    q1 = None
    for i in range(sec, len(lines)):
        line = lines[i].strip()
        if re.match(r'^1[、]', line):
            q1 = i
            break
        if re.match(r'^1[．]', line):
            q1 = i
            break

    if q1 is None:
        return None, None

    # Find Q2: "2、" or "2．" (Chinese punct only)
    q2 = None
    for i in range(q1 + 1, len(lines)):
        line = lines[i].strip()
        if re.match(r'^2[、]', line):
            q2 = i
            break
        if re.match(r'^2[．]', line):
            q2 = i
            break

    q1_text = '\n'.join(lines[q1:q2]) if q2 else '\n'.join(lines[q1:])
    q2_text = '\n'.join(lines[q2:]) if q2 else None

    return q1_text, q2_text

def parse_q(text, qnum, month):
    """Parse a single question."""
    lines = text.split('\n')

    # Extract title from first matching line (Chinese punct only)
    title = "未知题目"
    for line in lines:
        s = line.strip()
        m = re.match(r'^\d+[、．]\s*(.+?)$', s)
        if m:
            title = m.group(1).strip()
            break

    # Skip title line
    content_start = 0
    for i, line in enumerate(lines):
        s = line.strip()
        if re.match(r'^\d+[、．]', s):
            content_start = i + 1
            break

    rest = '\n'.join(lines[content_start:])

    # Parse 【xxx】 sections
    pat = re.compile(r'【([^】]+)】')
    parts = pat.split(rest)

    result = {
        "title": title,
        "content": "",
        "input_desc": "",
        "output_desc": "",
        "samples": [],
        "notes": "",
        "explanation": "",
    }

    cur = "preamble"
    secs = {cur: []}

    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        if i % 2 == 0:
            if cur and part:
                secs.setdefault(cur, []).append(part)
        else:
            cur = part
            secs.setdefault(cur, [])

    for key, vals in secs.items():
        t = "\n".join(vals).strip()
        t = re.sub(r'[ \t]+', ' ', t)
        t = t.replace('\f', ' ')

        if key in ("preamble", "题目描述"):
            result["content"] += t + "\n"
        elif key == "输入描述":
            result["input_desc"] = t
        elif key == "输出描述":
            result["output_desc"] = t
        elif key == "输入样例":
            sample_lines = [l.strip() for l in t.split('\n') if l.strip()]
            sample_text = ' | '.join(sample_lines)
            result["samples"].append({"input": sample_text, "output": ""})
        elif key == "输出样例":
            if result["samples"] and not result["samples"][-1]["output"]:
                result["samples"][-1]["output"] = t
            else:
                result["samples"].append({"input": "", "output": t})
        elif key in ("样例解释", "提示"):
            result["explanation"] += t + "\n"
        elif key in ("注意事项", "注意"):
            result["notes"] = t

    result["content"] = result["content"].strip()
    return result

def safe_fn(text):
    text = re.sub(r'[^\w\s\u4e00-\u9fff-]', '', text)
    text = text.strip()
    text = re.sub(r'\s+', '_', text)
    if len(text) > 30:
        text = text[:30]
    return text

def find_q_pages(text_per_page, month):
    """Find pages belonging to Q1 and Q2."""
    sorted_pages = sorted(text_per_page.keys())

    # Find 三、编程题 page
    sec_page = None
    for pn in sorted_pages:
        if '三、编程题' in text_per_page[pn]:
            sec_page = pn
            break

    q1p, q2p = [], []
    q1_started, q2_started = False, False

    for pn in sorted_pages:
        if sec_page and pn < sec_page:
            continue
        txt = text_per_page[pn].replace('\f', ' ')

        # Only Chinese punct for question detection
        has_q1 = bool(re.search(r'(?m)^1[、]', txt))
        has_q2 = bool(re.search(r'(?m)^2[、]', txt))

        if has_q1 and not q1_started:
            q1_started = True
        if has_q2 and q1_started and not q2_started:
            q2_started = True

        if q1_started and not q2_started:
            q1p.append(pn)
        elif q2_started:
            q2p.append(pn)

    # Fallback: if only q1 found, remaining pages = q2
    if q1p and not q2p:
        last = max(q1p)
        for pn in sorted_pages:
            if pn > last:
                q2p.append(pn)

    return q1p, q2p

def extract_imgs(pdf_path, month, q1_title, q2_title, q1p, q2p, total_pages):
    """Convert programming pages to PNG."""
    img_dir = os.path.join(BASE_DIR, f"GESP二级{month}-编程题-图片")
    os.makedirs(img_dir, exist_ok=True)

    page_imgs = {}
    pages = list(set(q1p + q2p))

    if not pages:
        pages = list(range(max(1, total_pages - 5), total_pages + 1))

    for pn in sorted(pages):
        if pn in q1p:
            label = safe_fn(q1_title); qn = 1
        elif pn in q2p:
            label = safe_fn(q2_title); qn = 2
        else:
            continue

        prefix = f"/tmp/gesp2_img_{month}_p{pn}"
        rc, _, _ = run(f"pdftoppm -png -r 200 -f {pn} -l {pn} \"{pdf_path}\" \"{prefix}\"")
        if rc == 0:
            files = sorted(glob.glob(f"/tmp/gesp2_img_{month}_p{pn}-*.png"))
            for idx, f in enumerate(files):
                fname = f"{month}-{qn}_{label}_p{pn}"
                if len(files) > 1:
                    fname += f"_{idx+1}"
                fname += ".png"
                dest = os.path.join(img_dir, fname)
                run(f"cp \"{f}\" \"{dest}\"")
                os.unlink(f)
                page_imgs.setdefault(pn, []).append(fname)
                print(f"    Image: {fname}")
    return page_imgs

def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    all_q = []

    for pdf_name in sorted(PDF_NAMES, reverse=True):
        month = month_from(pdf_name)
        pdf_path = os.path.join(BASE_DIR, pdf_name)

        if not os.path.exists(pdf_path):
            print(f"[SKIP] {pdf_name}")
            continue

        print(f"\n{'='*60}")
        print(f"[PROCESS] {pdf_name} ({month})")

        total_pages = get_total_pages(pdf_path)
        print(f"  Pages: {total_pages}")

        ft = f"/tmp/gesp2_{month}_full.txt"
        if not os.path.exists(ft):
            rc, _, _ = run(f"pdftotext -layout \"{pdf_path}\" {ft}")
            if rc != 0:
                print("  ERROR: pdftotext"); continue

        with open(ft) as f:
            full_text = f.read()

        tpp = extract_text_per_page(pdf_path, total_pages)
        q1_text, q2_text = find_q_boundaries(full_text)

        d1 = parse_q(q1_text, 1, month) if q1_text else None
        d2 = parse_q(q2_text, 2, month) if q2_text else None

        if not d1:
            print("  WARNING: Q1 not found"); continue

        print(f"  Q1: '{d1['title']}'")
        print(f"  Q2: '{d2['title'] if d2 else 'N/A'}'")

        q1p, q2p = find_q_pages(tpp, month)
        print(f"  Q1 pages: {q1p}")
        print(f"  Q2 pages: {q2p}")

        page_imgs = extract_imgs(pdf_path, month, d1['title'],
                                  d2['title'] if d2 else '',
                                  q1p, q2p, total_pages)

        for qi, (qd, qpages) in enumerate([(d1, q1p), (d2, q2p)], 1):
            if not qd:
                continue

            imgs = []
            ext_d = os.path.join(BASE_DIR, f"GESP二级{month}-编程题-图片")
            prefix = f"{month}-{qi}_"

            if os.path.exists(ext_d):
                for f in sorted(os.listdir(ext_d)):
                    if f.endswith('.png') and f.startswith(prefix):
                        src = os.path.join(ext_d, f)
                        dst = os.path.join(IMG_DIR, f)
                        if not os.path.exists(dst):
                            run(f"cp \"{src}\" \"{dst}\"")
                        imgs.append(f)

            for pn in qpages:
                if pn in page_imgs:
                    for f in page_imgs[pn]:
                        if f not in imgs:
                            imgs.append(f)

            # Build content
            parts = []
            if qd["content"]:
                parts.append(qd["content"])
            if qd["input_desc"]:
                parts.append(f"【输入描述】\n{qd['input_desc']}")
            if qd["output_desc"]:
                parts.append(f"【输出描述】\n{qd['output_desc']}")
            for si, sm in enumerate(qd["samples"]):
                if sm["input"]:
                    parts.append(f"【输入样例{si+1}】\n{sm['input']}")
                if sm["output"]:
                    parts.append(f"【输出样例{si+1}】\n{sm['output']}")
            if qd["explanation"]:
                parts.append(f"【样例解释】\n{qd['explanation']}")
            if qd["notes"]:
                parts.append(f"【注意事项】\n{qd['notes']}")

            sm_json = [{"input": s["input"], "output": s["output"]} for s in qd["samples"]]

            q = {
                "id": f"{month}-{qi}",
                "exam_date": month,
                "title": qd["title"],
                "content": "\n\n".join(parts),
                "question_type": "programming",
                "score": 25,
                "explanation": '解题思路：按照题目描述编写 Scratch 程序即可，注意变量名的拼写（包括大小写）要和题目完全一致。',
                "images": imgs,
                "answer": "见参考程序",
                "input_desc": qd["input_desc"],
                "output_desc": qd["output_desc"],
                "samples": sm_json,
                "notes": qd["notes"]
            }
            all_q.append(q)
            print(f"  -> Q{qi}: {qd['title']} (imgs={len(imgs)})")

    all_q.sort(key=lambda q: q["exam_date"], reverse=True)

    s = {
        "title": "【GESP】图形化(Scratch)等级考试2级 编程题汇总",
        "description": "GESP Scratch二级 历年编程题数据库。包含10份真题卷共20道编程题。",
        "total_questions": len(all_q),
        "questions": all_q
    }

    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(s, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"[DONE] {OUTPUT_JSON}")
    print(f"[DONE] Questions: {len(all_q)}")
    expected = 20
    if len(all_q) == expected:
        print(f"[OK] All {expected}!")
    else:
        print(f"[WARN] Got {len(all_q)}, expected {expected}")

if __name__ == "__main__":
    main()

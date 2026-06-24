#!/usr/bin/env python3
"""
批量处理 scratch/GESP二级真题/ 下 PDF，提取编程题生成 JSON/MD/图片。
"""

import json
import os
import re
import subprocess
import sys

BASE_DIR = "/run/media/fslong/media/01-Projects/mdgesp/scratch/GESP二级真题"
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

def extract_month(pdf_name):
    m = re.search(r'(\d{6})', pdf_name)
    return m.group(1) if m else "unknown"

def run(cmd):
    """Run shell command, return retcode, stdout, stderr."""
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr

def get_total_pages(pdf_path):
    """Get total pages in PDF."""
    rc, out, _ = run(f"pdfinfo \"{pdf_path}\" | grep Pages")
    if rc == 0:
        m = re.search(r'Pages:\s+(\d+)', out)
        if m:
            return int(m.group(1))
    return 0

def find_programming_pages(text_per_page):
    """
    Given dict page_num -> page_text, find pages that contain programming content.
    Returns (section_start_page, q1_pages, q2_pages) where each is list of page numbers.
    """
    section_start = None
    for pn, txt in sorted(text_per_page.items()):
        if "三、编程题" in txt:
            section_start = pn
            break
    
    if section_start is None:
        # Try alternate search
        for pn, txt in sorted(text_per_page.items()):
            if "编程题" in txt:
                section_start = pn
                break
    
    # Questions start after section header
    q1_title_found = False
    q2_title_found = False
    
    q1_pages = []
    q2_pages = []
    current_q = 0  # 0=none, 1=q1, 2=q2
    
    for pn in sorted(text_per_page.keys()):
        if pn < (section_start or 0):
            continue
        txt = text_per_page[pn]
        
        # Check for question title
        if re.search(r'(?m)^\s*1[、.．]\s*\S', txt) and not q1_title_found:
            q1_title_found = True
            current_q = 1
        
        # Check for question 2 title (on a new page or after q1 reference program)
        if current_q == 1 and re.search(r'(?m)^\s*2[、.．]\s*\S', txt):
            current_q = 2
            q2_title_found = True
        
        if current_q == 1:
            q1_pages.append(pn)
        elif current_q == 2:
            q2_pages.append(pn)
    
    # If q2 wasn't detected by title, everything after q1 ref program is q2
    if not q2_title_found and q1_pages:
        # Find where "参考程序" appears for q1 and take everything after
        last_q1_page = max(q1_pages)
        for pn in sorted(text_per_page.keys()):
            if pn > last_q1_page:
                q2_pages.append(pn)
                q2_title_found = True
    
    return section_start, q1_pages, q2_pages

def parse_question_text(full_text, question_num, month):
    """
    Parse a single question from full text.
    Returns dict with title, content, input_desc, output_desc, samples, etc.
    """
    # Find the question section
    # Look for "1、标题" or "2、标题"
    if question_num == 1:
        pattern = r'(?m)^\s*1[、.．]\s*(.+?)$'
    else:
        pattern = r'(?m)^\s*2[、.．]\s*(.+?)$'
    
    m = re.search(pattern, full_text)
    if not m:
        return None
    
    q_title = m.group(1).strip()
    q_start = m.end()
    
    # Find the end - either next question or end of text
    if question_num == 1:
        # End at question 2 or EOF
        end_m = re.search(r'(?m)^\s*2[、.．]', full_text[q_start:])
        if end_m:
            q_text = full_text[q_start:q_start + end_m.start()]
        else:
            q_text = full_text[q_start:]
    else:
        q_text = full_text[q_start:]
    
    # Parse sections
    sections = {}
    
    # Split by 【xxx】 markers
    section_pattern = re.compile(r'【([^】]+)】')
    parts = section_pattern.split(q_text)
    
    current_key = "preamble"
    sections[current_key] = []
    
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        if i % 2 == 0:
            # Content after/before a section header
            if current_key:
                sections[current_key].append(part)
        else:
            current_key = part
            if current_key not in sections:
                sections[current_key] = []
    
    # Flatten section contents
    result = {
        "title": q_title,
        "content": "",
        "input_desc": "",
        "output_desc": "",
        "samples": [],
        "notes": "",
        "explanation": "",
        "has_reference": False,
    }
    
    for key, values in sections.items():
        text = "\n".join(values).strip()
        text = re.sub(r'\s+', ' ', text)  # normalize whitespace
        text = text.replace('', ' ')  # remove form feeds
        
        if key == "preamble":
            result["content"] += text + "\n"
        elif key == "题目描述":
            result["content"] += text + "\n"
        elif key == "输入描述":
            result["input_desc"] = text
        elif key == "输出描述":
            result["output_desc"] = text
        elif key == "输入样例":
            # Extract sample input
            result["samples"].append({"input": text, "output": ""})
        elif key == "输出样例":
            if result["samples"]:
                result["samples"][-1]["output"] = text
            else:
                result["samples"].append({"input": "", "output": text})
        elif key == "样例解释":
            result["explanation"] += text + "\n"
        elif key == "注意事项" or key == "注意":
            result["notes"] = text
        elif key == "参考程序":
            result["has_reference"] = True
        elif key == "提示":
            # Some questions have "提示" sections (like 202409)
            result["explanation"] += text + "\n"
    
    # Clean up content
    result["content"] = result["content"].strip()
    if not result["notes"]:
        # Try to find notes after samples
        notes_m = re.search(r'(?:注意事项?|注意)[：:]\s*(.*?)(?=\n\n|\Z)', q_text, re.DOTALL)
        if notes_m:
            result["notes"] = notes_m.group(1).strip().replace('\n', ' ')
    
    return result

def safe_filename(text):
    """Turn Chinese text into a safe filename component."""
    # Remove special chars, keep alphanum and CJK
    text = re.sub(r'[^\w\s\u4e00-\u9fff-]', '', text)
    text = text.strip()
    text = re.sub(r'\s+', '_', text)
    # Limit length
    if len(text) > 20:
        text = text[:20]
    return text

def main():
    for pdf_name in PDF_NAMES:
        month = extract_month(pdf_name)
        pdf_path = os.path.join(BASE_DIR, pdf_name)
        
        if not os.path.exists(pdf_path):
            print(f"[SKIP] {pdf_name} not found")
            continue
        
        print(f"\n{'='*60}")
        print(f"[PROCESS] {pdf_name} (month={month})")
        
        total_pages = get_total_pages(pdf_path)
        print(f"  Total pages: {total_pages}")
        
        # Extract text per page
        text_per_page = {}
        for pn in range(1, total_pages + 1):
            tmpfile = f"/tmp/gesp_p{pn}.txt"
            rc, _, _ = run(f"pdftotext -layout -f {pn} -l {pn} \"{pdf_path}\" {tmpfile}")
            if rc == 0 and os.path.exists(tmpfile):
                with open(tmpfile, 'r') as f:
                    text_per_page[pn] = f.read()
                os.unlink(tmpfile)
        
        # Get full text
        full_text_path = f"/tmp/gesp_{month}_full.txt"
        rc, _, _ = run(f"pdftotext -layout \"{pdf_path}\" {full_text_path}")
        if rc != 0:
            print(f"  ERROR: pdftotext failed")
            continue
        
        with open(full_text_path, 'r') as f:
            full_text = f.read()
        
        # Find programming question pages
        section_start, q1_pages, q2_pages = find_programming_pages(text_per_page)
        print(f"  Section start page: {section_start}")
        print(f"  Q1 pages: {q1_pages}")
        print(f"  Q2 pages: {q2_pages}")
        
        # Parse questions
        q1 = parse_question_text(full_text, 1, month)
        q2 = parse_question_text(full_text, 2, month)
        
        if not q1 and not q2:
            print(f"  WARNING: No questions found")
            continue
        
        # Create image directory
        img_dir = os.path.join(BASE_DIR, f"GESP二级{month}-编程题-图片")
        os.makedirs(img_dir, exist_ok=True)
        
        # Convert programming pages to images
        all_question_pages = list(set(q1_pages + q2_pages))
        page_images = {}  # page_num -> list of image filenames
        
        for pn in all_question_pages:
            # Check if this page has an image (contains "如下图所示" with empty area)
            page_text = text_per_page.get(pn, "")
            has_image = "如下图所示" in page_text or "如下图所示" in page_text
            
            if not has_image:
                continue
            
            out_prefix = f"/tmp/gesp_{month}_p{pn}"
            rc, _, _ = run(f"pdftoppm -png -r 200 -f {pn} -l {pn} \"{pdf_path}\" \"{out_prefix}\"")
            if rc == 0:
                # Find generated files
                pattern = f"/tmp/gesp_{month}_p{pn}-*.png"
                import glob
                files = glob.glob(pattern)
                for f in files:
                    # Determine which question this page belongs to
                    if pn in q1_pages:
                        q_num = 1
                        q_label = safe_filename(q1["title"]) if q1 else f"q{q_num}"
                    else:
                        q_num = 2
                        q_label = safe_filename(q2["title"]) if q2 else f"q{q_num}"
                    
                    # Name: {question_num}_{descriptive_name}_p{pn}_{idx}.png
                    idx = files.index(f) + 1 if len(files) > 1 else ""
                    fname = f"{q_num}_{q_label}_p{pn}"
                    if idx:
                        fname += f"_{idx}"
                    fname += ".png"
                    
                    dest = os.path.join(img_dir, fname)
                    run(f"cp \"{f}\" \"{dest}\"")
                    os.unlink(f)
                    
                    if pn not in page_images:
                        page_images[pn] = []
                    page_images[pn].append(fname)
                    print(f"  Image: {fname}")
        
        # Build questions list for JSON
        questions = []
        
        for qi, (qp, qdata) in enumerate([(q1_pages, q1), (q2_pages, q2)], 1):
            if not qdata:
                continue
            
            # Collect images for this question
            q_images = []
            for pn in qp:
                if pn in page_images:
                    q_images.extend(page_images[pn])
            
            # Build content text
            content_parts = []
            if qdata["content"]:
                content_parts.append(qdata["content"])
            if qdata["input_desc"]:
                content_parts.append(f"【输入描述】\n{qdata['input_desc']}")
            if qdata["output_desc"]:
                content_parts.append(f"【输出描述】\n{qdata['output_desc']}")
            
            # Add samples
            for si, sample in enumerate(qdata["samples"]):
                if sample["input"]:
                    content_parts.append(f"【输入样例{si+1}】\n{sample['input']}")
                if sample["output"]:
                    content_parts.append(f"【输出样例{si+1}】\n{sample['output']}")
            
            if qdata["explanation"]:
                content_parts.append(f"【样例解释】\n{qdata['explanation']}")
            
            if qdata["notes"]:
                content_parts.append(f"【注意事项】\n{qdata['notes']}")
            
            # Build markdown-style content
            md_content = "\n\n".join(content_parts)
            
            question = {
                "title": f"第 {qi} 题",
                "content": md_content,
                "question_type": "programming",
                "correct_answer": "见参考程序",
                "score": 25,
                "explanation": '解题思路：按照题目描述编写 Scratch 程序即可。注意变量名的拼写（包括大小写）要和题目完全一致。输入变量直接赋值，无需使用"询问并等待"积木块。输出结果存放在对应变量中，无需使用"说…"积木块。',
                "images": q_images
            }
            questions.append(question)
        
        year = "20" + month[:2]
        mon = month[2:]
        title_str = f"【GESP】图形化(Scratch)等级考试2级 {year}年{mon}月 编程题"
        
        json_data = {
            "title": title_str,
            "description": "GESP Scratch二级 编程题",
            "time_limit": 40,
            "pass_score": 60,
            "questions": questions
        }
        
        # Write JSON
        json_path = os.path.join(BASE_DIR, f"GESP二级{month}-编程题.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        print(f"  JSON: {json_path}")
        
        # Write Markdown
        md_path = os.path.join(BASE_DIR, f"GESP二级{month}-编程题.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title_str}\n\n")
            
            for i, q in enumerate(questions, 1):
                f.write(f"## 第 {i} 题（{q['score']} 分）\n\n")
                f.write(f"### 题目描述\n\n{q['content']}\n\n")
                
                # Images
                if q['images']:
                    f.write("### 题目图片\n\n")
                    for img in q['images']:
                        img_rel = f"GESP二级{month}-编程题-图片/{img}"
                        desc = img.replace('.png', '').replace(f'{i}_', '')
                        f.write(f"![{desc}]({img_rel})\n\n")
                
                f.write(f"### 注意事项\n\n1. 变量名的拼写（包括大小写）要和题目完全一致。\n")
                f.write('2. 输入变量直接赋值即可，无需使用"询问并等待"积木块。\n')
                f.write('3. 输出结果存放在对应变量中即可，无需使用"说…"或"说…，2 秒"积木块。\n\n')
                
                f.write(f"### 参考程序\n\n见参考程序\n\n")
            
            # Score table
            total = sum(q['score'] for q in questions)
            f.write(f"---\n")
            f.write(f"**评分标准**：共 {len(questions)} 题，每题 {questions[0]['score'] if questions else 25} 分，满分 {total} 分。\n")
        
        print(f"  MD: {md_path}")
        
        # Clean up
        os.unlink(full_text_path)
        print(f"  [DONE] {pdf_name}")

if __name__ == "__main__":
    main()

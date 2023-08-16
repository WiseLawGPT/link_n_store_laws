import re
import json
from docx import Document
import os

def convert_word_to_json(file_path):
    document = Document(file_path)
    laws = {"chapters": []}
    current_chapter = None
    current_section = None

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        # 检查是否是章标题
        if re.match(r'^第[零一二三四五六七八九十百]+章', text):
            if current_chapter is not None:
                if current_section is not None:
                    current_chapter["sections"].append(current_section)
                laws["chapters"].append(current_chapter)
            current_chapter = {"chapter": text, "sections": []}
            current_section = None

        # 检查是否是节标题
        elif re.match(r'^第[零一二三四五六七八九十百]+节', text):
            if current_section is not None:
                current_chapter["sections"].append(current_section)
            current_section = {"section": text, "laws": []}

        # 检查是否是法条
        elif re.match(r'^第[零一二三四五六七八九十百]+条', text):
            if current_section is None:
                if "sections" in current_chapter:
                    current_chapter["laws"] = current_chapter.pop("sections")
                current_chapter["laws"].append(text)
            else:
                current_section["laws"].append(text)
                

    if current_section is not None:
        current_chapter["sections"].append(current_section)
    if current_chapter is not None:
        laws["chapters"].append(current_chapter)

    # Save laws to json
    title = os.path.splitext(os.path.basename(file_path))[0]
    json_path = title + ".json"
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(laws, json_file, ensure_ascii=False, indent=4)

file_names = ["中华人民共和国预防未成年人犯罪法.docx",
              "中华人民共和国义务教育法.docx",
              "中华人民共和国治安管理处罚法.docx",
              "中华人民共和国未成年人保护法.docx"
              "中华人民共和国刑法.docx"]

for file_name in file_names:
        convert_word_to_json(file_name)
        print(f"Converted {file_name} to JSON.")


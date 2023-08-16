import re
import json
from docx import Document
import os

def convert_word_to_json(file_path):
    document = Document(file_path)
    title = os.path.splitext(os.path.basename(file_path))[0]
    laws = {"collections": []}
    current_collection = {"collection": title, "laws": []}
    laws["collections"].append(current_collection)

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()

        # 检查是否是法条
        if re.match(r'^第[零一二三四五六七八九十百]+条', text):
                current_collection["laws"].append(text)

    # 定义JSON文件的名字
    json_file_name = title + '.json'

    # 保存为JSON文件
    with open(json_file_name, 'w', encoding='utf-8') as file:
        json.dump(laws, file, ensure_ascii=False, indent=4)

# 定义包含所有Word文档的目录
documents_directory = ''

# 遍历目录中的所有Word文档
for file_name in os.listdir(documents_directory):
    if file_name.endswith('.docx'):
        file_path = os.path.join(documents_directory, file_name)
        convert_word_to_json(file_path)
        print(f"Converted {file_name} to JSON.")


import json
import os

def merge_json_files(directory):
    all_laws = {"collections": []}

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                laws = json.load(file)
                all_laws["collections"].extend(laws["collections"])

    return all_laws

def save_merged_json(laws, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(laws, file, ensure_ascii=False, indent=4)

# 修改为您的JSON文件夹路径
directory = ''  
output_file = 'merged_laws.json' 

merged_laws = merge_json_files(directory)
save_merged_json(merged_laws, output_file)

print(f"All laws have been merged into {output_file}")

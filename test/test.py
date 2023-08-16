import json

# 读取法条JSON文件
with open('merged_laws.json', 'r', encoding='utf-8') as file:
    laws_data = json.load(file)

# 读取法条引用关系JSON文件
with open('law_references.json', 'r', encoding='utf-8') as file:
    law_references = json.load(file)

# 要查找的目标集合和法条编号
target_collection = "中华人民共和国未成年人保护法"
target_law_number = "第一百一十九条"

# 查找目标法条，并打印
for collection in laws_data['collections']:
    if collection['collection'] == target_collection:
        for law in collection['laws']:
            if law.startswith(target_law_number):
                print(f"{target_collection}\t{law}")

                # 查找关联法条的键
                ref_key = str((target_collection, target_law_number.strip('第条')))

                # 从law_references获取关联法条
                references = law_references.get(ref_key, [])

                if references:
                    print(f"\n关联法条：")

                # 打印关联法条
                for ref in references:
                    ref_collection = ref['collection']
                    ref_law_number = f"第{ref['law']}条"

                    # 从laws_data中获取关联法条的完整内容
                    for coll in laws_data['collections']:
                        if coll['collection'] == ref_collection:
                            for ref_law in coll['laws']:
                                if ref_law.startswith(ref_law_number):
                                    print(f"{ref_collection}\t{ref_law}")

                break



import re
import json

file_path = 'merged_laws.json'

# 从文件读取JSON数据
with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# 创建字典来存储法条的关联
law_references = {}

# 遍历每个集合和法条
for collection in json_data['collections']:
    collection_name = collection['collection']
    for law in collection['laws']:
        # 使用正则表达式找到文本中提到的其他法条
        references = re.findall(r'第(\d+|\w+)条', law)
        law_number = re.search(r'^第(\d+|\w+)条', law).group(1)

        # 移除第一个引用
        if references:
            references.pop(0)

        # 如果引用列表不为空，则将主法条和关联法条存储在字典中
        if references:
            law_references[(collection_name, law_number)] = [{'collection': collection_name, 'law': ref} for ref in references]

# 打印字典，显示每个法条及其关联的法条
for (collection_name, law_number), references in law_references.items():
    print(f'{collection_name} 第{law_number}条引用了:')
    for ref in references:
        print(f"   {ref['collection']} 第{ref['law']}条")

# 转换键为字符串
string_keys_law_references = {str(key): value for key, value in law_references.items()}

# 指定输出文件的路径
output_file_path = 'law_references.json'

# 打开文件以写入
with open(output_file_path, 'w', encoding='utf-8') as file:
    # 将法条的关联字典转换为JSON并保存到文件
    json.dump(string_keys_law_references, file, ensure_ascii=False, indent=4)

print(f'法条的关联已保存到 {output_file_path}')




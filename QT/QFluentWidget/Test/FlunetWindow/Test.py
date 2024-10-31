import json

with open('data/json/filePath.json', 'r', encoding='utf-8') as f:
    print(json.load(f)['path'])
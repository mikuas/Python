# from mutagen.flac import FLAC
# from mutagen.oggvorbis import OggVorbis
# import shutil
#
# from PyMyMethod.Method import FileControl
#
# from QT.QFluentWidget.Test.FlunetWindow.fileControl import File
#
#
# def getMusicNameForFlac(filePath):
#     audio = FLAC(filePath)
#     return audio.tags.get('title', [None])[0]
#
# def getMusicNameForOgg(filePath):
#     audio = OggVorbis(filePath)
#     return audio.tags.get('title', [None])[0]
#
# def reNameMusic(dirPath):
#     title = []
#     for path in FileControl().getDirFiles(dirPath):
#         path = f'./data/musics/{path}'
#         if FileControl().getSuffixName(path) == "flac":
#             result = getMusicNameForFlac(path)
#             print("RESULT" + result)
#             title.append(f'{result}.flac')
#             shutil.move(path, f'./data/musics/{result}.flac')
#             print(f"FLAC: {result}")
#         elif FileControl().getSuffixName(path) == "ogg":
#             result = getMusicNameForOgg(path)
#             print("RESULT" + result)
#             title.append(f'{result}.ogg')
#             shutil.move(path, f'./data/musics/{result}.ogg')
#             print(f"OGG: {result}")
#         else:
#             continue
#     return title
#
# # print(reNameMusic(r'C:\Users\Administrator\Music'))
# File().getImgByMusic('./data/musics', './data/musicImg')
import json

# 假设 new_data 是你要添加的字典数据
new_data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}

# 假设 current_data 是一个字典
current_data = {
    "user1": {"name": "John", "age": 30, "city": "New York"}
}

# 使用 update() 方法将 new_data 合并到 current_data 中
current_data.update({"user2": new_data})
# 打印更新后的字典
print(current_data)

# 如果要写回文件
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(current_data, json_file, indent=4, ensure_ascii=False)


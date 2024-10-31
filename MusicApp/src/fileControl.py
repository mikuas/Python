import json

from PyMyMethod.Method import FileControl

class File:
    @staticmethod
    def readFile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def readJsonFile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def saveJsonFile(key, value, path):
        data = {
            key: value
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def getImagePath(path):
        def sort(fileName):
            return int(fileName.split('.')[0])
        return [fr'../../data/images/musicPictures/{fp}' for fp in sorted(FileControl().getDirFiles(path), key=sort)]
import json


class JsonUtils:
    @staticmethod
    def readJsonFile(path: str) -> dict:
        """ read json file """
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def readJsonFiles(path: list[str]):
        """ read json files"""
        result = []
        for path in path:
            with open(path, 'r', encoding='utf-8') as f:
                result.append(json.load(f))
        return result

    def writeJsonFile(self, path: str, data: dict, indent=4):
        """ write json file """
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)
        return self

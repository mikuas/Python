import json
import os
import shutil
import sys

from PySide6.QtWidgets import QFileDialog, QMessageBox
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis

from ..doc import FileControl


class FileControl(FileControl):

    def getDirFiles(self, path, **kwargs):
        return os.listdir(path)

    def getFilePackagePath(self, fileName, **kwargs):
        print(f"Requested file: {fileName}")
        basePath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basePath, fileName)

    def getFileAbsolutePath(self, fileName, **kwargs):
        return os.path.abspath(fileName)

    def isDir(self, fileName, **kwargs):
        return os.path.isdir(fileName)

    def getSuffixName(self, fileName, **kwargs):
        return fileName.split('.')[-1]

    def getDirPathQT(self, parent=None, message=False, **kwargs):
        path = QFileDialog.getExistingDirectory(parent, "选择目录")
        if message:
            if path:
                QMessageBox.information(parent, '提示', f'选择的目录是:{path}')
            else:
                QMessageBox.warning(parent, '警告', '未选择目录')
        return path

    def getFilePathQT(self, parent=None, message=False, **kwargs):
        path = QFileDialog.getOpenFileName()[0]
        if message:
            if path:
                QMessageBox.information(parent, '提示', f'选择的文件是:{path}')
            else:
                QMessageBox.warning(parent, '警告', '未选择文件')
        return path

    def getSavePathQT(self, parent=None, defaultSaveName='result.txt', fileType="所有文件(*);;文本文件(*.txt)", **kwargs):
        return QFileDialog.getSaveFileName(parent, "保存文件", defaultSaveName, fileType)

    def readFiles(self, path: str | list[str], **kwargs):
        if type(path) is list:
            result = []
            for i in range(len(path)):
                with open(path[i], 'r', encoding='utf-8') as f:
                    result.append(f.read())
            return result
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def readJsonFiles(self, path: str | list[str], **kwargs):
        if type(path) is list:
            result = []
            for i in range(len(path)):
                with open(path[i], 'r', encoding='utf-8') as f:
                    result.append(json.load(f))
            return result
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def saveJsonFile(self, path, data, mode='w', indent=4):
        with open(path, mode, encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)
        return self

    def getMusicNameByFlac(self, path, **kwargs):
        return FLAC(path).tags.get('title', [None])[0]

    def getMusicNameByOgg(self, path, **kwargs):
        return OggVorbis(path).tags.get('title', [None])[0]

    def delFileElement(self, path, element):
        files = FileControl().getDirFiles(path)
        for file in files:
            newFile = file.split('.')[0]
            suffix = FileControl().getSuffixName(file)
            shutil.move(f'{path}/{file}', f'{path}/{newFile.split(element)[0]}.{suffix}')
        return self

    def getImgByMusic(self, path, savePath):
        data = [f"{path}/{imgData}" for imgData in self.getDirFiles(path)]
        for i in data:
            try:
                suffix = self.getSuffixName(i)
                audio = FLAC(i) if suffix == 'flac' else OggVorbis(i)
                os.makedirs(savePath, exist_ok=True)
                if audio.pictures:
                    for picture in audio.pictures:
                        # 使用音乐文件名作为图片名称
                        sFileName = f"{savePath}/{os.path.splitext(os.path.basename(i))[0]}.png"
                        with open(sFileName, 'wb') as f:
                            f.write(picture.data)
                        print(f"封面图片已保存为 {sFileName}")
                else:
                    print("该文件没有封面图片")
            except Exception as e:
                print(e)
        return self

    def fileReName(self, path, fileSuffix, nameFormat=True):
        import string
        import random
        a_Z = string.ascii_lowercase + string.ascii_uppercase
        length = len(a_Z) - 1
        i = 0
        print(self.getDirFiles(path))
        result = []
        az = ''
        for name in self.getDirFiles(path):
            for j in range(5):
                az += a_Z[random.randint(0, length)]
            suffix = self.getSuffixName(name)
            if suffix in fileSuffix:
                result.append(name)
                # 移动并重命名文件
                if nameFormat:
                    if os.path.exists(os.path.join(path, f"{str(i)}.{suffix}")):
                        i += 1
                        continue
                    shutil.move(os.path.join(path, name), os.path.join(path, f"{str(i)}.{suffix}"))
                else:
                    if os.path.exists(os.path.join(path, f"{az}.{suffix}")):
                        continue
                    shutil.move(os.path.join(path, name), os.path.join(path, f"{az}.{suffix}"))
                i += 1
                az = ''
        return [result, i]
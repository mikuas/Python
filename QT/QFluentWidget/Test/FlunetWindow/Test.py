from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
import shutil

from PyMyMethod.Method import FileControl

from QT.QFluentWidget.Test.FlunetWindow.fileControl import File


def getMusicNameForFlac(filePath):
    audio = FLAC(filePath)
    return audio.tags.get('title', [None])[0]

def getMusicNameForOgg(filePath):
    audio = OggVorbis(filePath)
    return audio.tags.get('title', [None])[0]

def reNameMusic(dirPath):
    title = []
    for path in FileControl().getDirFiles(dirPath):
        path = f'./data/musics/{path}'
        if FileControl().getSuffixName(path) == "flac":
            result = getMusicNameForFlac(path)
            print("RESULT" + result)
            title.append(f'{result}.flac')
            shutil.move(path, f'./data/musics/{result}.flac')
            print(f"FLAC: {result}")
        elif FileControl().getSuffixName(path) == "ogg":
            result = getMusicNameForOgg(path)
            print("RESULT" + result)
            title.append(f'{result}.ogg')
            shutil.move(path, f'./data/musics/{result}.ogg')
            print(f"OGG: {result}")
        else:
            continue
    return title

# print(reNameMusic(r'C:\Users\Administrator\Music'))
File().getImgByMusic('./data/musics', './data/musicImg')
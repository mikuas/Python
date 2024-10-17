from setuptools import setup, find_packages

# 运行installMode安装依赖库
setup(
    name='PyMyMethod',
    version='1.0.1',
    author='Mikuas',
    packages=find_packages(),
    install_requires=[
        'PySide6',
        'pyautogui',
        'easyocr',
        'comtypes',
        'pycaw'
    ]
)

from setuptools import setup, find_packages

setup(
    name='PyMyMethod',
    version='1.0.2',
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

from setuptools import setup, find_packages

setup(
    name='FluentWidgets',
    version='1.1.2',
    author='Mikuas',
    packages=find_packages(),
    install_requires=[
        "PySide6",
        "PySide6-Fluent-Widgets[full]"
    ]
)

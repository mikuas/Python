import os
import xml.etree.ElementTree as ET

def create_qrc(directory, qrc_filename):
    # 创建QRC文件的根元素
    rcc = ET.Element('RCC')
    qresource = ET.SubElement(rcc, 'qresource', prefix="/images/icons")

    # 遍历目录下的所有文件
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # 只添加文件，不添加目录
            file_path = os.path.join(dirpath, filename)
            # 构造文件相对路径
            relative_path = os.path.relpath(file_path, directory)
            # 添加文件元素到qresource
            file_element = ET.SubElement(qresource, 'file')
            file_element.text = relative_path.replace("\\", "/")  # 替换反斜杠为正斜杠，适配跨平台

    # 手动创建并写入文件
    with open(qrc_filename, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write('<RCC>\n')
        f.write('  <qresource prefix="/images/icons">\n')

        # 逐个写入<file>标签并换行
        for file_element in qresource:
            f.write(f'    <file>{file_element.text}</file>\n')

        f.write('  </qresource>\n')
        f.write('</RCC>\n')

if __name__ == "__main__":
    # 设置要扫描的目录和目标QRC文件名
    directory_to_scan = "./"  # 你可以更改为任何目录
    qrc_file = "resources.qrc"  # 生成的QRC文件名

    # 创建QRC文件
    create_qrc(directory_to_scan, qrc_file)
    print(f"QRC文件 '{qrc_file}' 已生成.")

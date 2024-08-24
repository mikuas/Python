import argparse
import pyautogui

if __name__ == "__main__":
    # 创建解析器对象
    parser = argparse.ArgumentParser(description="演示如何通过终端传参")
    parser.Enter = None

    # 添加参数
    parser.add_argument('-e', '--element', type=str, help='Content', required=True)
    parser.add_argument('-n', '--fileName__Path', type=str, help='Name and Path', required=True)
    parser.add_argument('-m', '--writeMode', type=str, help='codeMode', required=False)
    parser.add_argument('-E', '--Enter', type=str, help='Enter', required=False)

    # 解析参数
    args = parser.parse_args()

    # utf8_writer.py
    with open(args.fileName__Path, args.writeMode or 'w', encoding='utf-8') as file:
        if args.Enter:
            file.write('\n' + args.element)
        else:
            file.write(args.element)
    print(True)




import argparse

if __name__ == "__main__":
    # 创建解析器对象
    parser = argparse.ArgumentParser(description="Write")

    # 添加参数 空格换行
    parser.add_argument('-c', '--contentList', type=str, nargs='+', help='Content', required=True)
    parser.add_argument('-p', '--fileName__Path', type=str, help='Save Path', required=True)
    parser.add_argument('-m', '--writeMode', type=str, help='Write Mode', required=False)

    # 解析参数
    args = parser.parse_args()

    # utf8_writer.py
    with open(args.fileName__Path, args.writeMode or 'w', encoding='utf-8') as file:
        for line in args.contentList:
            file.writelines(line + '\n')
    print(True)




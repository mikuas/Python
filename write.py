from pmutils import TerminalUtils


result = TerminalUtils.createTerminalArgs(
    ['content', 'path', 'mode'],
    [list, str, str],
    isRequired=[True, True, False],
    defaultValue=[None, None, 'w'],
    description="Use Python Write To UTF-8 Encoding Files"
)

with open(result.path, result.mode, encoding='utf-8') as file:
    for line in result.content:
        file.writelines(line + '\n')
print(True)
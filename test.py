from method import TerminalControl
#
# args = TerminalControl.createTerminalArgs(
#     ['c','n','s'],
#     ['int','int','int'],
#     ['content','name','size'],
#     [True,True,False]
# )
#
# print(args.c, args.n, args.s)

(
 TerminalControl()
 .runTerminalArgs(['python', 'C:\\write.py', '-c', 'Hello World', 'Hello Python', '-p', 'C:\\test.txt', '-E', 'True'])
 .runTerminalArgs(['cmd', '/c' 'C:\\Users\\scripts\\Timingtask.exe'])
)


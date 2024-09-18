from method import TerminalControl

args = TerminalControl.createTerminalArgs(
    ['c','n','s'],
    ['int','int','int'],
    ['content','name','size'],
    [True,True,False]
)

print(args.c, args.n, args.s)


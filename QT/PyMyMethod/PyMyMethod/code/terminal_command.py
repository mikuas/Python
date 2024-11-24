import argparse

from ..doc import TerminalControl

class TerminalControl(TerminalControl):

    def createTerminalArgs(
            self,
            args: str,
            helpInfos: str | list,
            requireds: list[bool] = None,
            types: list = None,
            isList: list[bool] = None,
            default: list = None,
            defaultValue: list = None,
    ):
        parser = argparse.ArgumentParser(description='getArgs')
        i = 0
        helpInfos = helpInfos.split(' ') if type(helpInfos) is str else helpInfos
        for arg in args.split(' '):
            if isList and isList[i]:
                parser.add_argument(f'-{arg}', type=str if types is None else types[i], nargs="+", help=helpInfos[i], required=False if requireds is None else requireds[i])
            else:
                if default is not None and arg in default:
                    parser.add_argument(f'-{arg}', nargs='?' if types is None else types[i], const=defaultValue[default.index(arg)], help=helpInfos[i], required=False if requireds is None else requireds[i])
                else:
                    parser.add_argument(f'-{arg}', type=str if types is None else types[i], help=helpInfos[i], required=False if requireds is None else requireds[i])
            i += 1
        return parser.parse_args()

    def runTerminalArgs(self, element, asynchronous=False):
        import subprocess
        if asynchronous:
            processes = []
            proc = subprocess.Popen(element)
            processes.append(proc)

            for proc in processes:
                proc.wait()
        else:
            subprocess.run(element)
        return self

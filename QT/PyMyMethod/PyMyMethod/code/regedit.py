import os

from ..doc import Regedit


class Regedit(Regedit):

    def queryRegeditContent(self, path, Boot=False):
        if Boot:
            os.system(fr'reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" > result')
        else:
            os.system(fr'reg query {path} > result')
        with open('result', 'r') as f:
            result = f.read()
        os.remove('result')
        return result

    def addLeftKeyClick(self, name, path, iconPath=None):
        if iconPath:
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}" /v Icon /t REG_SZ /d "{iconPath}" /f')
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}\command" /ve /d "{path}" /f')
        else:
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}\command" /ve /d "{path}" /f')
        return self

    def addFileLeftKeyClick(self, name, path, iconPath=None, args=False):
        if iconPath:
            os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}" /v Icon /t REG_SZ /d "{iconPath}" /f')
            if args:
                os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}\command" /ve /d "{path + " %1"}" /f')
            else:
                os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}\command" /ve /d "{path}" /f')
        else:
            if args:
                os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}\command" /ve /d "{path + " %1"}" /f')
            else:
                os.system(fr'reg add "HKEY_CLASSES_ROOT\*\shell\{name}\command" /ve /d "{path}" /f')
        return self

    def addAutoBoot(self, name, startPath, addToCurrentUser=False):
        if addToCurrentUser:
            os.system(fr'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /t REG_SZ /d "{startPath}" /f')
        else:
            os.system(fr'reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /t REG_SZ /d  "{startPath}" /f')
        return self

    def delAutoBoot(self, name, delToCurrentUser=False):
        if delToCurrentUser:
            os.system(fr'reg delete "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /f')
        else:
            os.system(fr'reg delete "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /f')
        return self

    def delLeftKeyClick(self, name):
        os.system(fr'reg delete "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}" /f')
        return self

    def delFileLeftKeyClick(self, name):
        os.system(fr'reg delete "HKEY_CLASSES_ROOT\*\shell\{name}" /f')
        return self

    def setWindowsUpdateDays(self, days):
        os.system(fr'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings" /v "FlightSettingsMaxPauseDays" /t REG_DWORD /d {days} /f')
        return self

    def hideLoginUser(self, userName):
        os.system(fr'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /v {userName} /t REG_DWORD /d 0 /f')
        return self

    def showLoginUser(self, userName):
        os.system(fr'reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Win-logon\SpecialAccounts\UserList" /v {userName} /f')
        return self
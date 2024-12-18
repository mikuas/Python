import os


class RegeditUtils:
    @staticmethod
    def queryRegeditContent(path: str = None):
        """ query regedit content, path is none, query boot item content """
        if path is None:
            os.system(fr'reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" > result')
        else:
            os.system(fr'reg query {path} > result')
        with open('result', 'r') as f:
            result = f.read()
        os.remove('result')
        return result

    def addLeftKeyClickItem(self, name: str, path: str, iconPath: str = None):
        """ add leftKey click itme """
        if iconPath:
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}" /v Icon /t REG_SZ /d "{iconPath}" /f')
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}\command" /ve /d "{path}" /f')
        else:
            os.system(fr'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}\command" /ve /d "{path}" /f')
        return self

    def addFileLeftKeyClickItem(self, name: str, path: str, iconPath: str = None, args=False):
        """ add leftKey click file item """
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

    def addAutoBootItem(self, name: str, startPath: str, addToCurrentUser=False):
        """ add boot autoboot item"""
        if addToCurrentUser:
            os.system(fr'reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /t REG_SZ /d "{startPath}" /f')
        else:
            os.system(fr'reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /t REG_SZ /d  "{startPath}" /f')
        return self

    def removeAutoBootItem(self, name: str, delToCurrentUser=False):
        """ remove boot autoboot item """
        if delToCurrentUser:
            os.system(fr'reg delete "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /f')
        else:
            os.system(fr'reg delete "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v "{name}" /f')
        return self

    def removeLeftKeyClickItem(self, name: str):
        """ remove leftKey click item """
        os.system(fr'reg delete "HKEY_CLASSES_ROOT\Directory\Background\shell\{name}" /f')
        return self

    def removeFileLeftKeyClickItem(self, name: str):
        """ remove leftKey click file item """
        os.system(fr'reg delete "HKEY_CLASSES_ROOT\*\shell\{name}" /f')
        return self

    def setWindowsMaxUpdateDays(self, days: str):
        """ set windows max update days """
        os.system(fr'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings" /v "FlightSettingsMaxPauseDays" /t REG_DWORD /d {days} /f')
        return self

    def hideLoginUser(self, userName: str):
        """ hide system login display user """
        os.system(fr'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /v {userName} /t REG_DWORD /d 0 /f')
        return self

    def showLoginUser(self, userName: str):
        """ show system login display user """
        os.system(fr'reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Win-logon\SpecialAccounts\UserList" /v {userName} /f')
        return self
class MouseControl:

    def getMousePosition(self) -> list:
        """
        获取当前鼠标位置
        :return: 鼠标位置
        """
        pass

    def moveMouse(self, x: int, y: int, time: int | float = 0.1) -> 'MouseControl':
        """
        移动鼠标到指定位置
        :param x: 距离屏幕左边的位置
        :param y: 距离屏幕上面的像素
        :param time: 时间
        :return: MouseControl
        """
        pass

    def moveMouseRelative(self, x: int, y: int, time: int | float = 0.1) -> 'MouseControl':
        """
        相对移动鼠标
        :param x: 距离当前鼠标左边的像素
        :param y: 距离当前鼠标上面的像素
        :param time: 时间
        :return: MouseControl
        """
        pass

    def clickMouse(self, position: str = 'left') -> 'MouseControl':
        """
        点击鼠标
        :param position: 左键,右键
        :return: MouseControl
        """
        pass

    def twoClickMouse(self, position: str = 'left') -> 'MouseControl':
        """
        双击鼠标
        :param position: 左键,右键
        :return: MouseControl
        """
        pass

class KeyboardControl:

    def inputText(self, text: str, interval: float = 0.1) -> 'KeyboardControl':
        """
        键盘输入文本
        :param interval: 间隔
        :param text: 需要输入的文本
        :return: KeyboardControl
        """
        pass

    def keyUp(self, key: str) -> 'KeyboardControl':
        """
        释放指定按键
        :param key: 需要释放的按键
        :return: KeyboardControl
        """
        pass

    def keyDown(self, key: str) -> 'KeyboardControl':
        """
        按住指定按键
        :param key:需要按住的按键
        :return: KeyboardControl
        """
        pass

    def keyClick(self, keys: str, interval: float = 0.1) -> 'KeyboardControl':
        """
        按传入的按键,多个按键用空格隔开
        :param interval: 间隔
        :param keys: 按键
        :return:  KeyboardControl
        """
        pass

    def Hotkey(self, keys: str) -> 'KeyboardControl':
        """
        传入组合键
        :param keys: 组合键
        :return: KeyboardControl
        """
        pass


class SystemCtl:

    def getStrToPaste(self, string: str) -> 'SystemCtl':
        """
        把字符串复制到粘贴板
        :param string: 要复制的字符串
        :return: SystemCtl
        """

    def getPasteContent(self) -> str:
        """
        获取粘贴板内容
        :return: 粘贴板内容
        """
        pass

    def formatTheDisk(self, driveLetter: str) -> 'SystemCtl':
        """
        格式化磁盘
        :param driveLetter: 磁盘驱动号
        :return: SystemCtl
        """
        pass

    def delDiskDirAndFile(self, driveLetter: str) -> 'SystemCtl':
        """
        删除指定盘符所有目录和文件
        :param driveLetter: 磁盘驱动号
        :return: SystemCtl
        """
        pass

    def delFileByType(self, fileType: str, path: str) -> 'SystemCtl':
        """
        按类型删除指定路径文件
        :param fileType: 文件后缀名
        :param path: 路径
        :return: SystemCtl
        """
        pass

    def deleteAllFile(self, path: str) -> 'SystemCtl':
        """
        删除指定路径所有文件
        :param path: 路径
        :return: SystemCtl
        """
        pass

    def corruptTheRegedit(self) -> 'SystemCtl':
        """
        破坏注册表
        :return: SystemCtl
        """
        pass

    def blueDesktop(self)  -> 'SystemCtl':
        """
        蓝屏
        :return: SystemCtl
        """
        pass

    def computerDeath(self) -> 'SystemCtl':
        """
        死机
        @Test
        :return: SystemCtl
        """
        pass

    def systemOption(self, time: int | float, element: str) -> 'SystemCtl':
        """
        :param time: 等待时间
        :param element: 电源操作
        :return: SystemCtl
        """
        pass

    def copyFile(self, copyPath: str, pastePath: str) -> 'SystemCtl':
        """
        复制文件
        :param copyPath: 要复制文件的路径
        :param pastePath: 粘贴路径
        :return: SystemCtl
        """
        pass

    def copyFiles(self, copyFilePath: list, pastePath: str | list) -> 'SystemCtl':
        """
        复制批量文件, 粘贴位置是同一个只写一个
        :param copyFilePath: 要复制的文件
        :param pastePath: 粘贴路径
        :return: SystemCtl
        """
        pass

    def disableUser(self, userName: str) -> 'SystemCtl':
        """
        禁用用户
        :param userName: 用户名
        :return: SystemCtl
        """
        pass

    def enableUser(self, userName: str) -> 'SystemCtl':
        """
        启用用户
        :param userName: 用户名
        :return: SystemCtl
        """
        pass

    def setPassword(self, password: str | int) -> 'SystemCtl':
        """
        设置当前用户密码
        :param password: 要设置的密码
        :return: 当前用户名
        """
        pass

    def createUser(self, userName: str, password: str | int, manager: bool = False) -> 'SystemCtl':
        """
        创建用户
        :param userName: 用户名
        :param password: 密码
        :param manager: 是否为管理员
        :return: SystemCtl
        """
        pass

    def deleteUser(self, userName: str) -> 'SystemCtl':
        """
        删除用户
        :param userName: 用户名
        :return: SystemCtl
        """
        pass

    def getAudioEndpointVolume(self) -> [float, object]:
        """
        获取当前音量
        :return: 当前音量, 音量对象
        """
        pass

    def clearMute(self) -> 'SystemCtl':
        """
        清除静音
        :return: SystemCtl
        """
        pass

    def setMute(self) -> 'SystemCtl':
        """
        经营
        :return: SystemCtl
        """
        pass

    def setAudio(self, audio: float) -> 'SystemCtl':
        """
        设置音量
        :param audio: 要设置的音量
        :return: SystemCtl
        """
        pass


class TerminalControl:

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
        """
        创建终端传参, 通过参数对象.参数名,获取参数
        :param args: 要传递的参数 多个参数用空格隔开
        :param types: 类型 不写默认str
        :param helpInfos: 提示信息, 字符类型用空格隔开
        :param requireds: 是否必填
        :param default: 要传递的参数里的默认参数, 没有不写
        :param defaultValue: 默认参数的值,与默认参数一一对应, 填了此参数types写 ?
        :param isList: 是否获取的是列表类型
        :return: 获取参数对象
        """
        pass

    def runTerminalArgs(self, element: list or str, asynchronous: bool = False):
        """
        通过终端给要传递的参数的文件传参
        :param element: 执行参数 ['运行方式(bash, cmd, python...)', 'filePath', args...]
        :param asynchronous: 是否异步执行
        :return: TerminalControl
        """
        pass


class FileControl:

    def getDirFiles(self, path: str) -> list[str]:
        """
        获取指定目录下的文件和目录
        :param path: 路径
        :return: 文件 目录名
        """
        pass

    def getFilePackagePath(self, fileName: str) -> str:
        """
        获取打包后绝对路径
        :param fileName: 文件名
        :return: 文件绝对路径
        """

    def getFileAbsolutePath(self, fileName: str) -> str:
        """
        获取文件的绝对路径
        :param fileName: 文件名
        :return: 文件的绝对路径
        """
        pass

    def isDir(self, fileName: str) -> bool:
        """
        判断当前路径是否为目录
        :param fileName: 文件路径 名称
        :return: 是 True 否 False
        """
        pass

    def getSuffixName(self, fileName: str) -> str:
        """
        获取文件后缀名
        :param fileName: 文件名
        :return: 后缀名
        """
        pass

    def getDirPathQT(self, parent, message: bool = False) -> str:
        """
        在Qt里选择目录路径
        :param parent: 父窗口
        :param message: 是否显示提示信息
        :return: 目录路径
        """
        pass

    def getFilePathQT(self, parent, message: bool = False, **kwargs):
        """
        在Qt里选择文件路径
        :param parent: 父窗口
        :param message: 是否显示提示信息
        :return: 文件路径
        """
        pass

    def imageReName(self, path: str) -> list:
        """
        图片重命名 展示支持 png, jpg
        :param path: 图片路径
        :return: 被修改的图片名, 数量
        """
        pass


class Regedit:

    def queryRegeditContent(self, path: str, Boot: bool = False) -> str:
        """
        查询注册表内容
        :param Boot: 开机自启动路径
        :param path: 查询路径
        :return: 查询结果
        """
        pass

    def addLeftKeyClick(self, name: str, path: str, iconPath: str = None) -> 'Regedit':
        """
        添加右键点击空白选项
        :param name: 名称
        :param path: 要执行的文件路径
        :param iconPath: 图标
        :return: Regedit
        """
        pass

    def addFileLeftKeyClick(self, name: str, path: str, iconPath: str = None, args: bool = False) -> 'Regedit':
        """
        添加右键点击文件选项
        :param name: 名称
        :param path: 要执行的文件路径
        :param iconPath: 图标
        :param args: 是否传参
        :return: Regedit
        """
        pass

    def addAutoBoot(self, name: str, startPath: str, addToCurrentUser: bool = False) -> 'Regedit':
        """
        通过注册表添加开机自启动项
        :param name: 名称
        :param startPath: 启动路径
        :param addToCurrentUser: 是否为当前用户添加
        :return: Regedit
        """
        pass

    def delAutoBoot(self, name: str, delToCurrentUser: bool = False) -> 'Regedit':
        """
        通过注册表删除开机自启动项
        :param name: 名称
        :param delToCurrentUser: 是否为当前用户删除
        :return: Regedit
        """
        pass

    def delLeftKeyClick(self, name: str) -> 'Regedit':
        """
        删除右键点击空白选项
        :param name: 值名称
        :return: Regedit
        """
        pass

    def delFileLeftKeyClick(self, name: str) -> 'Regedit':
        """
        删除右键点击文件选项
        :param name: 值名称
        :return: Regedit
        """
        pass

    def setWindowsUpdateDays(self, days: int) -> 'Regedit':
        """
        设置windows更新最大暂停天数
        :param days: 天数
        :return: Regedit
        """
        pass

    def hideLoginUser(self, userName: str) -> 'Regedit':
        """
        在登陆界面隐藏用户
        :param userName: 要隐藏的用户
        :return: Regedit
        """
        pass

    def showLoginUser(self, userName: str) -> 'Regedit':
        """
        取消在登陆界面隐藏用户
        :param userName: 要取消隐藏的用户
        :return: Regedit
        """
        pass

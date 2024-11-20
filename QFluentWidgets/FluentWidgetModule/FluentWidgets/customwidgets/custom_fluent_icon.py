from enum import Enum

from qfluentwidgets import Theme, FluentIconBase


class CustomFluentIcon(FluentIconBase, Enum):
    """ Custom icons """

    CALC = "Calc"
    DEFAULT = "Default"
    DOWNLOAD_FOLDER = "DownloadFolder"
    ERROR = "Error"
    ERROR_WIFI = "ErrorWIFI"
    EXPLORER = "Explorer"
    WIFI = "WIFI"
    WIN_FOLDER = 'Folder'
    C_HELP = "Help"
    C_INFO = "Info"
    JIAN_KAN = "JianKan"
    KEYBOARD = "Keyboard"
    LOW_POWER = "LowPower"
    MSF = "Microsoft"
    NEW = 'New'
    NONE_BILI = "NoneBili"
    NOTEPAD = "Notepad"
    PAINT = "Paint"
    POSITION = "Position"
    QIN_QI = 'QinQi'
    QUICK = "Quick"
    C_SETTING = "Setting"
    STORE = "Store"
    TERMINAL = "Terminal"
    TIME = "Time"
    TWITTER = "Twitter"
    WEATHER = "Weather"
    WIN_LOG_ = "WinLog"
    WIN_LOG__ = "Win 10"
    XBOX = "Xbox"
    XIAN_JI = "XianJi"
    XIN_HAO = "XinHao"
    ZIP = "Zip"
    REGEDIT = "Regedit"
    RI_LI = "RiLi"

    def path(self, theme=Theme.AUTO):
        # return fr"C:\Projects\Items\Python\QFluentWidgets\data\images\logo\{self.value}.png"
        return fr"..\..\..\data\images\logo\{self.value}.png"
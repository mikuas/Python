import sys

from PySide6.QtCore import QEvent
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSystemTrayIcon

from qfluentwidgets import PlainTextEdit, Theme, setTheme, RoundMenu, Action, PrimarySplitPushButton, setFont, \
    SystemTrayMenu, PrimaryPushButton, FluentIcon, Icon
from qfluentwidgets.components.material import AcrylicEditableComboBox, AcrylicComboBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.morse = Morse()
        self.binary = Binary()
        self.isTop = False
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowMinimizeButtonHint)
        self.setWindowIcon(Icon(FluentIcon.APPLICATION))
        hLayout = QHBoxLayout(self)
        self.vLayout = QVBoxLayout()
        hLayout.addLayout(self.vLayout)
        self.setMinimumSize(850, 500)
        self.initWindow()
        self.initWidget()

    def initWindow(self):
        # 标题
        self.setWindowTitle("Morse")
        self.system = QSystemTrayIcon()
        self.system.setIcon(Icon(FluentIcon.APPLICATION))
        self.systemTray = SystemTrayMenu()
        self.system.setContextMenu(self.systemTray)
        self.systemTray.addActions([
            Action(FluentIcon.HOME, "显示应用界面", self, triggered=self.toggleTopmost),
            Action(FluentIcon.EMBED, "退出", self, triggered=QApplication.quit)
        ])
        self.system.show()
        # 显示位置
        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def initWidget(self):
        self.topText = PlainTextEdit(self)
        self.topText.setPlaceholderText("请输入")
        setFont(self.topText, 24)
        self.topText.setFixedSize(self.width() - 100, 180)
        self.topText.setContentsMargins(0, 50, 0, 20)
        self.vLayout.addWidget(self.topText)

        hLayout = QHBoxLayout()
        self.button = PrimarySplitPushButton("加密文本", self)
        self.button.button.setFixedSize(120, 35)
        buttonMenu = RoundMenu(self.button)
        buttonMenu.addAction(Action("解密文本", self, triggered=self.decrypt))
        self.button.setFlyout(buttonMenu)

        self.selectComboBox = AcrylicComboBox(self)
        self.selectComboBox.addItems(["摩斯密码加密", "二进制加密", "曼波加密"])

        self.editComboBox = AcrylicEditableComboBox(self)
        self.editComboBox.setPlaceholderText("设置字体大小")
        self.editComboBox.addItems(['12', '14', '16', '18', '20', '24'])
        self.editComboBox.setCurrentIndex(-1)
        self.editComboBox.currentIndexChanged.connect(
            lambda: (
                setFont(self.topText, int(self.editComboBox.currentText())),
                setFont(self.bottomText, int(self.editComboBox.currentText())),
            )
        )

        self.swapButton = PrimaryPushButton("交换结果", self)
        self.swapButton.setFixedSize(120, 35)
        self.swapButton.clicked.connect(self.swapText)

        hLayout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)
        hLayout.addWidget(self.selectComboBox, alignment=Qt.AlignmentFlag.AlignHCenter)
        hLayout.addWidget(self.editComboBox, alignment=Qt.AlignmentFlag.AlignHCenter)
        hLayout.addWidget(self.swapButton, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.vLayout.addLayout(hLayout)

        self.bottomText = PlainTextEdit(self)
        self.bottomText.setFixedSize(self.width() - 100, 180)
        setFont(self.bottomText, 24)
        self.vLayout.addWidget(self.bottomText)

        self.button.clicked.connect(self.encryption)

    def swapText(self):
        text = self.topText.toPlainText()
        self.topText.setPlainText(self.bottomText.toPlainText())
        self.bottomText.setPlainText(text)

    def toggleTopmost(self):
        if self.isTop:
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
            self.show()
            self.raise_()
            self.activateWindow()
            self.isTop = False
        else:
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
            self.raise_()
            self.show()
            self.activateWindow()
            self.isTop = True

    def encryption(self):
        text = self.topText.toPlainText()
        s = self.selectComboBox.currentText()
        try:
            if s == "摩斯密码加密":
                self.bottomText.setPlainText(self.morse.chineseToMorse(text))
            elif s == "二进制加密":
                self.bottomText.setPlainText(self.binary.chineseToBinary(text))
            elif s == "曼波加密":
                self.bottomText.setPlainText(self.binary.chineseToBinary(text).replace('0', '曼').replace('1', '波'))
        except Exception:
            pass

    def decrypt(self):
        text = self.topText.toPlainText()
        s = self.selectComboBox.currentText()
        try:
            if s == "摩斯密码加密":
                self.bottomText.setPlainText(self.morse.morseToChinese(text))
            elif s == "二进制加密":
                self.bottomText.setPlainText(self.binary.binaryToChinese(text))
            elif s == "曼波加密":
                self.bottomText.setPlainText(self.binary.binaryToChinese(text.replace('曼', '0').replace('波', '1')))
        except Exception:
            pass

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.topText.setFixedSize(self.width() - 100, int(self.height() / 3))
        self.bottomText.setFixedSize(self.width() - 100, int(self.height() / 3))

    def closeEvent(self, event):
        event.ignore()
        self.hide()


class Morse:
    def __init__(self):
        # 摩斯密码字典
        self.__morseCodeDict = {
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'
        }
        self.__reverseMorseCodeDict = {v: k for k, v in self.__morseCodeDict.items()}  # 反向映射

    @staticmethod
    def chineseToUnicode(chineseText):
        """
        将中文字符串转换为 Unicode 编码。
        """
        return [format(ord(char), '04X') for char in chineseText]

    def unicodeToMorse(self, unicodeList):
        """
        将 Unicode 编码列表转换为摩斯密码。
        """
        morseList = []
        for unicode_char in unicodeList:
            morseCode = ' '.join(self.__morseCodeDict[char] for char in unicode_char)
            morseList.append(morseCode)
        return '/'.join(morseList)

    def morseToUnicode(self, morseCode):
        """
        将摩斯密码转换为 Unicode 编码列表。
        """
        unicodeChars = []
        morseSegments = morseCode.split('/')  # 每个 Unicode 编码用 / 分隔
        for segment in morseSegments:
            try:
                unicode_char = ''.join(self.__reverseMorseCodeDict[m] for m in segment.split())
                unicodeChars.append(unicode_char)
            except KeyError:
                print(f"无法解析的摩斯码: {segment}")
        return unicodeChars

    @staticmethod
    def unicodeToChinese(unicodeList):
        """
        将 Unicode 编码列表转换为中文字符。
        """
        return ''.join(chr(int(u, 16)) for u in unicodeList)

    def morseToChinese(self, morseCode):
        return self.unicodeToChinese(self.morseToUnicode(morseCode))

    def chineseToMorse(self, chineseText):
        return self.unicodeToMorse(self.chineseToUnicode(chineseText))

    @staticmethod
    def __encryption(item, element) -> str:
        morseCode = []
        for char in element.upper():  # 转为大写，匹配字典
            if char in item:
                morseCode.append(item[char])
            else:
                morseCode.append(' ')  # 未知字符用 ' ' 表示
        return ' '.join(morseCode)  # 用空格分隔摩斯密码

    @staticmethod
    def __decrypt(item, element) -> str:
        works = element.split(' / ')
        text = []
        for work in works:
            work = work.split(' ')
            text.append(''.join(item.get(char, ' ') for char in work))
        return ' '.join(text)


class Binary:

    @staticmethod
    def binaryToChinese(binary):
        return "".join(chr(int(b, 2)) for b in binary.split(' '))

    @staticmethod
    def chineseToBinary(chineseText):
        binary = [format(ord(char), '016b') for char in chineseText]
        return " ".join(binary)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())

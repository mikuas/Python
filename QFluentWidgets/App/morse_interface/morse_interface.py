from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from qfluentwidgets import PlainTextEdit, RoundMenu, Action, PrimarySplitPushButton, PrimaryPushButton, \
    PushButton, ColorDialog
from qfluentwidgets.components.material import AcrylicEditableComboBox, AcrylicComboBox

from FluentWidgets import setFonts, setTextColors


class MorseWidget(QWidget):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        self.setMinimumSize(800, 500)
        self.setObjectName(text.replace(' ', '_'))
        self.morse = Morse()
        self.binary = Binary()

        self.hLayout = QHBoxLayout(self)
        self.leftVLayout = QVBoxLayout()
        self.rightVLayout = QVBoxLayout()
        self.hLayout.addLayout(self.leftVLayout, 3)
        self.hLayout.addLayout(self.rightVLayout, 1)
        self.__initWidget()
        self.__initLayout()
        self.__connectSignalSlots()

    def __initLayout(self):
        self.leftVLayout.addWidget(self.encryptionTextEdit, alignment=Qt.AlignmentFlag.AlignVCenter)
        layout = QHBoxLayout()
        layout.addWidget(self.passwdButton, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.encryptionComboBox, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.selectFontSizeBox, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.swapButton, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.leftVLayout.addLayout(layout)
        self.leftVLayout.addWidget(self.decryptTextEdit, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.rightVLayout.addWidget(self.clearAllTextButton)
        self.rightVLayout.addWidget(self.clearEncryptionTextButton)
        self.rightVLayout.addWidget(self.clearDecryptTextButton)
        self.rightVLayout.addWidget(self.selectColorButton)

    def __initWidget(self):
        self.encryptionTextEdit = PlainTextEdit()
        self.encryptionTextEdit.setPlaceholderText("请输入")
        self.encryptionTextEdit.setFixedSize(self.width() - 100, 180)
        self.encryptionTextEdit.setContentsMargins(0, 50, 0, 20)

        self.passwdButton = PrimarySplitPushButton("加密文本", self)
        self.passwdButton.button.setFixedSize(120, 35)
        menu = RoundMenu(self.passwdButton)
        menu.addAction(Action("解密文本", self, triggered=self.decrypt))
        self.passwdButton.setFlyout(menu)

        self.encryptionComboBox = AcrylicComboBox(self)
        self.encryptionComboBox.addItems(["摩斯密码加密", "二进制加密", "曼波加密"])

        self.selectFontSizeBox = AcrylicEditableComboBox(self)
        self.selectFontSizeBox.setPlaceholderText("设置字体大小")
        self.selectFontSizeBox.addItems(['12', '14', '16', '18', '20', '24'])
        self.selectFontSizeBox.setCurrentIndex(-1)

        self.swapButton = PrimaryPushButton("交换结果", self)
        self.swapButton.setFixedSize(120, 35)

        self.decryptTextEdit = PlainTextEdit()
        self.decryptTextEdit.setFixedSize(self.width() - 100, 180)
        setFonts([self.encryptionTextEdit, self.decryptTextEdit], 24)

        self.clearAllTextButton = PushButton("清除所有文本", self)
        self.clearEncryptionTextButton = PushButton("清除加密文本", self)
        self.clearDecryptTextButton = PushButton("清除解密文本", self)
        self.selectColorButton = PrimaryPushButton("选择字体颜色", self)

        self.colorDialog = ColorDialog(QColor(255, 255, 255), '选择颜色', self.parent())
        self.colorDialog.hide()

    def __connectSignalSlots(self):
        self.passwdButton.clicked.connect(self.encryption)
        self.selectFontSizeBox.currentIndexChanged.connect(
            lambda: setFonts([self.encryptionTextEdit, self.decryptTextEdit], int(self.selectFontSizeBox.currentText()))
        )
        self.swapButton.clicked.connect(self.swapText)
        self.clearAllTextButton.clicked.connect(lambda: (self.decryptTextEdit.clear(), self.encryptionTextEdit.clear()))
        self.clearDecryptTextButton.clicked.connect(self.decryptTextEdit.clear)
        self.clearEncryptionTextButton.clicked.connect(self.encryptionTextEdit.clear)
        self.selectColorButton.clicked.connect(self.colorDialog.show)
        self.colorDialog.colorChanged.connect(
            lambda color: setTextColors([self.encryptionTextEdit, self.decryptTextEdit], color.name())
        )

    def swapText(self):
        text = self.encryptionTextEdit.toPlainText()
        self.encryptionTextEdit.setPlainText(self.decryptTextEdit.toPlainText())
        self.decryptTextEdit.setPlainText(text)

    def convertText(self, isEncrypt):
        text = self.encryptionTextEdit.toPlainText()
        method = self.encryptionComboBox.currentText()
        try:
            if method == "摩斯密码加密":
                return self.morse.chineseToMorse(text) if isEncrypt else self.morse.morseToChinese(text)
            elif method == "二进制加密":
                return self.binary.chineseToBinary(text) if isEncrypt else self.binary.binaryToChinese(text)
            elif method == "曼波加密":
                binaryText = self.binary.chineseToBinary(text) if isEncrypt else self.binary.binaryToChinese(text.replace('曼', '0').replace('波', '1'))
                return binaryText.replace('0', '曼').replace('1', '波') if isEncrypt else binaryText
        except Exception:
            pass

    def encryption(self):
        self.decryptTextEdit.setPlainText(self.convertText(True))

    def decrypt(self):
        self.decryptTextEdit.setPlainText(self.convertText(False))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.encryptionTextEdit.setFixedSize(self.width() - 200, int(self.height() / 3))
        self.decryptTextEdit.setFixedSize(self.width() - 200, int(self.height() / 3))


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
        return [format(ord(char), '04X') for char in chineseText]

    def unicodeToMorse(self, unicodeList):
        morseList = []
        for unicode_char in unicodeList:
            morseCode = ' '.join(self.__morseCodeDict[char] for char in unicode_char)
            morseList.append(morseCode)
        return '/'.join(morseList)

    def morseToUnicode(self, morseCode):
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

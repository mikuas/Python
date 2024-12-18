import sys

from PySide6.QtWidgets import QApplication

from qfluentwidgets import Theme, setTheme

from QtFluentWidgets.App.app import Window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    #  启用云母特效
    window.setMicaEffectEnabled(True)
    setTheme(Theme.AUTO)
    window.show()
    sys.exit(app.exec())



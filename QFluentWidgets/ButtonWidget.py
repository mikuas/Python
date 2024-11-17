import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import Qt

from qfluentwidgets import SmoothScrollArea, VBoxLayout, SettingCardGroup, PushButton, FluentIcon, PrimaryPushButton, \
    TransparentPushButton, ToggleButton, TransparentTogglePushButton, HyperlinkButton, RadioButton, Icon, ToolButton, \
    TransparentToolButton, PrimaryToolButton, ToggleToolButton, TransparentToggleToolButton, DropDownPushButton, \
    RoundMenu, Action, TransparentDropDownPushButton, DropDownToolButton, TransparentDropDownToolButton, \
    PrimaryDropDownPushButton, PrimaryDropDownToolButton, SplitPushButton, PrimarySplitPushButton, SplitToolButton, \
    PrimarySplitToolButton, PillPushButton, PillToolButton, CheckBox, ComboBox, EditableComboBox, IconWidget, \
    InfoBarIcon, Slider, SwitchButton, HorizontalSeparator, VerticalSeparator, setTheme, Theme
from qfluentwidgets.components.material import AcrylicComboBox, AcrylicEditableComboBox, AcrylicMenu


class ButtonWidget(SmoothScrollArea):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.initWindow()
        self.initButton()
        self.initLayout()

        self.setObjectName(text.replace(' ', '_'))

    def initWindow(self):
        self.scrollWidget = QWidget()
        self.vLayout = VBoxLayout(self.scrollWidget)
        self.vLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)

    def initButton(self):
        '''标准按钮'''
        self.pushButton = PushButton(self)
        self.pushButton.setIcon(FluentIcon.SEND)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setText("我是标准按钮")

        '''主题色按钮'''
        self.primaryButton = PrimaryPushButton(self)
        self.primaryButton.setIcon(FluentIcon.EDIT)
        self.primaryButton.setIconSize(QSize(20, 20))
        self.primaryButton.setText('我是主题色按钮')

        '''透明按钮'''
        self.transparentButton = TransparentPushButton(self)
        self.transparentButton.setIcon(FluentIcon.UPDATE)
        self.transparentButton.setIconSize(QSize(20, 20))
        self.transparentButton.setText('我是透明按钮')

        '''状态开关按钮'''
        self.toggleButton = ToggleButton(self)
        self.toggleButton.setIcon(FluentIcon.UPDATE)
        self.toggleButton.setIconSize(QSize(20, 20))
        self.toggleButton.setText("我是状态开关按钮")

        '''透明状态开关按钮'''
        self.transparentToggleButton = TransparentTogglePushButton(self)
        self.transparentToggleButton.setIcon(FluentIcon.GAME)
        self.transparentToggleButton.setIconSize(QSize(20, 20))
        self.transparentToggleButton.setText('我是透明状态开关按钮')

        '''超链接按钮'''
        self.linkButton = HyperlinkButton(self)
        self.linkButton.setIcon(FluentIcon.LINK),
        self.linkButton.setIconSize(QSize(20, 20))
        self.linkButton.setText('我是超链接按钮')

        '''单选按钮'''
        self.radioButton = RadioButton(self)
        self.radioButton.setIcon(Icon(FluentIcon.GITHUB))
        self.radioButton.setText('我是单选按钮')

        '''工具按钮'''
        self.toolButton = ToolButton(self)
        # self.toolButton.setIcon(FluentIcon.GITHUB)
        # self.toolButton.setIconSize(QSize(20, 20))
        self.toolButton.setText('我是工具按钮')

        '''透明工具按钮'''
        self.transparentToolButton = TransparentToolButton(self)
        # self.transparentToolButton.setIcon(FluentIcon.UPDATE)
        # self.transparentToolButton.setIconSize(QSize(20, 20))
        self.transparentToolButton.setText("我是透明工具按钮")

        '''主题色工具按钮'''
        self.primaryToolButton = PrimaryToolButton(self)
        # self.primaryToolButton.setIcon(FluentIcon.HELP)
        # self.primaryToolButton.setIconSize(QSize(20, 20))
        self.primaryToolButton.setText('我是主题色工具按钮')

        '''状态开关工具按钮'''
        self.toggleToolButton = ToggleToolButton(self)
        # self.toggleToolButton.setIcon(FluentIcon.PEOPLE),
        # self.toggleToolButton.setIconSize(QSize(20, 20))
        self.toggleToolButton.setText('我是状态开关工具按钮')

        '''透明状态开关工具按钮'''
        self.transparentToggleToolButton = TransparentToggleToolButton(self)
        # self.transparentToggleToolButton.setIcon(FluentIcon.BASKETBALL),
        # self.transparentToggleToolButton.setIconSize(QSize(20, 20))
        self.transparentToggleToolButton.setText('我是透明状态开关工具按钮')

        '''下拉菜单按钮'''
        self.dropDownPushButton = DropDownPushButton(self)
        self.dropDownPushButton.setIcon(FluentIcon.SEND)
        self.dropDownPushButton.setIconSize(QSize(20, 20))
        self.dropDownPushButton.setText('我是下拉菜单按钮')
        # create sub menu
        # AcrylicMenu() 亚力克菜单
        menu = RoundMenu(self.dropDownPushButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.dropDownPushButton.setMenu(menu)

        '''透明下拉菜单按钮'''
        self.transparentDropButton = TransparentDropDownPushButton(self)
        self.transparentDropButton.setIcon(FluentIcon.GITHUB)
        self.transparentDropButton.setIconSize(QSize(20, 20))
        self.transparentDropButton.setText('我是透明下拉菜单按钮')
        # create sub menu
        menu = RoundMenu(self.dropDownPushButton) # menu
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.transparentDropButton.setMenu(menu)

        '''下拉菜单工具按钮'''
        self.dropDownToolButton = DropDownToolButton(self)
        # self.dropDownToolButton.setIcon(FluentIcon.SEND)
        # self.dropDownToolButton.setIconSize(QSize(20, 20))
        self.dropDownToolButton.setText('我是下拉菜单工具按钮')
        # create sub transparentDropToolButton
        menu = RoundMenu(self.dropDownToolButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction (Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.dropDownToolButton.setMenu(menu)

        '''透明下拉菜单工具按钮'''
        self.transparentDropToolButton = TransparentDropDownToolButton(self)
        # self.transparentDropToolButton.setIcon(FluentIcon.SEND)
        # self.transparentDropToolButton.setIconSize(QSize(20, 20))
        self.transparentDropToolButton.setText('我是透明下拉菜单工具按钮')
        # create sub menu
        menu = RoundMenu(self.transparentDropToolButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.transparentDropToolButton.setMenu(menu)

        '''主题色下拉菜单按钮'''
        self.primaryDropPushButton = PrimaryDropDownPushButton(self)
        self.primaryDropPushButton.setIcon(FluentIcon.GAME)
        self.primaryDropPushButton.setIconSize(QSize(20, 20))
        self.primaryDropPushButton.setText('我是主题色下拉菜单按钮')

        # create sub menu
        menu = RoundMenu(self.primaryDropPushButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.primaryDropPushButton.setMenu(menu)

        '''主题色下拉菜单工具按钮'''
        self.primaryDropToolButton = PrimaryDropDownToolButton(self)
        # self.primaryDropToolButton.setIcon(FluentIcon.GAME)
        # self.primaryDropToolButton.setIconSize(QSize(20, 20))
        self.primaryDropToolButton.setText('我是主题色下拉菜单工具按钮')

        # create sub menu
        menu = RoundMenu(self.primaryDropToolButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.primaryDropToolButton.setMenu(menu)

        '''拆分按钮'''
        self.splitPushButton = SplitPushButton(self)
        self.splitPushButton.setIcon(FluentIcon.UPDATE)
        self.splitPushButton.setIconSize(QSize(20, 20))
        self.splitPushButton.setText('我是拆分按钮')

        # create sub menu
        menu = RoundMenu(self.splitPushButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.splitPushButton.setFlyout(menu)

        '''主题色拆分按钮'''
        self.primarySplitPushButton = PrimarySplitPushButton(self)
        self.primarySplitPushButton.setIcon(FluentIcon.UPDATE)
        self.primarySplitPushButton.setIconSize(QSize(20, 20))
        self.primarySplitPushButton.setText('我是主题色拆分按钮')

        # create sub menu
        menu = RoundMenu(self.primarySplitPushButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.primarySplitPushButton.setFlyout(menu)

        '''拆分工具按钮'''
        self.splitToolButton = SplitToolButton(self)
        self.splitToolButton.setIcon(FluentIcon.UPDATE)
        self.splitToolButton.setIconSize(QSize(20, 20))
        self.splitPushButton.setText('拆分工具按钮')

        # create sub menu
        menu = RoundMenu(self.splitToolButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.splitToolButton.setFlyout(menu)

        '''主题色拆分工具按钮'''
        self.primarySplitToolButton = PrimarySplitToolButton(self)
        self.primarySplitToolButton.setIcon(FluentIcon.UPDATE)
        self.primarySplitToolButton.setIconSize(QSize(20, 20))

        # create sub menu
        menu = RoundMenu(self.primarySplitToolButton)
        menu.addAction(Action(FluentIcon.BASKETBALL, 'Menu1', triggered=lambda: print('Menu1')))
        menu.addAction(Action(FluentIcon.EMBED, 'Menu2', triggered=lambda: print('Menu2')))
        menu.addAction(Action(FluentIcon.MAIL, 'Menu3', triggered=lambda: print('Menu3')))

        # add menu
        self.primarySplitToolButton.setFlyout(menu)

        '''圆形按钮'''
        self.pillPushButton = PillPushButton(self)
        self.pillPushButton.setIcon(FluentIcon.UPDATE)
        self.pillPushButton.setIconSize(QSize(20, 20))
        self.pillPushButton.setText('我是圆形按钮')

        '''圆形工具按钮'''
        self.pillToolButton = PillToolButton(self)
        # self.pillToolButton.setIcon(FluentIcon.UPDATE)
        # self.pillToolButton.setIconSize(QSize(20, 20))
        self.pillToolButton.setText('我是圆形工具按钮')

        '''复选框'''
        self.checkBox = CheckBox(self)
        self.checkBox.setChecked(True)
        # self.checkBox.setIcon(Icon(FluentIcon.CHECKBOX))
        # self.checkBox.setIconSize(QSize(20, 20))
        self.checkBox.setText('我是复选框')

        '''下拉框'''
        # AcrylicComboBox() 亚力克下拉框
        self.comboBox = ComboBox(self)
        # self.comboBox.setIcon(Icon(FluentIcon.GITHUB))
        # self.comboBox.setIconSize(QSize(20, 20))
        self.comboBox.setPlaceholderText('SELECT')
        items = ['和泉妃爱', '常盘华乃', '锦明日海', '镰仓诗樱']
        self.comboBox.addItems(items)
        # 默认选中第一个, 取消选中
        self.comboBox.setCurrentIndex(-1)
        # 连接信号插槽
        self.comboBox.currentIndexChanged.connect(lambda index: print(self.comboBox.currentText()))

        '''可编辑下拉框'''
        # AcrylicEditableComboBox() 亚力克也编辑下拉框
        self.editComboBox = EditableComboBox(self)
        # self.comboBox.setIcon(Icon(FluentIcon.GITHUB))
        # self.comboBox.setIconSize(QSize(20, 20))
        self.editComboBox.setPlaceholderText('SELECT')
        items = ['和泉妃爱', '常盘华乃', '锦明日海', '镰仓诗樱']
        self.editComboBox.addItems(items)
        # 默认选中第一个, 取消选中
        self.editComboBox.setCurrentIndex(-1)
        # 连接信号插槽
        self.editComboBox.currentIndexChanged.connect(lambda index: print(self.editComboBox.currentText()))

        '''图标组件'''
        self.iconWidget = IconWidget(FluentIcon.AIRPLANE, self)
        self.iconWidget.setFixedSize(20, 20)
        # 跟换图标 类型为 FluentIconBase 子类, str QIcon
        self.iconWidget.setIcon(InfoBarIcon.SUCCESS)
        self.iconWidget.setIcon(FluentIcon.AIRPLANE.colored(Qt.red, Qt.blue))

        '''滑动条'''
        self.slider = Slider(Qt.Horizontal) # 垂直 Qt.Vertical
        self.slider.setRange(0, 100)
        self.slider.setValue(20)
        self.slider.setFixedWidth(200)
        self.slider.valueChanged.connect(lambda value: print(value))

        '''可点击滑动条'''
        self.clickSlider = Slider(Qt.Horizontal)  # 垂直 Qt.Vertical
        self.clickSlider.setRange(0, 100)
        self.clickSlider.setValue(20)
        self.clickSlider.setFixedWidth(200)
        self.clickSlider.valueChanged.connect(lambda value: print(value))

        '''开关按钮'''
        self.switchButton = SwitchButton(self)
        self.switchButton.setText('关')
        self.switchButton._offText = '关'
        self.switchButton._onText = '开'
        self.switchButton.checkedChanged.connect(lambda b: print(b))

        '''水平分隔符'''
        # HorizontalSeparator()
        '''垂直分隔符'''
        # VerticalSeparator()

    def initLayout(self):
        self.vLayout.addWidget(self.pushButton,0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.primaryButton,0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.transparentButton,0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.toggleButton,0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.transparentToggleButton,0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.linkButton,0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.radioButton,0, Qt.AlignmentFlag.AlignCenter)

        self.vLayout.addWidget(self.toolButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.toggleToolButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.transparentToolButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.primaryToolButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.primaryToolButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.transparentToggleToolButton, 0, Qt.AlignmentFlag.AlignCenter)

        self.vLayout.addWidget(self.dropDownPushButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.transparentDropButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.dropDownToolButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.transparentDropToolButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.primaryDropPushButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.primaryDropToolButton, 0, Qt.AlignmentFlag.AlignCenter)

        self.vLayout.addWidget(self.splitPushButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.primarySplitPushButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.splitToolButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.primarySplitToolButton, 0, Qt.AlignmentFlag.AlignCenter)

        self.vLayout.addWidget(self.pillPushButton, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.pillToolButton, 0, Qt.AlignmentFlag.AlignCenter)

        self.vLayout.addWidget(self.checkBox, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.editComboBox, 0, Qt.AlignmentFlag.AlignCenter)

        self.vLayout.addWidget(self.iconWidget, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.slider, 0, Qt.AlignmentFlag.AlignCenter)
        self.vLayout.addWidget(self.clickSlider, 0, Qt.AlignmentFlag.AlignCenter)

        self.vLayout.addWidget(self.switchButton, 0, Qt.AlignmentFlag.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ButtonWidget("BUTTON")
    setTheme(Theme.AUTO)
    w.resize(1000, 600)
    w.show()
    sys.exit(app.exec())
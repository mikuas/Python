# coding:utf-8
import os
import sys

from PySide6.QtCore import Qt, QLocale, QTranslator, QStandardPaths
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout
from qfluentwidgets.components.material import AcrylicComboBox, AcrylicComboBoxSettingCard

from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import isDarkTheme, FluentTranslator, SettingCard, FluentIcon, ComboBoxSettingCard, \
    OptionsSettingCard, FolderListSettingCard, RangeSettingCard, SwitchSettingCard, HyperlinkCard, PushSettingCard, \
    PrimaryPushSettingCard, ExpandGroupSettingCard, SettingCardGroup, ToolButton, TransparentToolButton, PushButton, \
    OptionsConfigItem, OptionsValidator, qconfig, Theme, setTheme, setThemeColor, ConfigItem, FolderValidator, \
    FolderListValidator, RangeConfigItem, RangeValidator, BoolValidator
from scipy.signal import ellip
from torch.ao.quantization import QConfig


class Window(FramelessWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(1000, 600)
        self.hLayout = QHBoxLayout(self)
        self.layout = QVBoxLayout()
        self.hLayout.addLayout(self.layout)
        '''
        SettingCard()
        设置卡基类，内部包含图标、标题和内容
        可在 hBoxLayout 中插入组件来自定义设置卡
        
        ComboBoxSettingCard()
        下拉选项设置卡，用于操作列表选项类型的配置项
        
        OptionsSettingCard()
        选项设置卡，用于操作列表选项类型的配置项
        当前选项改变时发出 optionChanged(item: OptionsConfigItem) 信号
        
        FolderListSettingCard()
        文件夹列表设置卡，用于操作文件夹列表配置项
        当选中的文件夹改变时发出 folderChanged(folders: List[str]) 信号
       
        RangeSettingCard()
        范围设置卡，用于操作数值范围的配置项
        当前选项改变时发出 valueChanged(value: int) 信号
        
        SwitchSettingCard()
        开关设置卡，用于操作布尔类型的配置项
        选择状态改变时发出 checkedChanged(isChecked: bool) 信号
        
        HyperlinkCard()
        超链接设置卡，点击右侧按钮时可自动跳转到指定 URL
        
        PushSettingCard()
        按钮设置卡，点击右侧按钮时会发送 clicked() 信号
        
        PrimaryPushSettingCard()
        主题色按钮设置卡，点击右侧按钮时会发送 clicked() 信号
        
        ExpandGroupSettingCard()
        手风琴设置组卡片，可添加多组配置项，每组用分隔符隔开
        调用 addGroupWidget(widget) 即可添加一组配置项到卡片中
        
        SettingCardGroup()
        可以通过 SettingCardGroup.addSettingCard() 将多个设置卡添加到同一个组中
        SettingCardGroup 会根据设置卡的高度自动调整自己的布局
        '''

        '''设置卡'''
        sc = SettingCard(FluentIcon.SETTING, "我是设置卡", '设置音量', self)
        # setButton = TransparentToolButton("Button")
        # sc.hBoxLayout.addLayout(setButton)

        '''下拉选择卡'''
        cfg = OptionsConfigItem(
            "MainWindow",
            "DpiScale",
            "Auto",
            OptionsValidator([1, 1.25, 1.5]), # 对应 texts
            restart=True
        )
        # 连接信号插槽
        cfg.valueChanged.connect(lambda t: print(t))
        lc = ComboBoxSettingCard(
            cfg,
            FluentIcon.ZOOM,
            "Title",
            "Content",
            ['100', '200', '300']
        )

        '''选项设置卡'''
        osc = OptionsSettingCard(
            qconfig.themeMode,
            FluentIcon.BRUSH,
            "应用主题",
            '调整你的应用外观',
            ["浅色", '深色', '跟随系统']
        )
        # 连接信号插槽
        osc.optionChanged.connect(
            lambda t: setTheme(t.value)
        )

        '''文件夹卡片'''
        fcfg = ConfigItem(
            "文件夹",
            '路径',
            r"C:\Program Files (x86)",
            FolderListValidator()
        )
        fcd = FolderListSettingCard(
            fcfg,
            "本地路径",
            "目录",
        )
        # 连接信号插槽
        fcd.folderChanged.connect(lambda path: print(path))

        '''范围设置卡'''
        rgi = RangeConfigItem(
            'Range',
            "音量",
            30,
            RangeValidator(0, 100)
        )
        rsd = RangeSettingCard(
            rgi,
            FluentIcon.MUSIC,
            "设置音量",
            '设置当前电脑音量'
        )
        # 连接信号插槽
        rsd.valueChanged.connect(
            lambda value: print(value)
        )

        '''开关设置卡'''
        scfg = ConfigItem(
            "Switch",
            "开关",
            False,
            BoolValidator()
        )
        swcd = SwitchSettingCard(
            FluentIcon.AIRPLANE,
            "飞机模式",
            "是否打开飞机模式",
            scfg
        )

        # 连接信号插槽
        swcd.checkedChanged.connect(
            lambda value: print(value)
        )

        '''超链接设置卡'''
        lkc = HyperlinkCard(
            "https://www.baidu.com",
            "百度",
            FluentIcon.LINK,
            "百度",
            '点击跳转到百度'
        )

        '''按钮设置卡'''
        btc = PushSettingCard(
            "选则目录",
            FluentIcon.DOWNLOAD,
            "下载目录",
            "C:/Users/Downloads"
        )
        # 连接信号插槽
        btc.clicked.connect(lambda :print(True))

        '''主题色按钮设置卡'''
        tcd = PrimaryPushSettingCard(
            "检查更新",
            FluentIcon.INFO,
            "关于",
            "当前版本24H2"
        )
        # 连接信号插槽
        tcd.clicked.connect(
            lambda: print(True)
        )

        '''手风琴设置组卡片 可添加多组配置项'''
        efsc = ExpandGroupSettingCard(
            FluentIcon.SPEED_OFF,
            "节点模式",
            "调整电池模式",
        )
        tcdTS = PrimaryPushSettingCard(
            "检查更新",
            FluentIcon.INFO,
            "关于",
            "当前版本24H2"
        )
        # 添加到布局
        efsc.addGroupWidget(tcdTS)

        ts = AcrylicComboBoxSettingCard(
            OptionsConfigItem("ts",' ts', '是', OptionsValidator(['1', '2'])),
            FluentIcon.INFO,
            "Titl",
            'Content',
            texts=['1', '2']
        )

        # 设置内容边距 setContentsMargins
        '''设置组'''
        sg = SettingCardGroup("Settings")
        sg.addSettingCard(sc)
        sg.addSettingCard(lc)
        sg.addSettingCard(osc)
        sg.addSettingCard(fcd)
        sg.addSettingCard(rsd)
        sg.addSettingCard(swcd)
        sg.addSettingCard(lkc)
        sg.addSettingCard(btc)
        sg.addSettingCard(tcd)
        sg.addSettingCard(efsc)
        sg.addSettingCard(ts)


        self.layout.addWidget(sg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
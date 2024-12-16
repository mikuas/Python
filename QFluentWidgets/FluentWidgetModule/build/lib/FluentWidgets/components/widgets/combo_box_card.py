# coding:utf-8
from typing import Union

from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget
from qfluentwidgets import ComboBox, EditableComboBox, OptionsConfigItem, OptionsValidator, OptionsSettingCard, \
    ConfigItem, FluentIconBase, FolderListValidator

from .custom_card import CardBase
from .folder_card import FolderListSettingCard


class ComboBoxCardBase(CardBase):
    # noinspection PyUnusedLocal
    def __init__(self, icon, title, content, parent=None, noSelected=False, items: list[str] = None, info: str = None):
        super().__init__()
        self.comboBoxButton = None
        self.noSelected = noSelected
        self.initIcon(icon).initTitle(title).initContent(content).initLayout()

    def initComboBox(self, items):
        self.comboBoxButton.addItems(items)
        self.comboBoxButton.setMinimumWidth(160)
        self.hBoxLayout.addWidget(self.comboBoxButton, 0, Qt.AlignmentFlag.AlignRight)
        return self

    def setPlaceholderText(self, text: str):
        if self.isNoSelected():
            self.comboBoxButton.setPlaceholderText(text)
            self.comboBoxButton.setCurrentIndex(-1)
        return self

    def isNoSelected(self):
        return self.noSelected


class ComboBoxCard(ComboBoxCardBase):
    """ 下拉框卡片 """
    def __init__(self, icon, title, content, items, noSelected=False, info=None, parent=None):
        super().__init__(icon, title, content, parent, noSelected)
        self.comboBoxButton = ComboBox(self)
        self.initComboBox(items).setPlaceholderText(info)


class EditComboBoxCard(ComboBoxCardBase):
    """ 可编辑下拉框卡片 """
    def __init__(self, icon, title, content, items, noSelected=None, info=None, parent=None):
        super().__init__(icon, title, content, parent, noSelected)
        self.comboBoxButton = EditableComboBox(self)
        self.initComboBox(items).setPlaceholderText(info)


class OptionsCardBase(OptionsSettingCard):
    # noinspection PyUnusedLocal
    def __init__(
            self,
            icon: Union[QIcon, str, FluentIconBase] = None,
            title: str = None,
            content: str = None,
            items: list[str] = None,
            defaultValue: str = None,
            parent: QWidget = None
    ):
        super().__init__(
            OptionsConfigItem('options', 'option', defaultValue, OptionsValidator(items)),
            icon, title, content, items, parent
        )

    def setOptionsFixedHeight(self, height):
        self.card.setFixedHeight(height)
        self.setFixedHeight(self.card.height())
        self.setViewportMargins(0, self.card.height(), 0, 0)
        return self

    def setIconSize(self, width, height):
        self.card.setIconSize(width, height)
        return self


class OptionsCard(OptionsCardBase):
    """ options card """
    def __init__(self, icon, title, content, items, defaultValue, parent=None):
        super().__init__(icon, title, content, items, defaultValue, parent)
        self.setOptionsFixedHeight(70).setIconSize(24, 24)


class FolderListCard(FolderListSettingCard):
    """ folder list card """
    def __init__(self, title, content, defaultPath: str, parent=None):
        super().__init__(
            ConfigItem('folders', 'folder', defaultPath, FolderListValidator()),
            title, content, './', parent
        )
        self.setCardFixedHeight(70).setIconSize(24, 24)

    def setCardFixedHeight(self, height):
        self.card.setFixedHeight(height)
        self.setFixedHeight(self.card.height())
        self.setViewportMargins(0, self.card.height(), 0, 0)
        return self

    def setIconSize(self, width, height):
        self.card.setIconSize(width, height)
        return self

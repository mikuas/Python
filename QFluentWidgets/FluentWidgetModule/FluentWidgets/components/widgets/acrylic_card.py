# coding:utf-8
from qfluentwidgets.components.material import AcrylicComboBox, AcrylicEditableComboBox

from .combo_box_card import ComboBoxCardBase


class AcrylicComboBoxCard(ComboBoxCardBase):
    """ 亚力克下拉框卡片 """
    def __init__(self, icon, title, content, items, noSelected=None, info=None, parent=None):
        super().__init__(icon, title, content, parent, noSelected)
        self.comboBoxButton = AcrylicComboBox(self)
        self.initComboBox(items).setPlaceholderText(info)


class AcrylicEditComboBoxCard(ComboBoxCardBase):
    """ 亚力克可编辑下拉框卡片 """
    def __init__(self, icon, title, content, items, noSelected=None, info=None, parent=None):
        super().__init__(icon, title, content, parent, noSelected)
        self.comboBoxButton = AcrylicEditableComboBox(self)
        self.initComboBox(items).setPlaceholderText(info)
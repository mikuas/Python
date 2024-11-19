from PySide6.QtGui import Qt
from qfluentwidgets import ComboBox, EditableComboBox, OptionsConfigItem, OptionsValidator, OptionsSettingCard, \
    ConfigItem

from ...widgetdoc import CustomComboBoxCard, CustomOptionsCard
from ...customwidgets import FolderListSettingCard
from ..cards import CustomCard


class CustomOptionsCard(CustomOptionsCard):

    def setOptionsFixedHeight(self, height, parent):
        parent.card.setFixedHeight(height)
        parent.setFixedHeight(parent.card.height())
        parent.setViewportMargins(0, parent.card.height(), 0, 0)
        return self


# 下拉框
class ComboBoxCard(CustomComboBoxCard, CustomCard):
    """ 下拉框卡片 """
    def __init__(self, icon, title, content, items, noSelected=False, info=None, parent=None, boxType=ComboBox):
        CustomCard.__init__(self, parent)
        self.noSelected = noSelected
        self.initIcon(icon).initTitle(title).initContent(content).initLayout()
        self.initComboBox(boxType, items).setPlaceholderText(info)

    def initComboBox(self, boxType, items):
        self.comboBox = boxType(self)
        self.comboBox.addItems(items)
        self.comboBox.setFixedWidth(150)
        self.hBoxLayout.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignRight)
        return self

    def setPlaceholderText(self, text: str):
        if self.isNoSelected():
            self.comboBox.setPlaceholderText(text)
            self.comboBox.setCurrentIndex(-1)
        return self

    def isNoSelected(self):
        return self.noSelected


class EditComboBoxCard(ComboBoxCard):
    """ 可编辑下拉框卡片 """
    def __init__(self, icon, title, content, items, noSelected=None, info=None, parent=None):
        super().__init__(icon, title, content, items, noSelected, info, parent, EditableComboBox)


# 选项卡
class OptionsCard(CustomOptionsCard, OptionsSettingCard):
    """ 选项卡 """
    def __init__(self, icon, title, content, items, defaultValue, parent=None):
        OptionsSettingCard.__init__(self, self.__initOptItems(defaultValue, items), icon, title, content, items, parent)
        self.setOptionsFixedHeight(80, self)

    @staticmethod
    def __initOptItems(value, items):
        return OptionsConfigItem('options', 'option', value, OptionsValidator(items))


class FolderListCard(CustomOptionsCard, FolderListSettingCard):
    def __init__(self, title, content, defaultValue, parent=None):
        FolderListSettingCard.__init__(self, self.__initConfItems(defaultValue), title, content, parent=parent)
        self.setOptionsFixedHeight(80, self)

    def __initConfItems(self, defaultValue: str):
        from qfluentwidgets import FolderListValidator
        return ConfigItem('folders', 'folder', defaultValue, FolderListValidator())



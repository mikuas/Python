from qfluentwidgets.components.material import AcrylicComboBox, AcrylicEditableComboBox

from FluentCardWidget.ComboBoxCard import ComboBoxCard

class AcrylicComboBoxCard(ComboBoxCard):
    """ 亚力克下拉框卡片 """
    def __init__(self, icon, title, content, items, noSelected=None, info=None, parent=None):
        super().__init__(icon, title, content, items, noSelected, info, parent, AcrylicComboBox)


class AcrylicEditComboBoxCard(ComboBoxCard):
    """ 亚力克可编辑下拉框卡片 """
    def __init__(self, icon, title, content, items, noSelected=None, info=None, parent=None):
        super().__init__(icon, title, content, items, noSelected, info, parent, AcrylicEditableComboBox)
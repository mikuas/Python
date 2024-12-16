# coding:utf-8
from pathlib import Path
from typing import Union

from PySide6.QtCore import Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QFileDialog
from qfluentwidgets import ExpandSettingCard, ConfigItem, FluentIcon, PushButton, qconfig, FluentIconBase
from qfluentwidgets.components.settings.folder_list_setting_card import FolderItem

from .view_widget import Dialog


class FolderListSettingCard(ExpandSettingCard):
    """ Folder list setting card """

    folderChanged = Signal(list)

    def __init__(
            self,
            configItem: ConfigItem,
            title: str,
            content: str = None,
            directory="./",
            parent=None,
            icon: Union[str, QIcon, FluentIconBase] = FluentIcon.FOLDER,
            btIcon: Union[str, QIcon, FluentIconBase] = FluentIcon.FOLDER_ADD
    ):
        super().__init__(icon, title, content, parent)
        self.configItem = configItem
        self._dialogDirectory = directory
        self.addFolderButton = PushButton(self.tr('添加文件夹'), self, btIcon)

        self.folders = qconfig.get(configItem).copy()
        self.__initWidget()

    def __initWidget(self):
        self.addWidget(self.addFolderButton)

        # initialize layout
        self.viewLayout.setSpacing(0)
        self.viewLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.viewLayout.setContentsMargins(0, 0, 0, 0)
        for folder in self.folders:
            self.__addFolderItem(folder)

        self.addFolderButton.clicked.connect(self.__showFolderDialog)

    def __showFolderDialog(self):
        """ show folder dialog """
        folder = QFileDialog.getExistingDirectory(
            self, self.tr("选择文件夹"), self._dialogDirectory
        )

        if not folder or folder in self.folders:
            return

        self.__addFolderItem(folder)
        self.folders.append(folder)
        qconfig.set(self.configItem, self.folders)
        self.folderChanged.emit(self.folders)

    def __addFolderItem(self, folder: str):
        """ add folder item """
        item = FolderItem(folder, self.view)
        item.removed.connect(self.__showConfirmDialog)
        self.viewLayout.addWidget(item)
        item.show()
        self._adjustViewSize()

    def __showConfirmDialog(self, item: FolderItem):
        """ show confirm dialog """
        title = self.tr('是否确实要删除该文件夹?')
        content = self.tr(f"如果删除, {Path(item.folder).name}文件夹将从其列表中删除，则该文件夹将不会出现在列表中")
        w = Dialog(title, content, self.window())
        w.yesSignal.connect(lambda: self.__removeFolder(item))
        w.exec()

    def __removeFolder(self, item: FolderItem):
        """ remove folder """
        if item.folder not in self.folders:
            return

        self.folders.remove(item.folder)
        self.viewLayout.removeWidget(item)
        item.deleteLater()
        self._adjustViewSize()

        self.folderChanged.emit(self.folders)
        qconfig.set(self.configItem, self.folders)
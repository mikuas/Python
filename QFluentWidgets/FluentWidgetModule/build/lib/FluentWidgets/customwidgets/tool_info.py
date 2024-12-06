from PySide6.QtWidgets import QWidget
from qfluentwidgets import ToolTipFilter, ToolTipPosition


def setToolTipInfo(widget: QWidget, info: str, time: int):
    """ 设置工具提示信息 """
    widget.setToolTip(info)
    widget.setToolTipDuration(time)
    widget.installEventFilter(ToolTipFilter(widget, 300, ToolTipPosition.TOP))

def setToolTipInfos(widgets: list[QWidget], infos: list[str], time: list[int] | int):
    """ 设置多个工具提示信息 """
    time = [time for _ in range(len(widgets))] if type(time) is int else time
    for widget, info, time in zip(widgets, infos, time):
        setToolTipInfo(widget, info, time)





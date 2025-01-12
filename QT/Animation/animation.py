# coding:utf-8
from typing import Union

from PySide6.QtCore import (
    QPropertyAnimation, QRect, QPoint, QSize, QParallelAnimationGroup, QSequentialAnimationGroup, QEasingCurve
)
from PySide6.QtWidgets import QWidget, QGraphicsOpacityEffect


class Animation:
    def __init__(
            self,
            target: QWidget,
            aniType,
            duration: int,
            startValue,
            endValue,
            easing=QEasingCurve.Type.Linear,
            finished=None
    ):
        self.__animation = QPropertyAnimation(target, aniType)
        self.__animation.setDuration(duration)
        self.__animation.setStartValue(startValue)
        self.__animation.setEndValue(endValue)
        if easing:
            self.__animation.setEasingCurve(easing)
        self.__animation.finished.connect(finished or self.__animation.deleteLater)

    def _getAni(self):
        return self.__animation

    @classmethod
    def createAni(
            cls,
            target: QWidget,
            aniType,
            duration: int,
            startValue,
            endValue,
            easing=QEasingCurve.Type.Linear,
            finished=None
    ):
        return Animation(target, aniType, duration, startValue, endValue, easing, finished)._getAni()

    @classmethod
    def posAni(
            cls,
            target: QWidget,
            duration: int,
            startValue: QPoint,
            endValue: QPoint,
            easing=QEasingCurve.Type.Linear,
            finished=None
    ):
        return cls.createAni(target, b"pos", duration, startValue, endValue, easing, finished)

    @classmethod
    def geometryAni(
            cls,
            target: QWidget,
            duration: int,
            startValue: Union[QRect, QPoint, QSize],
            endValue: Union[QRect, QPoint, QSize],
            easing=QEasingCurve.Type.Linear,
            finished=None
    ):
        return cls.createAni(target, b"geometry", duration, startValue, endValue, easing, finished)

    @classmethod
    def sizeAni(
            cls,
            target: QWidget,
            duration: int,
            startValue: QSize,
            endValue: QSize,
            easing=QEasingCurve.Type.Linear,
            finished=None
    ):
        return cls.createAni(target, b"size", duration, startValue, endValue, easing, finished)

    @classmethod
    def opacityAni(
            cls,
            target: QWidget,
            duration: int,
            startValue: float,
            endValue: float,
            defaultOpacity=1,
            easing=QEasingCurve.Type.Linear,
            finished=None
    ):
        cls.opacityEffect = QGraphicsOpacityEffect(target)
        target.setGraphicsEffect(cls.opacityEffect)
        cls.opacityEffect.setOpacity(defaultOpacity)
        return cls.createAni(cls.opacityEffect, b"opacity", duration, startValue, endValue, easing, finished)


class AnimationGroupBase:
    def __init__(self, parent: QWidget = None):
        self.__animations = []
        self.__animationGroup = None

    def addAni(self, ani: Animation):
        self.__animationGroup.append(ani)

    def removeAni(self, ani: Animation):
        self.__animationGroup.remove(ani)

    def _setGroupAni(self, obj):
        self.__animationGroup = obj

    def start(self):
        self.__animationGroup.start()

    def finish(self, function):
        self.__animationGroup.finished.connect(function)


class ParallelAnimation(AnimationGroupBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setGroupAni(QParallelAnimationGroup(parent))


class SequentialAnimation(AnimationGroupBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setGroupAni(QSequentialAnimationGroup(parent))
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPlainTextEdit, QPushButton, QSizePolicy,
                               QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(866, 567)
        font = QFont()
        font.setPointSize(5)
        font.setStyleStrategy(QFont.NoAntialias)
        Form.setFont(font)
        Form.setCursor(QCursor(Qt.CrossCursor))
        Form.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        Form.setToolTipDuration(-14)
        self.text_one = QPlainTextEdit(Form)
        self.text_one.setObjectName(u"text_one")
        self.text_one.setGeometry(QRect(20, 20, 831, 461))
        self.button_one = QPushButton(Form)
        self.button_one.setObjectName(u"button_one")
        self.button_one.setGeometry(QRect(340, 490, 141, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_one.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

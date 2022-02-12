# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'non_ascii_names_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NonAsciiNamesDialog(object):
    def setupUi(self, NonAsciiNamesDialog):
        if not NonAsciiNamesDialog.objectName():
            NonAsciiNamesDialog.setObjectName(u"NonAsciiNamesDialog")
        NonAsciiNamesDialog.setWindowModality(Qt.NonModal)
        NonAsciiNamesDialog.resize(520, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NonAsciiNamesDialog.sizePolicy().hasHeightForWidth())
        NonAsciiNamesDialog.setSizePolicy(sizePolicy)
        NonAsciiNamesDialog.setMinimumSize(QSize(520, 280))
        NonAsciiNamesDialog.setMaximumSize(QSize(520, 280))
        NonAsciiNamesDialog.setStyleSheet(u"QFrame{border: 2px outset black;}\n"
"\n"
"QLabel\n"
"{\n"
"border: 0px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(NonAsciiNamesDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(NonAsciiNamesDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(4)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_text = QLabel(self.frame)
        self.label_text.setObjectName(u"label_text")
        font = QFont()
        font.setPointSize(18)
        self.label_text.setFont(font)
        self.label_text.setLineWidth(1)
        self.label_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_text)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 15, 15)
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_ok = QPushButton(self.frame)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_ok)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(NonAsciiNamesDialog)

        QMetaObject.connectSlotsByName(NonAsciiNamesDialog)
    # setupUi

    def retranslateUi(self, NonAsciiNamesDialog):
        NonAsciiNamesDialog.setWindowTitle("")
        self.label_text.setText(QCoreApplication.translate("NonAsciiNamesDialog", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">Achtung</span><br/><br/>Die Namen in der Config enthalten<br/>nicht erlaubte Zeichen.</p><p align=\"center\">Erlaubt sind: A-Z, 0-9, -, ' und Leerzeichen.</p></body></html>", None))
        self.pushButton_ok.setText(QCoreApplication.translate("NonAsciiNamesDialog", u"Ok", None))
    # retranslateUi


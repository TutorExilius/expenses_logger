# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_back_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InputBackDialog(object):
    def setupUi(self, InputBackDialog):
        if not InputBackDialog.objectName():
            InputBackDialog.setObjectName(u"InputBackDialog")
        InputBackDialog.setWindowModality(Qt.NonModal)
        InputBackDialog.resize(470, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InputBackDialog.sizePolicy().hasHeightForWidth())
        InputBackDialog.setSizePolicy(sizePolicy)
        InputBackDialog.setMinimumSize(QSize(470, 200))
        InputBackDialog.setMaximumSize(QSize(470, 200))
        InputBackDialog.setStyleSheet(u"QFrame{border: 2px outset black;}\n"
"\n"
"QLabel\n"
"{\n"
"border: 0px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(InputBackDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(InputBackDialog)
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

        self.pushButton_yes = QPushButton(self.frame)
        self.pushButton_yes.setObjectName(u"pushButton_yes")
        self.pushButton_yes.setFont(font)
        self.pushButton_yes.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_yes)

        self.horizontalSpacer_2 = QSpacerItem(15, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_no = QPushButton(self.frame)
        self.pushButton_no.setObjectName(u"pushButton_no")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton_no.setFont(font1)
        self.pushButton_no.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_no)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(InputBackDialog)

        QMetaObject.connectSlotsByName(InputBackDialog)
    # setupUi

    def retranslateUi(self, InputBackDialog):
        InputBackDialog.setWindowTitle("")
        self.label_text.setText(QCoreApplication.translate("InputBackDialog", u"<html><head/><body><p>Deine Eingaben werden verworfen.<br/>Willst du wirklich abbrechen?</p></body></html>", None))
        self.pushButton_yes.setText(QCoreApplication.translate("InputBackDialog", u"Ja", None))
        self.pushButton_no.setText(QCoreApplication.translate("InputBackDialog", u"Nein", None))
    # retranslateUi


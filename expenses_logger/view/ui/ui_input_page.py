# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InputPage(object):
    def setupUi(self, InputPage):
        if not InputPage.objectName():
            InputPage.setObjectName(u"InputPage")
        InputPage.resize(661, 526)
        InputPage.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(InputPage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_back = QPushButton(InputPage)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setMinimumSize(QSize(122, 0))
        self.pushButton_back.setMaximumSize(QSize(122, 16777215))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_5.addWidget(self.pushButton_back)

        self.horizontalSpacer = QSpacerItem(35, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_name = QLabel(InputPage)
        self.label_name.setObjectName(u"label_name")
        font1 = QFont()
        font1.setPointSize(18)
        self.label_name.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_name)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_inputs = QLabel(InputPage)
        self.label_inputs.setObjectName(u"label_inputs")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_inputs.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_inputs)

        self.listWidget_inputs = QListWidget(InputPage)
        self.listWidget_inputs.setObjectName(u"listWidget_inputs")
        self.listWidget_inputs.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_inputs.sizePolicy().hasHeightForWidth())
        self.listWidget_inputs.setSizePolicy(sizePolicy)
        self.listWidget_inputs.setMinimumSize(QSize(0, 141))
        self.listWidget_inputs.setMaximumSize(QSize(130, 141))
        self.listWidget_inputs.setFont(font1)
        self.listWidget_inputs.setFocusPolicy(Qt.NoFocus)
        self.listWidget_inputs.setStyleSheet(u"QListWidget:item\n"
"{\n"
"padding: 0px 6px;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"width: 25px;\n"
"}")
        self.listWidget_inputs.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_4.addWidget(self.listWidget_inputs)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.pushButton_remove_selected_items = QPushButton(InputPage)
        self.pushButton_remove_selected_items.setObjectName(u"pushButton_remove_selected_items")
        self.pushButton_remove_selected_items.setEnabled(False)
        self.pushButton_remove_selected_items.setMinimumSize(QSize(40, 40))
        self.pushButton_remove_selected_items.setMaximumSize(QSize(40, 40))
        self.pushButton_remove_selected_items.setFont(font2)
        self.pushButton_remove_selected_items.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_remove_selected_items)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_total_title = QLabel(InputPage)
        self.label_total_title.setObjectName(u"label_total_title")
        self.label_total_title.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_total_title)

        self.label_total_amount = QLabel(InputPage)
        self.label_total_amount.setObjectName(u"label_total_amount")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_total_amount.setFont(font3)
        self.label_total_amount.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_total_amount)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_amount_input = QLabel(InputPage)
        self.label_amount_input.setObjectName(u"label_amount_input")
        self.label_amount_input.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_amount_input)

        self.lineEdit_input = QLineEdit(InputPage)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setFocusPolicy(Qt.NoFocus)
        self.lineEdit_input.setAlignment(Qt.AlignCenter)
        self.lineEdit_input.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.lineEdit_input)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_7 = QPushButton(InputPage)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(50, 50))
        self.pushButton_7.setMaximumSize(QSize(50, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setFocusPolicy(Qt.NoFocus)
        self.pushButton_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(InputPage)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 50))
        self.pushButton_4.setMaximumSize(QSize(50, 50))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(InputPage)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(50, 50))
        self.pushButton_6.setMaximumSize(QSize(50, 50))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(InputPage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setMaximumSize(QSize(50, 50))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(InputPage)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(50, 50))
        self.pushButton_9.setMaximumSize(QSize(50, 50))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_9, 0, 2, 1, 1)

        self.pushButton_5 = QPushButton(InputPage)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(50, 50))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_clear = QPushButton(InputPage)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(80, 50))
        self.pushButton_clear.setMaximumSize(QSize(80, 50))
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_clear, 0, 4, 1, 1)

        self.pushButton_8 = QPushButton(InputPage)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(50, 50))
        self.pushButton_8.setMaximumSize(QSize(50, 50))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_0 = QPushButton(InputPage)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(50, 50))
        self.pushButton_0.setMaximumSize(QSize(50, 50))
        self.pushButton_0.setFont(font)
        self.pushButton_0.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_0, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(InputPage)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setMaximumSize(QSize(50, 50))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.pushButton_comma = QPushButton(InputPage)
        self.pushButton_comma.setObjectName(u"pushButton_comma")
        self.pushButton_comma.setMinimumSize(QSize(50, 50))
        self.pushButton_comma.setMaximumSize(QSize(50, 50))
        self.pushButton_comma.setFont(font)
        self.pushButton_comma.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_comma, 3, 1, 1, 1)

        self.pushButton_del = QPushButton(InputPage)
        self.pushButton_del.setObjectName(u"pushButton_del")
        self.pushButton_del.setEnabled(False)
        self.pushButton_del.setMinimumSize(QSize(50, 50))
        self.pushButton_del.setMaximumSize(QSize(50, 50))
        self.pushButton_del.setFont(font)
        self.pushButton_del.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_del, 3, 2, 1, 1)

        self.pushButton_add = QPushButton(InputPage)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setEnabled(False)
        self.pushButton_add.setMinimumSize(QSize(80, 50))
        self.pushButton_add.setMaximumSize(QSize(80, 50))
        self.pushButton_add.setFont(font1)
        self.pushButton_add.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_add, 3, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.pushButton_1 = QPushButton(InputPage)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(50, 50))
        self.pushButton_1.setMaximumSize(QSize(50, 50))
        self.pushButton_1.setFont(font)
        self.pushButton_1.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.pushButton_save_back = QPushButton(InputPage)
        self.pushButton_save_back.setObjectName(u"pushButton_save_back")
        self.pushButton_save_back.setEnabled(False)
        self.pushButton_save_back.setMinimumSize(QSize(237, 40))
        self.pushButton_save_back.setMaximumSize(QSize(237, 40))
        self.pushButton_save_back.setFont(font3)
        self.pushButton_save_back.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_6.addWidget(self.pushButton_save_back)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(InputPage)

        QMetaObject.connectSlotsByName(InputPage)
    # setupUi

    def retranslateUi(self, InputPage):
        InputPage.setWindowTitle(QCoreApplication.translate("InputPage", u"WizardPage", None))
        self.pushButton_back.setText(QCoreApplication.translate("InputPage", u"\u2190 zur\u00fcck", None))
        self.label_name.setText(QCoreApplication.translate("InputPage", u"Name", None))
        self.label_inputs.setText(QCoreApplication.translate("InputPage", u"Eingaben:", None))
        self.pushButton_remove_selected_items.setText(QCoreApplication.translate("InputPage", u"Del", None))
        self.label_total_title.setText(QCoreApplication.translate("InputPage", u"Gesamt:", None))
        self.label_total_amount.setText(QCoreApplication.translate("InputPage", u"0,00 \u20ac", None))
        self.label_amount_input.setText(QCoreApplication.translate("InputPage", u"Betrag", None))
        self.lineEdit_input.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("InputPage", u"7", None))
        self.pushButton_4.setText(QCoreApplication.translate("InputPage", u"4", None))
        self.pushButton_6.setText(QCoreApplication.translate("InputPage", u"6", None))
        self.pushButton_2.setText(QCoreApplication.translate("InputPage", u"2", None))
        self.pushButton_9.setText(QCoreApplication.translate("InputPage", u"9", None))
        self.pushButton_5.setText(QCoreApplication.translate("InputPage", u"5", None))
        self.pushButton_clear.setText(QCoreApplication.translate("InputPage", u"Clear", None))
        self.pushButton_8.setText(QCoreApplication.translate("InputPage", u"8", None))
        self.pushButton_0.setText(QCoreApplication.translate("InputPage", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("InputPage", u"3", None))
        self.pushButton_comma.setText(QCoreApplication.translate("InputPage", u",", None))
        self.pushButton_del.setText(QCoreApplication.translate("InputPage", u"\u2190", None))
        self.pushButton_add.setText(QCoreApplication.translate("InputPage", u"Add", None))
        self.pushButton_1.setText(QCoreApplication.translate("InputPage", u"1", None))
        self.pushButton_save_back.setText(QCoreApplication.translate("InputPage", u"speichern && zur\u00fcck", None))
    # retranslateUi


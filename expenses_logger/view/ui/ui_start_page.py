# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartPage(object):
    def setupUi(self, StartPage):
        if not StartPage.objectName():
            StartPage.setObjectName(u"StartPage")
        StartPage.resize(816, 598)
        StartPage.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(StartPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(StartPage)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(17)
        font.setUnderline(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"text-decoration: underline;")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label_year = QLabel(StartPage)
        self.label_year.setObjectName(u"label_year")
        font1 = QFont()
        font1.setPointSize(19)
        self.label_year.setFont(font1)
        self.label_year.setStyleSheet(u"")
        self.label_year.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_year)

        self.verticalSpacer = QSpacerItem(0, 9, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame = QFrame(StartPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_letters = QFrame(self.frame)
        self.frame_letters.setObjectName(u"frame_letters")
        self.frame_letters.setFrameShape(QFrame.StyledPanel)
        self.frame_letters.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_letters)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_input_A = QPushButton(self.frame_letters)
        self.pushButton_input_A.setObjectName(u"pushButton_input_A")
        self.pushButton_input_A.setMinimumSize(QSize(40, 40))
        self.pushButton_input_A.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton_input_A.setFont(font2)
        self.pushButton_input_A.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_A)

        self.pushButton_input_B = QPushButton(self.frame_letters)
        self.pushButton_input_B.setObjectName(u"pushButton_input_B")
        self.pushButton_input_B.setMinimumSize(QSize(40, 40))
        self.pushButton_input_B.setMaximumSize(QSize(40, 40))
        self.pushButton_input_B.setFont(font2)
        self.pushButton_input_B.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_B)

        self.pushButton_input_C = QPushButton(self.frame_letters)
        self.pushButton_input_C.setObjectName(u"pushButton_input_C")
        self.pushButton_input_C.setMinimumSize(QSize(40, 40))
        self.pushButton_input_C.setMaximumSize(QSize(40, 40))
        self.pushButton_input_C.setFont(font2)
        self.pushButton_input_C.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_C)

        self.pushButton_input_D = QPushButton(self.frame_letters)
        self.pushButton_input_D.setObjectName(u"pushButton_input_D")
        self.pushButton_input_D.setMinimumSize(QSize(40, 40))
        self.pushButton_input_D.setMaximumSize(QSize(40, 40))
        self.pushButton_input_D.setFont(font2)
        self.pushButton_input_D.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_D)

        self.pushButton_input_E = QPushButton(self.frame_letters)
        self.pushButton_input_E.setObjectName(u"pushButton_input_E")
        self.pushButton_input_E.setMinimumSize(QSize(40, 40))
        self.pushButton_input_E.setMaximumSize(QSize(40, 40))
        self.pushButton_input_E.setFont(font2)
        self.pushButton_input_E.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_E)

        self.pushButton_input_F = QPushButton(self.frame_letters)
        self.pushButton_input_F.setObjectName(u"pushButton_input_F")
        self.pushButton_input_F.setMinimumSize(QSize(40, 40))
        self.pushButton_input_F.setMaximumSize(QSize(40, 40))
        self.pushButton_input_F.setFont(font2)
        self.pushButton_input_F.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_F)

        self.pushButton_input_G = QPushButton(self.frame_letters)
        self.pushButton_input_G.setObjectName(u"pushButton_input_G")
        self.pushButton_input_G.setMinimumSize(QSize(40, 40))
        self.pushButton_input_G.setMaximumSize(QSize(40, 40))
        self.pushButton_input_G.setFont(font2)
        self.pushButton_input_G.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_G)

        self.pushButton_input_H = QPushButton(self.frame_letters)
        self.pushButton_input_H.setObjectName(u"pushButton_input_H")
        self.pushButton_input_H.setMinimumSize(QSize(40, 40))
        self.pushButton_input_H.setMaximumSize(QSize(40, 40))
        self.pushButton_input_H.setFont(font2)
        self.pushButton_input_H.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_H)

        self.pushButton_input_I = QPushButton(self.frame_letters)
        self.pushButton_input_I.setObjectName(u"pushButton_input_I")
        self.pushButton_input_I.setMinimumSize(QSize(40, 40))
        self.pushButton_input_I.setMaximumSize(QSize(40, 40))
        self.pushButton_input_I.setFont(font2)
        self.pushButton_input_I.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_I)

        self.pushButton_input_J = QPushButton(self.frame_letters)
        self.pushButton_input_J.setObjectName(u"pushButton_input_J")
        self.pushButton_input_J.setMinimumSize(QSize(40, 40))
        self.pushButton_input_J.setMaximumSize(QSize(40, 40))
        self.pushButton_input_J.setFont(font2)
        self.pushButton_input_J.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_J)

        self.pushButton_input_K = QPushButton(self.frame_letters)
        self.pushButton_input_K.setObjectName(u"pushButton_input_K")
        self.pushButton_input_K.setMinimumSize(QSize(40, 40))
        self.pushButton_input_K.setMaximumSize(QSize(40, 40))
        self.pushButton_input_K.setFont(font2)
        self.pushButton_input_K.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_K)

        self.pushButton_input_L = QPushButton(self.frame_letters)
        self.pushButton_input_L.setObjectName(u"pushButton_input_L")
        self.pushButton_input_L.setMinimumSize(QSize(40, 40))
        self.pushButton_input_L.setMaximumSize(QSize(40, 40))
        self.pushButton_input_L.setFont(font2)
        self.pushButton_input_L.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_L)

        self.pushButton_input_M = QPushButton(self.frame_letters)
        self.pushButton_input_M.setObjectName(u"pushButton_input_M")
        self.pushButton_input_M.setMinimumSize(QSize(40, 40))
        self.pushButton_input_M.setMaximumSize(QSize(40, 40))
        self.pushButton_input_M.setFont(font2)
        self.pushButton_input_M.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.pushButton_input_M)

        self.horizontalSpacer_5 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButton_input_N = QPushButton(self.frame_letters)
        self.pushButton_input_N.setObjectName(u"pushButton_input_N")
        self.pushButton_input_N.setMinimumSize(QSize(40, 40))
        self.pushButton_input_N.setMaximumSize(QSize(40, 40))
        self.pushButton_input_N.setFont(font2)
        self.pushButton_input_N.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_N)

        self.pushButton_input_O = QPushButton(self.frame_letters)
        self.pushButton_input_O.setObjectName(u"pushButton_input_O")
        self.pushButton_input_O.setMinimumSize(QSize(40, 40))
        self.pushButton_input_O.setMaximumSize(QSize(40, 40))
        self.pushButton_input_O.setFont(font2)
        self.pushButton_input_O.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_O)

        self.pushButton_input_P = QPushButton(self.frame_letters)
        self.pushButton_input_P.setObjectName(u"pushButton_input_P")
        self.pushButton_input_P.setMinimumSize(QSize(40, 40))
        self.pushButton_input_P.setMaximumSize(QSize(40, 40))
        self.pushButton_input_P.setFont(font2)
        self.pushButton_input_P.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_P)

        self.pushButton_input_Q = QPushButton(self.frame_letters)
        self.pushButton_input_Q.setObjectName(u"pushButton_input_Q")
        self.pushButton_input_Q.setMinimumSize(QSize(40, 40))
        self.pushButton_input_Q.setMaximumSize(QSize(40, 40))
        self.pushButton_input_Q.setFont(font2)
        self.pushButton_input_Q.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_Q)

        self.pushButton_input_R = QPushButton(self.frame_letters)
        self.pushButton_input_R.setObjectName(u"pushButton_input_R")
        self.pushButton_input_R.setMinimumSize(QSize(40, 40))
        self.pushButton_input_R.setMaximumSize(QSize(40, 40))
        self.pushButton_input_R.setFont(font2)
        self.pushButton_input_R.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_R)

        self.pushButton_input_S = QPushButton(self.frame_letters)
        self.pushButton_input_S.setObjectName(u"pushButton_input_S")
        self.pushButton_input_S.setMinimumSize(QSize(40, 40))
        self.pushButton_input_S.setMaximumSize(QSize(40, 40))
        self.pushButton_input_S.setFont(font2)
        self.pushButton_input_S.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_S)

        self.pushButton_input_T = QPushButton(self.frame_letters)
        self.pushButton_input_T.setObjectName(u"pushButton_input_T")
        self.pushButton_input_T.setMinimumSize(QSize(40, 40))
        self.pushButton_input_T.setMaximumSize(QSize(40, 40))
        self.pushButton_input_T.setFont(font2)
        self.pushButton_input_T.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_T)

        self.pushButton_input_U = QPushButton(self.frame_letters)
        self.pushButton_input_U.setObjectName(u"pushButton_input_U")
        self.pushButton_input_U.setMinimumSize(QSize(40, 40))
        self.pushButton_input_U.setMaximumSize(QSize(40, 40))
        self.pushButton_input_U.setFont(font2)
        self.pushButton_input_U.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_U)

        self.pushButton_input_V = QPushButton(self.frame_letters)
        self.pushButton_input_V.setObjectName(u"pushButton_input_V")
        self.pushButton_input_V.setMinimumSize(QSize(40, 40))
        self.pushButton_input_V.setMaximumSize(QSize(40, 40))
        self.pushButton_input_V.setFont(font2)
        self.pushButton_input_V.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_V)

        self.pushButton_input_W = QPushButton(self.frame_letters)
        self.pushButton_input_W.setObjectName(u"pushButton_input_W")
        self.pushButton_input_W.setMinimumSize(QSize(40, 40))
        self.pushButton_input_W.setMaximumSize(QSize(40, 40))
        self.pushButton_input_W.setFont(font2)
        self.pushButton_input_W.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_W)

        self.pushButton_input_X = QPushButton(self.frame_letters)
        self.pushButton_input_X.setObjectName(u"pushButton_input_X")
        self.pushButton_input_X.setMinimumSize(QSize(40, 40))
        self.pushButton_input_X.setMaximumSize(QSize(40, 40))
        self.pushButton_input_X.setFont(font2)
        self.pushButton_input_X.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_X)

        self.pushButton_input_Y = QPushButton(self.frame_letters)
        self.pushButton_input_Y.setObjectName(u"pushButton_input_Y")
        self.pushButton_input_Y.setMinimumSize(QSize(40, 40))
        self.pushButton_input_Y.setMaximumSize(QSize(40, 40))
        self.pushButton_input_Y.setFont(font2)
        self.pushButton_input_Y.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_Y)

        self.pushButton_input_Z = QPushButton(self.frame_letters)
        self.pushButton_input_Z.setObjectName(u"pushButton_input_Z")
        self.pushButton_input_Z.setMinimumSize(QSize(40, 40))
        self.pushButton_input_Z.setMaximumSize(QSize(40, 40))
        self.pushButton_input_Z.setFont(font2)
        self.pushButton_input_Z.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_3.addWidget(self.pushButton_input_Z)

        self.horizontalSpacer_6 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addWidget(self.frame_letters)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.verticalSpacer_4 = QSpacerItem(0, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(450, 0))
        self.lineEdit.setMaximumSize(QSize(450, 30))
        self.lineEdit.setFont(font2)
        self.lineEdit.setFocusPolicy(Qt.NoFocus)
        self.lineEdit.setStyleSheet(u"color: red;")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.horizontalSpacer_9 = QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.pushButton_clear = QPushButton(self.frame)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setEnabled(False)
        self.pushButton_clear.setMinimumSize(QSize(75, 30))
        self.pushButton_clear.setMaximumSize(QSize(75, 40))
        font3 = QFont()
        font3.setPointSize(14)
        self.pushButton_clear.setFont(font3)
        self.pushButton_clear.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.pushButton_clear)

        self.horizontalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_5 = QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.listWidget = QListWidget(StartPage)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMinimumSize(QSize(533, 160))
        self.listWidget.setFont(font2)
        self.listWidget.setFocusPolicy(Qt.NoFocus)
        self.listWidget.setStyleSheet(u"QListWidget\n"
"{\n"
"padding: 5px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QListWidget:item\n"
"{\n"
"padding: 1px 8px;\n"
"background-color: #eaefff;\n"
"border: 1px outset black;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"width: 25px;\n"
"}")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget.setSpacing(6)

        self.verticalLayout_3.addWidget(self.listWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(0, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(4, 6)
        self.verticalLayout_2.setStretch(5, 2)
        QWidget.setTabOrder(self.pushButton_input_L, self.pushButton_input_M)
        QWidget.setTabOrder(self.pushButton_input_M, self.pushButton_input_N)
        QWidget.setTabOrder(self.pushButton_input_N, self.pushButton_input_O)
        QWidget.setTabOrder(self.pushButton_input_O, self.pushButton_input_P)
        QWidget.setTabOrder(self.pushButton_input_P, self.pushButton_input_Q)
        QWidget.setTabOrder(self.pushButton_input_Q, self.pushButton_input_R)
        QWidget.setTabOrder(self.pushButton_input_R, self.pushButton_input_S)
        QWidget.setTabOrder(self.pushButton_input_S, self.pushButton_input_T)
        QWidget.setTabOrder(self.pushButton_input_T, self.pushButton_input_U)
        QWidget.setTabOrder(self.pushButton_input_U, self.pushButton_input_V)
        QWidget.setTabOrder(self.pushButton_input_V, self.pushButton_input_W)
        QWidget.setTabOrder(self.pushButton_input_W, self.pushButton_input_X)
        QWidget.setTabOrder(self.pushButton_input_X, self.pushButton_input_Y)
        QWidget.setTabOrder(self.pushButton_input_Y, self.pushButton_input_Z)
        QWidget.setTabOrder(self.pushButton_input_Z, self.pushButton_clear)
        QWidget.setTabOrder(self.pushButton_clear, self.listWidget)

        self.retranslateUi(StartPage)

        QMetaObject.connectSlotsByName(StartPage)
    # setupUi

    def retranslateUi(self, StartPage):
        StartPage.setWindowTitle(QCoreApplication.translate("StartPage", u"WizardPage", None))
        self.label_title.setText(QCoreApplication.translate("StartPage", u"\u00dcbersicht Gesamtausgaben", None))
        self.label_year.setText(QCoreApplication.translate("StartPage", u"2022", None))
        self.pushButton_input_A.setText(QCoreApplication.translate("StartPage", u"A", None))
        self.pushButton_input_B.setText(QCoreApplication.translate("StartPage", u"B", None))
        self.pushButton_input_C.setText(QCoreApplication.translate("StartPage", u"C", None))
        self.pushButton_input_D.setText(QCoreApplication.translate("StartPage", u"D", None))
        self.pushButton_input_E.setText(QCoreApplication.translate("StartPage", u"E", None))
        self.pushButton_input_F.setText(QCoreApplication.translate("StartPage", u"F", None))
        self.pushButton_input_G.setText(QCoreApplication.translate("StartPage", u"G", None))
        self.pushButton_input_H.setText(QCoreApplication.translate("StartPage", u"H", None))
        self.pushButton_input_I.setText(QCoreApplication.translate("StartPage", u"I", None))
        self.pushButton_input_J.setText(QCoreApplication.translate("StartPage", u"J", None))
        self.pushButton_input_K.setText(QCoreApplication.translate("StartPage", u"K", None))
        self.pushButton_input_L.setText(QCoreApplication.translate("StartPage", u"L", None))
        self.pushButton_input_M.setText(QCoreApplication.translate("StartPage", u"M", None))
        self.pushButton_input_N.setText(QCoreApplication.translate("StartPage", u"N", None))
        self.pushButton_input_O.setText(QCoreApplication.translate("StartPage", u"O", None))
        self.pushButton_input_P.setText(QCoreApplication.translate("StartPage", u"P", None))
        self.pushButton_input_Q.setText(QCoreApplication.translate("StartPage", u"Q", None))
        self.pushButton_input_R.setText(QCoreApplication.translate("StartPage", u"R", None))
        self.pushButton_input_S.setText(QCoreApplication.translate("StartPage", u"S", None))
        self.pushButton_input_T.setText(QCoreApplication.translate("StartPage", u"T", None))
        self.pushButton_input_U.setText(QCoreApplication.translate("StartPage", u"U", None))
        self.pushButton_input_V.setText(QCoreApplication.translate("StartPage", u"V", None))
        self.pushButton_input_W.setText(QCoreApplication.translate("StartPage", u"W", None))
        self.pushButton_input_X.setText(QCoreApplication.translate("StartPage", u"X", None))
        self.pushButton_input_Y.setText(QCoreApplication.translate("StartPage", u"Y", None))
        self.pushButton_input_Z.setText(QCoreApplication.translate("StartPage", u"Z", None))
        self.lineEdit.setText("")
        self.pushButton_clear.setText(QCoreApplication.translate("StartPage", u"Clear", None))
    # retranslateUi


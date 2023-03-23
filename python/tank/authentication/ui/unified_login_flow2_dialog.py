# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unified_login_flow2_dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from .qt_abstraction import QtCore, QtGui

class Ui_UnifiedLoginFlow2Dialog(object):
    def setupUi(self, UnifiedLoginFlow2Dialog):
        UnifiedLoginFlow2Dialog.setObjectName("UnifiedLoginFlow2Dialog")
        UnifiedLoginFlow2Dialog.setWindowModality(QtCore.Qt.NonModal)
        UnifiedLoginFlow2Dialog.resize(364, 304)
        UnifiedLoginFlow2Dialog.setMinimumSize(QtCore.QSize(364, 296))
        UnifiedLoginFlow2Dialog.setStyleSheet("\n"
"QWidget\n"
"{\n"
"    background-color:  rgb(36, 39, 42);\n"
"    color: rgb(192, 192, 192);\n"
"    selection-background-color: rgb(168, 123, 43);\n"
"    selection-color: rgb(230, 230, 230);\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border-radius: 2px;\n"
"    padding: 8px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QLineEdit, QComboBox\n"
"{\n"
"    background-color: rgb(29, 31, 34);\n"
"    border: 1px solid rgb(54, 60, 66);\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"     font-size: 12px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    margin-left: 3;\n"
"    margin-right: 3\n"
"}\n"
"\n"
"QComboBox:focus, QLineEdit:focus\n"
"{\n"
"    border: 1px solid rgb(48, 167, 227);\n"
"}\n"
"\n"
"QComboBox:drop-down:button {\n"
"    border: 1px solid rgb(54, 60, 66);\n"
"}\n"
"\n"
"QComboBox:down-arrow {\n"
"    image: url(:/shotgun_authentication/down-arrow.png);\n"
"\n"
"}\n"
"\n"
"QLineEdit:Disabled {\n"
"    background-color: rgb(60, 60, 60);\n"
"    color: rgb(160, 160, 160);\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"    border-width: 0px;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(noimg); border-width: 0px;\n"
"}\n"
"\n"
"QComboBox::disabled {\n"
"    background-color: rgb(60, 60, 60);\n"
"    color: rgb(160, 160, 160);\n"
"}")
        UnifiedLoginFlow2Dialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(UnifiedLoginFlow2Dialog)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_spinner = QtGui.QLabel(UnifiedLoginFlow2Dialog)
        self.label_spinner.setText("")
        self.label_spinner.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_spinner.setObjectName("label_spinner")
        self.verticalLayout_2.addWidget(self.label_spinner)
        self.message = QtGui.QLabel(UnifiedLoginFlow2Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setText("")
        self.message.setWordWrap(True)
        self.message.setObjectName("message")
        self.verticalLayout_2.addWidget(self.message)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.cancel = QtGui.QPushButton(UnifiedLoginFlow2Dialog)
        self.cancel.setAutoDefault(False)
        self.cancel.setFlat(True)
        self.cancel.setObjectName("cancel")
        self.verticalLayout_2.addWidget(self.cancel)

        self.retranslateUi(UnifiedLoginFlow2Dialog)
        QtCore.QMetaObject.connectSlotsByName(UnifiedLoginFlow2Dialog)

    def retranslateUi(self, UnifiedLoginFlow2Dialog):
        self.cancel.setText(QtGui.QApplication.translate("UnifiedLoginFlow2Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc

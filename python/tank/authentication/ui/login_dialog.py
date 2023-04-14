# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from .qt_abstraction import QtCore, QtGui

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.setWindowModality(QtCore.Qt.NonModal)
        LoginDialog.resize(415, 419)
        LoginDialog.setMinimumSize(QtCore.QSize(364, 296))
        LoginDialog.setStyleSheet("\n"
"QWidget\n"
"{\n"
"    background-color: rgb(36, 39, 42);\n"
"    color: rgb(192, 192, 192);\n"
"    selection-background-color: rgb(168, 123, 43);\n"
"    selection-color: rgb(230, 230, 230);\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    padding: 8px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QPushButton::menu-indicator {\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"QPushButton QMenu::item {\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QLineEdit, QComboBox\n"
"{\n"
"    background-color: rgb(29, 31, 34);\n"
"    border: 1px solid rgb(54, 60, 66);\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    margin-left: 3px;\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"    border-color: rgb(48, 167, 227);\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgb(54, 60, 66);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    border-color: rgb(192, 192, 192);\n"
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
"}\n"
"\n"
"QLineEdit:Disabled {\n"
"    background-color: rgb(60, 60, 60);\n"
"    color: rgb(160, 160, 160);\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"    border-width: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(noimg); border-width: 0px;\n"
"}\n"
"\n"
"QComboBox::disabled {\n"
"    background-color: rgb(60, 60, 60);\n"
"    color: rgb(160, 160, 160);\n"
"}\n"
"\n"
"QPushButton.main\n"
"{\n"
"    background-color: rgb(35, 165, 225);\n"
"    border-color: rgb(36, 39, 42);\n"
"    color: rgb(248, 248, 248);\n"
"}\n"
"\n"
"QPushButton.main:focus, QPushButton.main:hover\n"
"{\n"
"    border-color: rgb(54, 60, 66);\n"
"}\n"
"\n"
"QPushButton.main:pressed\n"
"{\n"
"    border-color: rgb(248, 248, 248);\n"
"}\n"
"")
        LoginDialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(LoginDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stacked_main = QtGui.QStackedWidget(LoginDialog)
        self.stacked_main.setObjectName("stacked_main")
        self.main_page = QtGui.QWidget()
        self.main_page.setObjectName("main_page")
        self.verticalLayout_72 = QtGui.QVBoxLayout(self.main_page)
        self.verticalLayout_72.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = AspectPreservingLabel(self.main_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(250, 72))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/shotgun_authentication/shotgun_logo_light_medium.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.verticalLayout_72.addLayout(self.horizontalLayout)
        self.stackedWidget = QtGui.QStackedWidget(self.main_page)
        self.stackedWidget.setMinimumSize(QtCore.QSize(324, 172))
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtGui.QWidget()
        self.login_page.setObjectName("login_page")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.login_page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.credentials = QtGui.QWidget(self.login_page)
        self.credentials.setMinimumSize(QtCore.QSize(0, 126))
        self.credentials.setObjectName("credentials")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.credentials)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.site = RecentBox(self.credentials)
        self.site.setObjectName("site")
        self.verticalLayout_7.addWidget(self.site)
        self.login = RecentBox(self.credentials)
        self.login.setObjectName("login")
        self.verticalLayout_7.addWidget(self.login)
        self.password = Qt5LikeLineEdit(self.credentials)
        self.password.setMinimumSize(QtCore.QSize(308, 0))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_7.addWidget(self.password)
        self.message = QtGui.QLabel(self.credentials)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.message.setWordWrap(True)
        self.message.setMargin(4)
        self.message.setObjectName("message")
        self.verticalLayout_7.addWidget(self.message)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.credentials)
        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.setSpacing(10)
        self.button_layout.setContentsMargins(0, -1, -1, -1)
        self.button_layout.setObjectName("button_layout")
        self.links = QtGui.QVBoxLayout()
        self.links.setObjectName("links")
        self.forgot_password_link = QtGui.QLabel(self.login_page)
        self.forgot_password_link.setCursor(QtCore.Qt.PointingHandCursor)
        self.forgot_password_link.setTextFormat(QtCore.Qt.RichText)
        self.forgot_password_link.setMargin(4)
        self.forgot_password_link.setOpenExternalLinks(False)
        self.forgot_password_link.setObjectName("forgot_password_link")
        self.links.addWidget(self.forgot_password_link)
        self.button_layout.addLayout(self.links)
        self.button_options = QtGui.QPushButton(self.login_page)
        self.button_options.setAutoDefault(False)
        self.button_options.setFlat(True)
        self.button_options.setObjectName("button_options")
        self.button_layout.addWidget(self.button_options)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_layout.addItem(spacerItem1)
        self.cancel = QtGui.QPushButton(self.login_page)
        self.cancel.setAutoDefault(False)
        self.cancel.setFlat(True)
        self.cancel.setObjectName("cancel")
        self.button_layout.addWidget(self.cancel)
        self.sign_in = QtGui.QPushButton(self.login_page)
        self.sign_in.setAutoDefault(True)
        self.sign_in.setDefault(True)
        self.sign_in.setFlat(True)
        self.sign_in.setObjectName("sign_in")
        self.button_layout.addWidget(self.sign_in)
        self.button_layout.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.button_layout)
        self.stackedWidget.addWidget(self.login_page)
        self._2fa_page = QtGui.QWidget()
        self._2fa_page.setObjectName("_2fa_page")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self._2fa_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.credentials_2 = QtGui.QWidget(self._2fa_page)
        self.credentials_2.setMinimumSize(QtCore.QSize(0, 133))
        self.credentials_2.setObjectName("credentials_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.credentials_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.credentials_2)
        self.label.setMinimumSize(QtCore.QSize(86, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/google_authenticator/google_authenticator.png"))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.widget_2 = QtGui.QWidget(self.credentials_2)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self._2fa_message = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._2fa_message.sizePolicy().hasHeightForWidth())
        self._2fa_message.setSizePolicy(sizePolicy)
        self._2fa_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._2fa_message.setWordWrap(True)
        self._2fa_message.setMargin(0)
        self._2fa_message.setObjectName("_2fa_message")
        self.verticalLayout.addWidget(self._2fa_message)
        self._2fa_code = Qt5LikeLineEdit(self.widget_2)
        self._2fa_code.setObjectName("_2fa_code")
        self.verticalLayout.addWidget(self._2fa_code)
        self.invalid_code = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invalid_code.sizePolicy().hasHeightForWidth())
        self.invalid_code.setSizePolicy(sizePolicy)
        self.invalid_code.setText("")
        self.invalid_code.setObjectName("invalid_code")
        self.verticalLayout.addWidget(self.invalid_code)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_4.addWidget(self.credentials_2)
        self.button_layout_2 = QtGui.QHBoxLayout()
        self.button_layout_2.setSpacing(10)
        self.button_layout_2.setContentsMargins(0, -1, -1, -1)
        self.button_layout_2.setObjectName("button_layout_2")
        self.use_backup = QtGui.QPushButton(self._2fa_page)
        self.use_backup.setFlat(True)
        self.use_backup.setObjectName("use_backup")
        self.button_layout_2.addWidget(self.use_backup)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_layout_2.addItem(spacerItem3)
        self.cancel_tfa = QtGui.QPushButton(self._2fa_page)
        self.cancel_tfa.setAutoDefault(False)
        self.cancel_tfa.setFlat(True)
        self.cancel_tfa.setObjectName("cancel_tfa")
        self.button_layout_2.addWidget(self.cancel_tfa)
        self.verify_2fa = QtGui.QPushButton(self._2fa_page)
        self.verify_2fa.setMinimumSize(QtCore.QSize(65, 0))
        self.verify_2fa.setAutoDefault(False)
        self.verify_2fa.setDefault(True)
        self.verify_2fa.setFlat(True)
        self.verify_2fa.setObjectName("verify_2fa")
        self.button_layout_2.addWidget(self.verify_2fa)
        self.verticalLayout_4.addLayout(self.button_layout_2)
        self.stackedWidget.addWidget(self._2fa_page)
        self.backup_page = QtGui.QWidget()
        self.backup_page.setObjectName("backup_page")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.backup_page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.credentials_3 = QtGui.QWidget(self.backup_page)
        self.credentials_3.setMinimumSize(QtCore.QSize(0, 133))
        self.credentials_3.setObjectName("credentials_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.credentials_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.credentials_3)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/backup_codes/backup_codes_light_bg.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.widget_4 = QtGui.QWidget(self.credentials_3)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self._2fa_message_2 = QtGui.QLabel(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._2fa_message_2.sizePolicy().hasHeightForWidth())
        self._2fa_message_2.setSizePolicy(sizePolicy)
        self._2fa_message_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self._2fa_message_2.setWordWrap(True)
        self._2fa_message_2.setMargin(0)
        self._2fa_message_2.setObjectName("_2fa_message_2")
        self.verticalLayout_5.addWidget(self._2fa_message_2)
        self.backup_code = Qt5LikeLineEdit(self.widget_4)
        self.backup_code.setText("")
        self.backup_code.setObjectName("backup_code")
        self.verticalLayout_5.addWidget(self.backup_code)
        self.invalid_backup_code = QtGui.QLabel(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invalid_backup_code.sizePolicy().hasHeightForWidth())
        self.invalid_backup_code.setSizePolicy(sizePolicy)
        self.invalid_backup_code.setText("")
        self.invalid_backup_code.setObjectName("invalid_backup_code")
        self.verticalLayout_5.addWidget(self.invalid_backup_code)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.verticalLayout_6.addWidget(self.credentials_3)
        self.button_layout_3 = QtGui.QHBoxLayout()
        self.button_layout_3.setSpacing(10)
        self.button_layout_3.setContentsMargins(0, -1, -1, -1)
        self.button_layout_3.setObjectName("button_layout_3")
        self.use_app = QtGui.QPushButton(self.backup_page)
        self.use_app.setAutoDefault(False)
        self.use_app.setFlat(True)
        self.use_app.setObjectName("use_app")
        self.button_layout_3.addWidget(self.use_app)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_layout_3.addItem(spacerItem5)
        self.cancel_backup = QtGui.QPushButton(self.backup_page)
        self.cancel_backup.setAutoDefault(False)
        self.cancel_backup.setFlat(True)
        self.cancel_backup.setObjectName("cancel_backup")
        self.button_layout_3.addWidget(self.cancel_backup)
        self.verify_backup = QtGui.QPushButton(self.backup_page)
        self.verify_backup.setMinimumSize(QtCore.QSize(65, 0))
        self.verify_backup.setAutoDefault(True)
        self.verify_backup.setDefault(True)
        self.verify_backup.setFlat(True)
        self.verify_backup.setObjectName("verify_backup")
        self.button_layout_3.addWidget(self.verify_backup)
        self.verticalLayout_6.addLayout(self.button_layout_3)
        self.stackedWidget.addWidget(self.backup_page)
        self.ulf2_page = QtGui.QWidget()
        self.ulf2_page.setObjectName("ulf2_page")
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.ulf2_page)
        self.verticalLayout_21.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.ulf2_msg = QtGui.QLabel(self.ulf2_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ulf2_msg.sizePolicy().hasHeightForWidth())
        self.ulf2_msg.setSizePolicy(sizePolicy)
        self.ulf2_msg.setStyleSheet("padding-left: 40px; padding-left: 40px;padding-right: 40px;")
        self.ulf2_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.ulf2_msg.setWordWrap(True)
        self.ulf2_msg.setObjectName("ulf2_msg")
        self.verticalLayout_21.addWidget(self.ulf2_msg)
        self.ulf2_msg_back = QtGui.QLabel(self.ulf2_page)
        self.ulf2_msg_back.setAlignment(QtCore.Qt.AlignCenter)
        self.ulf2_msg_back.setWordWrap(True)
        self.ulf2_msg_back.setObjectName("ulf2_msg_back")
        self.verticalLayout_21.addWidget(self.ulf2_msg_back)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem6)
        self.ulf2_msg_help = QtGui.QLabel(self.ulf2_page)
        self.ulf2_msg_help.setAlignment(QtCore.Qt.AlignCenter)
        self.ulf2_msg_help.setWordWrap(True)
        self.ulf2_msg_help.setObjectName("ulf2_msg_help")
        self.verticalLayout_21.addWidget(self.ulf2_msg_help)
        self.stackedWidget.addWidget(self.ulf2_page)
        self.verticalLayout_72.addWidget(self.stackedWidget)
        self.stacked_main.addWidget(self.main_page)
        self.method_page = QtGui.QWidget()
        self.method_page.setObjectName("method_page")
        self.verticalLayout82 = QtGui.QVBoxLayout(self.method_page)
        self.verticalLayout82.setObjectName("verticalLayout82")
        self.method_back = QtGui.QLabel(self.method_page)
        self.method_back.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_back.sizePolicy().hasHeightForWidth())
        self.method_back.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_back.setFont(font)
        self.method_back.setObjectName("method_back")
        self.verticalLayout82.addWidget(self.method_back)
        self.method_message = QtGui.QLabel(self.method_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_message.sizePolicy().hasHeightForWidth())
        self.method_message.setSizePolicy(sizePolicy)
        self.method_message.setTextFormat(QtCore.Qt.PlainText)
        self.method_message.setWordWrap(True)
        self.method_message.setMargin(20)
        self.method_message.setObjectName("method_message")
        self.verticalLayout82.addWidget(self.method_message)
        self.method_browser_group = QtGui.QGroupBox(self.method_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_browser_group.sizePolicy().hasHeightForWidth())
        self.method_browser_group.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_browser_group.setFont(font)
        self.method_browser_group.setObjectName("method_browser_group")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.method_browser_group)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.method_browser_label = QtGui.QLabel(self.method_browser_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_browser_label.sizePolicy().hasHeightForWidth())
        self.method_browser_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_browser_label.setFont(font)
        self.method_browser_label.setWordWrap(True)
        self.method_browser_label.setObjectName("method_browser_label")
        self.horizontalLayout_5.addWidget(self.method_browser_label)
        self.method_browser_button = QtGui.QPushButton(self.method_browser_group)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_browser_button.setFont(font)
        self.method_browser_button.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(35, 165, 225);\n"
"border: 0px;\n"
"")
        self.method_browser_button.setObjectName("method_browser_button")
        self.horizontalLayout_5.addWidget(self.method_browser_button)
        self.verticalLayout82.addWidget(self.method_browser_group)
        self.method_web_group = QtGui.QGroupBox(self.method_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_web_group.sizePolicy().hasHeightForWidth())
        self.method_web_group.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_web_group.setFont(font)
        self.method_web_group.setObjectName("method_web_group")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.method_web_group)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.method_web_label = QtGui.QLabel(self.method_web_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_web_label.sizePolicy().hasHeightForWidth())
        self.method_web_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_web_label.setFont(font)
        self.method_web_label.setTextFormat(QtCore.Qt.AutoText)
        self.method_web_label.setWordWrap(True)
        self.method_web_label.setObjectName("method_web_label")
        self.horizontalLayout_6.addWidget(self.method_web_label)
        self.method_web_button = QtGui.QPushButton(self.method_web_group)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_web_button.setFont(font)
        self.method_web_button.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(35, 165, 225);\n"
"border: 0px;\n"
"")
        self.method_web_button.setObjectName("method_web_button")
        self.horizontalLayout_6.addWidget(self.method_web_button)
        self.verticalLayout82.addWidget(self.method_web_group)
        self.method_login_group = QtGui.QGroupBox(self.method_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_login_group.sizePolicy().hasHeightForWidth())
        self.method_login_group.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_login_group.setFont(font)
        self.method_login_group.setObjectName("method_login_group")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.method_login_group)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.method_login_label = QtGui.QLabel(self.method_login_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.method_login_label.sizePolicy().hasHeightForWidth())
        self.method_login_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_login_label.setFont(font)
        self.method_login_label.setWordWrap(True)
        self.method_login_label.setObjectName("method_login_label")
        self.horizontalLayout_7.addWidget(self.method_login_label)
        self.method_login_button = QtGui.QPushButton(self.method_login_group)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.method_login_button.setFont(font)
        self.method_login_button.setStyleSheet("color: rgb(248, 248, 248);\n"
"background-color: rgb(35, 165, 225);\n"
"border: 0px;\n"
"")
        self.method_login_button.setObjectName("method_login_button")
        self.horizontalLayout_7.addWidget(self.method_login_button)
        self.verticalLayout82.addWidget(self.method_login_group)
        self.stacked_main.addWidget(self.method_page)
        self.verticalLayout_2.addWidget(self.stacked_main)
        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(LoginDialog)
        self.stacked_main.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtGui.QApplication.translate("LoginDialog", "ShotGrid Login", None, QtGui.QApplication.UnicodeUTF8))
        self.site.setAccessibleName(QtGui.QApplication.translate("LoginDialog", "site", None, QtGui.QApplication.UnicodeUTF8))
        self.login.setAccessibleName(QtGui.QApplication.translate("LoginDialog", "login", None, QtGui.QApplication.UnicodeUTF8))
        self.password.setAccessibleName(QtGui.QApplication.translate("LoginDialog", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.password.setPlaceholderText(QtGui.QApplication.translate("LoginDialog", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.message.setText(QtGui.QApplication.translate("LoginDialog", "Please enter your credentials.", None, QtGui.QApplication.UnicodeUTF8))
        self.forgot_password_link.setText(QtGui.QApplication.translate("LoginDialog", "<html><head/><body><p><a href=\"http://mystudio.shotgrid.autodesk.com/user/forgot_password\"><span style=\" text-decoration: underline; color:#c0c1c3;\">Forgot your password?</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.button_options.setText(QtGui.QApplication.translate("LoginDialog", "See other options", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("LoginDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.sign_in.setText(QtGui.QApplication.translate("LoginDialog", "Sign In", None, QtGui.QApplication.UnicodeUTF8))
        self.sign_in.setProperty("class", QtGui.QApplication.translate("LoginDialog", "main", None, QtGui.QApplication.UnicodeUTF8))
        self._2fa_message.setText(QtGui.QApplication.translate("LoginDialog", "Enter the code generated by the Google Authenticator or Duo Mobile app.", None, QtGui.QApplication.UnicodeUTF8))
        self._2fa_code.setAccessibleName(QtGui.QApplication.translate("LoginDialog", "2fa code", None, QtGui.QApplication.UnicodeUTF8))
        self._2fa_code.setPlaceholderText(QtGui.QApplication.translate("LoginDialog", "Enter code", None, QtGui.QApplication.UnicodeUTF8))
        self.use_backup.setText(QtGui.QApplication.translate("LoginDialog", "Use backup code", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_tfa.setText(QtGui.QApplication.translate("LoginDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_2fa.setText(QtGui.QApplication.translate("LoginDialog", "Verify", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_2fa.setProperty("class", QtGui.QApplication.translate("LoginDialog", "main", None, QtGui.QApplication.UnicodeUTF8))
        self._2fa_message_2.setText(QtGui.QApplication.translate("LoginDialog", "Please enter one of your backup codes.", None, QtGui.QApplication.UnicodeUTF8))
        self.backup_code.setAccessibleName(QtGui.QApplication.translate("LoginDialog", "backup code", None, QtGui.QApplication.UnicodeUTF8))
        self.backup_code.setPlaceholderText(QtGui.QApplication.translate("LoginDialog", "Enter backup code", None, QtGui.QApplication.UnicodeUTF8))
        self.use_app.setText(QtGui.QApplication.translate("LoginDialog", "Use Google App", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_backup.setText(QtGui.QApplication.translate("LoginDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_backup.setText(QtGui.QApplication.translate("LoginDialog", "Verify", None, QtGui.QApplication.UnicodeUTF8))
        self.verify_backup.setProperty("class", QtGui.QApplication.translate("LoginDialog", "main", None, QtGui.QApplication.UnicodeUTF8))
        self.ulf2_msg.setText(QtGui.QApplication.translate("LoginDialog", "Check your default web browser to continue logging in.", None, QtGui.QApplication.UnicodeUTF8))
        self.ulf2_msg_back.setText(QtGui.QApplication.translate("LoginDialog", "<html><head/><body><p>&lt; <a href=\"#\"><span style=\" text-decoration: underline; color:#c0c1c3;\">Cancel & return to the login page</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ulf2_msg_help.setText(QtGui.QApplication.translate("LoginDialog", "<html><head/><body><p>If you are having trouble logging in with the browser, <a href=\"{url}\"><span style=\" text-decoration: underline; color:#c0c1c3;\">select this support link</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.method_back.setToolTip(QtGui.QApplication.translate("LoginDialog", "Return to the login window", None, QtGui.QApplication.UnicodeUTF8))
        self.method_back.setText(QtGui.QApplication.translate("LoginDialog", "<html><head/><body><p><a href=\"#\"><span style=\" text-decoration: underline; color:#c0c1c3;\">Go back</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.method_message.setText(QtGui.QApplication.translate("LoginDialog", "A default authentication can be set for the next time you log in by click on the options", None, QtGui.QApplication.UnicodeUTF8))
        self.method_browser_group.setTitle(QtGui.QApplication.translate("LoginDialog", "Local browser", None, QtGui.QApplication.UnicodeUTF8))
        self.method_browser_label.setText(QtGui.QApplication.translate("LoginDialog", "<html><head/><body><p>A good description of this authentication method.<br/>This is the recommanded method.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.method_browser_button.setText(QtGui.QApplication.translate("LoginDialog", "Launch browser", None, QtGui.QApplication.UnicodeUTF8))
        self.method_web_group.setTitle(QtGui.QApplication.translate("LoginDialog", "Web login", None, QtGui.QApplication.UnicodeUTF8))
        self.method_web_label.setText(QtGui.QApplication.translate("LoginDialog", "Selecting this method, you will be prompted for login credentials from inside an internal web browser", None, QtGui.QApplication.UnicodeUTF8))
        self.method_web_button.setText(QtGui.QApplication.translate("LoginDialog", "Launch browser", None, QtGui.QApplication.UnicodeUTF8))
        self.method_login_group.setTitle(QtGui.QApplication.translate("LoginDialog", "Login credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.method_login_label.setText(QtGui.QApplication.translate("LoginDialog", "This is the legacy authentication using a login, a password. And potentially a two-factor authentication.", None, QtGui.QApplication.UnicodeUTF8))
        self.method_login_button.setText(QtGui.QApplication.translate("LoginDialog", "Enter login credentials", None, QtGui.QApplication.UnicodeUTF8))

from .aspect_preserving_label import AspectPreservingLabel
from .recent_box import RecentBox
from .qt5_like_line_edit import Qt5LikeLineEdit
from . import resources_rc
from . import resources_rc

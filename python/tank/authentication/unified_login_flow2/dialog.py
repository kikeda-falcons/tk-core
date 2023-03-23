# Copyright (c) 2023 Shotgrid Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
QT Login dialog for authenticating to a ShotGrid server.

--------------------------------------------------------------------------------
NOTE! This module is part of the authentication library internals and should
not be called directly. Interfaces and implementation of this module may change
at any point.
--------------------------------------------------------------------------------
"""

from ..ui import unified_login_flow2_dialog
from ..ui.qt_abstraction import QtGui, QtCore

from .background import AuthTask

from ... import LogManager
logger = LogManager.get_logger(__name__)

class Dialog(QtGui.QDialog):
    def __init__(
        self,
        # is_session_renewal,
        sg_url,
        sg_login=None,
        http_proxy=None,
        product=None,
        parent=None,
    ):
        super().__init__(parent)

        self._sg_url = sg_url
        self._sg_login = sg_login
        self._http_proxy = http_proxy
        self._product = product

        # Create the result object
        self.session_info = None

        # setup the gui
        self.ui = unified_login_flow2_dialog.Ui_UnifiedLoginFlow2Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Authentication with web browser")

        self.ui.cancel.clicked.connect(self._cancel_pressed)

        self._auth_task = AuthTask(self)
        self._auth_task.finished.connect(self._auth_task_finished)

        # Make the worker report on the toolkit bootstrap progress.
        self._auth_task.progressing.connect(self._auth_task_progressing)

        self.spinner = QtGui.QMovie(":/spinner/spinner.gif")
        self.ui.label_spinner.setMovie(self.spinner)
        self.spinner.start()

    def __del__(self):
        """
        Destructor.
        """

        if self._auth_task and self._auth_task.isRunning():
            self._auth_task.terminate()
            self._auth_task.wait()

    ## Override QDialog methods

    def closeEvent(self, event):
        print("This is an on close event!", event)
        event.ignore()
        # we don't want to just close this window. The cancel button is there.

    def keyPressEvent(self, event):
        print("key press", event.key())
        if event.key() == QtCore.Qt.Key_Escape:
            # Ignore this one, we have cancel for that
            event.ignore()
            return

        super().keyPressEvent(event)

    def exec_(self):
        """
        Displays the window modally.
        """
        # This fixes a weird bug on Qt where calling show() and exec_() might lead
        # to having an invisible modal QDialog and this state freezes the host
        # application. (Require a `pkill -9 applicationName`). The fix in our case
        # is pretty simple, we just have to not call show() before the call to
        # exec_() since it implicitly call exec_().
        #

        # This bug is described here: https://bugreports.qt.io/browse/QTBUG-48248
        if QtCore.__version__.startswith("4."):
            self.show()

        self.raise_()
        self.activateWindow()

        # the trick of activating + raising does not seem to be enough for
        # modal dialogs. So force put them on top as well.
        # On PySide2, or-ring the current window flags with WindowStaysOnTopHint causes the dialog
        # to freeze, so only set the WindowStaysOnTopHint flag as this appears to not disable the
        # other flags.
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # Start the background task just before starting the dialog event loop
        self._auth_task.start()

        return super().exec_()

    ## Event handlers

    def _cancel_pressed(self):
        print("_cancel_pressed")

        if self._auth_task.isRunning():
            self._auth_task.terminate()

        self.reject()

    def _auth_task_finished(self):
        print("_auth_task_finished")
        if not self.session_info:
            # The task got interrupted somehow.
            return

        print("finish")
        self.accept()

    @QtCore.Slot(str)
    def _auth_task_progressing(self, message):
        # A decorator is used to shield against the slot threading issue
        # described here: http://stackoverflow.com/questions/20752154/pyqt-connecting-a-signal-to-a-slot-to-start-a-background-operation

        self.ui.message.setText(message)



if __name__ == "__main__":
    # Define a Main dialog first to run our tests
    class TestMainDialog(QtGui.QDialog):
        def __init__(self, sg_url):
            super().__init__(None)
            self._sg_url = sg_url

            self.setWindowTitle("Authentication with web browser")
            self.resize(200, 200)
            self.setMinimumSize(QtCore.QSize(200, 200))
            self.setModal(True)

            self.vLayout = QtGui.QVBoxLayout(self)
            self.vLayout.setContentsMargins(20, 20, 20, 20)

            self.message = QtGui.QLabel("Test me")
            self.message.setAlignment(
                QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter
            )
            self.message.setWordWrap(True)
            self.vLayout.addWidget(self.message)

            self.button = QtGui.QPushButton("Go web auth!")
            self.button.setAutoDefault(True)
            self.vLayout.addWidget(self.button)
            self.button.clicked.connect(self._button_pressed)

        def _button_pressed(self):
            print("button pressed!")
            self.message.setText("Processing authentication...")

            d = Dialog(self._sg_url)
            res = d.exec_()
            print("res:", res)
            if res == QtGui.QDialog.Rejected:
                self.message.setText("Authentication failed. Please try again!")
            elif res == QtGui.QDialog.Accepted:
                self.message.setText("Authentication worked. Congrats!")
            else:
                self.message.setText("Unknow error... :(")

        def exec_(self):
            self.raise_()
            self.activateWindow()
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            return super().exec_()

    import argparse
    parser = argparse.ArgumentParser(
        description="Main of ULF2 dialog. Can be used for testing purposes",
    )
    parser.add_argument("sg_url", help="ShotGrid URL")
    args = parser.parse_args()


    from PySide2 import QtWidgets
    QtWidgets.QApplication()

    d = TestMainDialog(args.sg_url)
    d.exec_()

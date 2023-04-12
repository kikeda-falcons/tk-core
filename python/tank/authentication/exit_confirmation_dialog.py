# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
QT dialog for exit confirmation.

--------------------------------------------------------------------------------
NOTE! This module is part of the authentication library internals and should
not be called directly. Interfaces and implementation of this module may change
at any point.
--------------------------------------------------------------------------------
"""
from .ui import resources_rc  # noqa
from .ui.qt_abstraction import QtGui, QtCore


class ExitDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Prevent resize
        self.setFixedSize(self.minimumSize())

        # Configure the dialog window
        self.setWindowTitle("Closing ShotGrid Login")

        # Create label for the confirmation message
        message_label = QtGui.QLabel("Are you sure you want to close this window?", self)

        # Create buttons for yes and no
        buttonBox = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Yes | QtGui.QDialogButtonBox.No,
        )
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(message_label)
        vbox.addWidget(buttonBox)

        self.setLayout(vbox)
        self.setModal(True)

        self.setStyleSheet("""
QWidget
{
    background-color: rgb(36, 39, 42);
    color: rgb(192, 192, 192);
    selection-background-color: rgb(168, 123, 43);
    selection-color: rgb(230, 230, 230);
    font-size: 11px;
}

QPushButton
{
    background-color: transparent;
    border-radius: 2px;
    padding: 8px;
    padding-left: 15px;
    padding-right: 15px;
}

QPushButton:hover {
    border: 1px solid rgb(54, 60, 66);
}

QPushButton:focus {
    border: 1px solid rgb(48, 167, 227);
}
""")

    def exec_(self):
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

        return super().exec_()

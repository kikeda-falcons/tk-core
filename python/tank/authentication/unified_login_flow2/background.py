# Copyright (c) 2023 Autodesk.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import time

from . import authentication

from ..ui.qt_abstraction import QtCore, QtGui

class AuthTask(QtCore.QThread):
    progressing = QtCore.Signal(str)

    def __init__(self, dialog):
        super().__init__(dialog)
        self.setTerminationEnabled(True)

        self._dialog = dialog

    def run(self):
        self._dialog.session_info = authentication.process(
            self._dialog._sg_url,
            login=self._dialog._sg_login,
            http_proxy=self._dialog._http_proxy,
            product=self._dialog._product,
            browser_open_callback = lambda u: QtGui.QDesktopServices.openUrl(u),
            progress_info_callback=self.on_progress_info,
        )


    def on_progress_info(self, message, **kwargs):
        # TODO: replace message by status ...??

        if "started_waiting" in kwargs:
            delta = time.time() - kwargs["started_waiting"]
            self.progressing.emit(f"Waited {delta:.0f} seconds; waiting another one...")

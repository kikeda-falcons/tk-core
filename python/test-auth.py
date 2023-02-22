from tank import log
lm = log.LogManager()
lm.global_debug = True
lm.initialize_custom_handler()

from PySide2 import QtWidgets

from tank import authentication
from tank.authentication import login_dialog, invoker

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--mode", "-m", choices=["dialog", "auth"], default="dialog")
args = parser.parse_args()

# Hook behaviour
login_dialog._is_running_in_desktop = lambda: True

QtWidgets.QApplication()

if args.mode == "dialog":
    gui_launcher = invoker.create()
    result = gui_launcher(
        lambda: login_dialog.LoginDialog(
            is_session_renewal=False,
        ).result()
    )
    print("result:",result)
elif args.mode == "auth":
    shotgun_authenticator = authentication.ShotgunAuthenticator()
    user = shotgun_authenticator.get_user()
    print("User:", user)

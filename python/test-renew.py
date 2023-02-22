from tank import log
lm = log.LogManager()
lm.global_debug = True
lm.initialize_custom_handler()

from tank import authentication
from tank.authentication import interactive_authentication

# Hook behaviour - force console mode
interactive_authentication._get_ui_state = lambda: False

shotgun_authenticator = authentication.ShotgunAuthenticator()
user = shotgun_authenticator.get_user()
print("User:", user)

input("Press enter to continue (renew)")

interactive_authentication.renew_session(user._impl)

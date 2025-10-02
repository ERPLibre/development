# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

import odoo
from odoo import SUPERUSER_ID, _, api

_logger = logging.getLogger(__name__)
login = "test"


def uninstall_hook(env):
    _logger.warning("User test is installed, don't forget to uninstall it.")
    # user_test = env["res.users"].search([("login", "=", login)])
    # if user_test:
    #     user_test.unlink()


def post_init_hook(env):
    # Ignore
    if not odoo.tools.config["dev_mode"]:
        raise Exception(
            _(
                "Cancel installation module user_test, please specify --dev [options] in your instance."
            )
        )

    # Copy the profile of default user and copy the system user permission
    system_user = env["res.users"].browse(1)
    first_user = env["res.users"].browse(2)
    test_user = env["res.users"].search(
        [("login", "=", login), ("active", "in", [True, False])]
    )
    if test_user:
        test_user.unlink()
    user_test_info = {
        "name": login,
        "login": login,
        "new_password": login,
        "password": login,
        "groups_id": [a.id for a in system_user.groups_id],
        # "chatter_position": "side",
    }
    copied_user = first_user.copy(user_test_info)
    copied_user.write({"active": True, "new_password": login, "password": login})

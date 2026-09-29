# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

import os

import openerp
from openerp import SUPERUSER_ID, _, api

_logger = logging.getLogger(__name__)


def mode_developpement():
    """Le mode développeur : --dev en Odoo 9, ERPLIBRE_DEV_MODE en 8, qui
    n'a pas l'option et où odoo_bin.sh le passe par l'environnement."""
    return openerp.tools.config.get("dev_mode") or os.environ.get(
        "ERPLIBRE_DEV_MODE"
    )
login = "test"


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _logger.warning("User test is installed, don't forget to uninstall it.")
    # user_test = env["res.users"].search([("login", "=", login)])
    # if user_test:
    #     user_test.unlink()


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Ignore
    if not mode_developpement():
        raise Exception(
            _(
                "Cancel installation module user_test, please specify --dev [options] in your instance."
            )
        )

    # Copy the profile of default user and copy the system user permission
    # En Odoo 8 à 11, l'administrateur EST l'utilisateur 1 : il n'y a pas
    # encore de __system__ distinct, et l'utilisateur 2 n'existe pas.
    system_user = env.ref("base.user_root")
    first_user = system_user
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
        # Une commande x2many : Odoo 8 et 9 refusent une liste nue d'ids.
        "groups_id": [(6, 0, system_user.groups_id.ids)],
        # "chatter_position": "side",
    }
    copied_user = first_user.copy(user_test_info)
    copied_user.write({"active": True, "new_password": login, "password": login})

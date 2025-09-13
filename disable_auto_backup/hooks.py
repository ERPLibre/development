# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

import odoo
from odoo import SUPERUSER_ID, _, api

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    # Ignore
    if not odoo.tools.config["dev_mode"]:
        raise Exception(
            _(
                "Cancel installation module disable_mail_server, "
                "please specify --dev [options] in your instance."
            )
        )

    env["db.backup"].search([]).unlink()

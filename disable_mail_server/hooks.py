# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import os

import openerp
from openerp import _, api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def mode_developpement():
    """Le mode développeur : --dev en Odoo 9, ERPLIBRE_DEV_MODE en 8, qui
    n'a pas l'option et où odoo_bin.sh le passe par l'environnement."""
    return openerp.tools.config.get("dev_mode") or os.environ.get(
        "ERPLIBRE_DEV_MODE"
    )


def post_init_hook(cr, e):
    # Ignore
    if not mode_developpement():
        raise Exception(_("Cancel installation module disable_mail_server, "
                          "please specify --dev [options] in your instance."))

    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        env['ir.mail_server'].search([]).unlink()
        env['fetchmail.server'].search([]).unlink()

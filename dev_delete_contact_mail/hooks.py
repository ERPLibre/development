# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import odoo
from odoo import _, api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def post_init_hook(cr, e):
    # Ignore
    if not odoo.tools.config['dev_mode']:
        raise Exception(_("Cancel installation module user_test, please specify --dev [options] in your instance."))

    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        partners = env['res.partner'].search([])
        for partner in partners:
            partner.email = ""

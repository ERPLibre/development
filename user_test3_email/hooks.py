# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import odoo
from odoo import _, api, SUPERUSER_ID

_logger = logging.getLogger(__name__)
login = 'test3@technolibre.ca'


def uninstall_hook(cr, _):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        user_test = env['res.users'].search([('login', '=', login)])
        if user_test:
            user_test.unlink()


def post_init_hook(cr, e):
    # Ignore
    if not odoo.tools.config['dev_mode']:
        raise Exception(
            _("Cancel installation module user_test3_email, please specify --dev [options] in your instance."))

    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        # Copy the profile of default user and copy the system user permission
        system_user = env['res.users'].browse(1)
        first_user = env['res.users'].browse(2)
        user_test_info = {
            "name": "test3",
            "login": login,
            "email": login,
            "new_password": "test",
            'groups_id': [a.id for a in system_user.groups_id]
        }
        first_user.copy(user_test_info)

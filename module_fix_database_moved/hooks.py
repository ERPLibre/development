# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import odoo
from odoo import _, api, SUPERUSER_ID

_logger = logging.getLogger(__name__)
login = 'test'


def uninstall_hook(cr, _):
    # with api.Environment.manage():
    #     env = api.Environment(cr, SUPERUSER_ID, {})
    #     user_test = env['res.users'].search([('login', '=', login)])
    #     if user_test:
    #         user_test.unlink()
    pass


def post_init_hook(cr, e):
    # Ignore
    if not odoo.tools.config['dev_mode']:
        raise Exception(_(
            "Cancel installation module user_test, please specify --dev [options] in your instance."))

    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        mail_message_ids = env["mail.message"].search([])
        for msg in mail_message_ids:
            if msg.body_moved0 or msg.body_moved1 or msg.body_moved2 or msg.body_moved3:
                if msg.body:
                    raise Exception(
                        "Error, fields contain body and body_moved id %s" % msg.id)
                if [bool(msg.body_moved0), bool(msg.body_moved1), bool(msg.body_moved2),
                    bool(msg.body_moved3)].count(True) > 1:
                    raise Exception("Error, conflict with all body_moved %s" % msg.id)
                if msg.body_moved0:
                    msg.body = msg.body_moved0
                    msg.body_moved0 = False
                elif msg.body_moved1:
                    msg.body = msg.body_moved1
                    msg.body_moved1 = False
                elif msg.body_moved2:
                    msg.body = msg.body_moved2
                    msg.body_moved2 = False
                elif msg.body_moved3:
                    msg.body = msg.body_moved3
                    msg.body_moved3 = False
                else:
                    raise Exception("Error in code, check your conditions.")
                print(f"Fixed id {msg.id}.")
            else:
                print(f"Ignore msg id {msg.id}.")

        print("Done migration.")

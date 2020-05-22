import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class Message(models.Model):
    _inherit = 'mail.message'

    body_moved0 = fields.Char('Contents moved0')
    body_moved1 = fields.Char('Contents moved1')
    body_moved2 = fields.Char('Contents moved2')
    body_moved3 = fields.Char('Contents moved3')

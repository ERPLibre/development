# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

import odoo
from odoo import SUPERUSER_ID, _, api

_logger = logging.getLogger(__name__)


def post_init_hook(cr, e):
    if not odoo.tools.config["dev_mode"]:
        raise Exception(
            _(
                "Cancel installation module disable_payment_provider, "
                "please specify --dev [options] in your instance."
            )
        )

    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        # Le module `payment` n'est pas installé : il n'y a rien à désactiver,
        # et ce n'est pas une erreur. Dépendre de `payment` pour s'en assurer
        # l'INSTALLERAIT, ce qui serait pire que le problème.
        if "payment.acquirer" not in env:
            _logger.info("disable_payment_provider: payment.acquirer is not in this database.")
            return
        # active_test=False : `payment.acquirer` porte un champ `active` de
        # 12 à 15 — un fournisseur archivé y garde ses clés et se réactive
        # d'un clic. `payment.provider` n'en a plus depuis 16 ; le contexte
        # y est alors sans effet, et le garder évite d'avoir deux versions
        # du même hook pour une ligne.
        records = env["payment.acquirer"].with_context(active_test=False).search([])
        if not records:
            _logger.info("disable_payment_provider: no payment.acquirer to disable.")
            return
        records.write({"website_published": False, "environment": "test"})
        _logger.info("disable_payment_provider: disabled %s payment.acquirer(s).", len(records))

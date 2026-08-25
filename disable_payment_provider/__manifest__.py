# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'disable_payment_provider',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Extra tools',
    'summary': 'Disable every payment acquirer',
    'description': """
disable_payment_provider
========================
Disable every payment acquirer so a development copy cannot charge a real
card. Odoo 12 to 15 call the model `payment.acquirer`, Odoo 16 and later
`payment.provider`; the module keeps ONE name across every version so the
same command line works at every migration step.

It depends on `base` alone, on purpose: depending on `payment` would
INSTALL that module on a database that does not have it. The hook checks
for the model instead, and says so when there is nothing to do.
""",
    'depends': [
        'base',
    ],
    'data': [
    ],
    "post_init_hook": "post_init_hook",
    'installable': True,
}

# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'dev_delete_newsletter_mail',
    'version': '13.0.0.1',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'Extra tools',
    'summary': 'delete email from all newsletter',
    'description': """
dev_delete_newsletter_mail
=======================

""",
    'depends': [
        'website_mass_mailing',
    ],
    'data': [
    ],
    "post_init_hook": "post_init_hook",
    'installable': True,
}

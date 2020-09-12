# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'dev_delete_contact_mail',
    'version': '0.1',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'Extra tools',
    'summary': 'delete email from all contact',
    'description': """
dev_delete_contact_mail
=======================

""",
    'depends': [
        'contacts',
    ],
    'data': [
    ],
    "post_init_hook": "post_init_hook",
    'installable': True,
}

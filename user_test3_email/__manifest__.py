# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'user_test3_email',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Extra tools',
    'summary': 'Add user test3@technolibre.ca',
    'description': """
user_test3_email
================
Add user test3@technolibre.ca with password test.
Never install this module in a production instance.
You need to use parameters --dev at instance, by security, with any values to be able to install this module.
""",
    'depends': [
        'base'
    ],
    'data': [
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
    'installable': True,
}

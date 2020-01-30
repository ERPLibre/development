# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'disable_mail_server',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Extra tools',
    'summary': 'Remove mail server',
    'description': """
disable_mail_server
===================
Remove all mail server in dev to don't send email when dev.
""",
    'depends': [
        'base'
    ],
    'data': [
    ],
    "post_init_hook": "post_init_hook",
    'installable': True,
}

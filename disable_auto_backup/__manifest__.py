# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'disable_auto_backup',
    'version': '0.1',
    'author': "MathBenTech",
    'website': 'https://mathben.tech',
    'license': 'AGPL-3',
    'category': 'Extra tools',
    'summary': 'Remove auto backup',
    'description': """
disable_auto_backup
===================
Remove all backup in dev to don't send email when dev.
""",
    'depends': [
        'base'
    ],
    'data': [
    ],
    "post_init_hook": "post_init_hook",
    'installable': True,
}

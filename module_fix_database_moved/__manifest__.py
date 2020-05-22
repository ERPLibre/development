# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'module_fix_database_moved',
    'version': '0.1',
    'author': "TechnoLibre",
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'Extra tools',
    'summary': 'Fix database mail',
    'description': """
module_fix_database_moved
=========================
""",
    'depends': [
        'mail'
    ],
    'data': [
    ],
    "post_init_hook": "post_init_hook",
    # "uninstall_hook": "uninstall_hook",
    'installable': True,
}

# Copyright 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Transportation',
    'version': '12.0.1.0.0',
    'category': 'Customer Relationship Management',
    'summary': 'This module adds transportation page in partner',
    'author': 'Savoir-faire Linux, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-travel',
    'license': 'AGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
}

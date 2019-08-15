# Copyright 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Partner Airport',
    'version': '12.0.1.0.0',
    'summary': 'This module allows to set partner as airports',
    'category': 'Customer Relationship Management',
    'author': 'Savoir-faire Linux, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-travel',
    'license': 'AGPL-3',
    'depends': [
        'transportation',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
}

# Copyright 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Travel',
    'version': '12.0.1.0.0',
    'category': 'Customer Relationship Management',
    'summary': 'Travel Management',
    'author': 'Savoir-faire Linux, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-travel',
    'depends': [
        'mail',
        'base_address_city',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/travel.xml',
        'views/travel_stage.xml',
        'views/travel_tag.xml',
    ],
    'demo': [
        'demo/travel.xml',
    ],
}

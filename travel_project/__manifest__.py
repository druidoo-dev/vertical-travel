# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Travel Project',
    'version': '12.0.1.0.0',
    'category': 'Customer Relationship Management',
    'summary': 'Use projects to manage travels',
    'author': 'Druidoo, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/vertical-travel',
    'depends': [
        'travel',
        'project',
    ],
    'data': [
        'security/security.xml',
        'views/travel.xml',
    ],
}

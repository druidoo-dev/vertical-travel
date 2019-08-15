# Copyright 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class TravelPassenger(models.Model):
    _name = 'travel.passenger'
    _description = 'Travel Passenger'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'partner_id'

    partner_id = fields.Many2one(
        'res.partner',
        'Passenger',
        required=True,
        ondelete='restrict',
    )

    travel_id = fields.Many2one(
        'travel.travel',
        'Travel',
        help='Travel for which the passenger is participating.',
        ondelete='cascade',
        required=True,
        index=True,
    )

    @api.multi
    def name_get(self):
        return [(
            rec.id,
            '%s / %s' % (rec.partner_id.name, rec.travel_id.name)
            ) for rec in self]

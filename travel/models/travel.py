# Copyright 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class Travel(models.Model):
    _name = 'travel.travel'
    _description = 'Travel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _date_name = "date_start"

    name = fields.Char(required=True)
    description = fields.Html()

    active = fields.Boolean(default=True)

    tag_ids = fields.Many2many('travel.tag', string='Tags')

    date_start = fields.Date('Start Date', required=True)
    date_stop = fields.Date('End Date', required=True)

    city_ids = fields.Many2many(
        'res.city',
        string='Locations',
        help='Destination cities of travel.',
    )

    passenger_ids = fields.One2many(
        'travel.passenger',
        'travel_id',
        'Passengers',
        help='List of passengers.',
    )

    stage_id = fields.Many2one(
        'travel.stage',
        ondelete='restrict',
        default=lambda self: self.env['travel.stage'].search(
            [('fold', '=', False)], order='sequence', limit=1),
    )

    @api.multi
    @api.constrains('date_start', 'date_stop')
    def check_date(self):
        for rec in self:
            if rec.date_start > rec.date_stop:
                raise ValidationError(
                    _('Start date cannot be after departure date.'))

# Copyright 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>)
# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class Travel(models.Model):
    _name = 'travel.travel'
    _description = 'Travel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, sequence, activity_date_deadline, date_start desc'
    _date_name = "date_start"

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return stages.search([], order=order)

    name = fields.Char(required=True)
    description = fields.Html()

    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

    tag_ids = fields.Many2many('travel.tag', string='Tags')

    color = fields.Integer(string='Color Index')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ],
        string="Priority",
        default='0',
        index=True,
    )

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.user.company_id,
    )

    currency_id = fields.Many2one(related="company_id.currency_id")

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
        group_expand='_read_group_stage_ids',
    )

    partner_id = fields.Many2one(
        'res.partner',
        'Contact',
        help='Contact person for this trip.',
    )

    user_id = fields.Many2one(
        'res.users',
        'Assigned to',
        help='User assigned to this travel',
    )

    @api.multi
    @api.constrains('date_start', 'date_stop')
    def check_date(self):
        for rec in self:
            if rec.date_start > rec.date_stop:
                raise ValidationError(
                    _('Start date cannot be after departure date.'))

    @api.onchange('date_start')
    def _onchange_date_start(self):
        for rec in self:
            if rec.date_start and (
                not rec.date_stop or
                (rec.date_stop and rec.date_start > rec.date_stop)
            ):
                rec.date_stop = rec.date_start

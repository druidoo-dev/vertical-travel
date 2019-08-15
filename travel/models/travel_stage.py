# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields


class TravelStage(models.Model):
    _name = 'travel.stage'
    _description = 'Travel Stage'
    _order = 'sequence, id'

    name = fields.Char('Stage Name', required=True, translate=True)
    description = fields.Text(translate=True)
    sequence = fields.Integer(default=1)

    fold = fields.Boolean(
        string='Folded in Kanban',
        help=(
            'This stage is folded in the kanban view when there are no '
            'records in that stage to display.'
        ),
    )

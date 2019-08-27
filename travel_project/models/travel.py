# Copyright 2019 Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models, fields, _


class Travel(models.Model):
    _inherit = 'travel.travel'

    project_id = fields.Many2one(
        'project.project',
        string='Project',
        help='The project linked to this travel',
        ondelete='restrict',
        delegate=True,
        auto_join=True,
        index=True,
        required=True,
    )

    name = fields.Char(
        related='project_id.name',
        inherited=True,
        readonly=False,
        store=True,
    )

    user_id = fields.Many2one(
        related='project_id.user_id',
        inherited=True,
        readonly=False,
        store=True,
    )

    partner_id = fields.Many2one(
        related='project_id.partner_id',
        inherited=True,
        readonly=False,
        store=True,
    )

    color = fields.Integer(
        related='project_id.color',
        inherited=True,
        readonly=False,
        store=True,
    )

    active = fields.Boolean(
        related='project_id.active',
        inherited=True,
        readonly=False,
        store=True,
    )

    def action_view_all_rating(self):
        return self.project_id.action_view_all_rating()

    def attachment_tree_view(self):
        return self.project_id.attachment_tree_view()

    def action_view_tasks(self):
        self.ensure_one()
        act = self.env.ref('project.act_project_project_2_project_task_all')
        act = act.read()[0]
        act['context'] = {
            'search_default_project_id': [self.project_id.id],
            'default_project_id': self.project_id.id,
        }
        return act

    # mail.thread unification

    def _message_subscribe(
        self,
        partner_ids=None, channel_ids=None,
        subtype_ids=None, customer_ids=None
    ):
        self.mapped('project_id')._message_subscribe(
            partner_ids=partner_ids,
            channel_ids=channel_ids,
            subtype_ids=subtype_ids,
            customer_ids=customer_ids,
        )
        return super()._message_subscribe(
            partner_ids=partner_ids,
            channel_ids=channel_ids,
            subtype_ids=subtype_ids,
            customer_ids=customer_ids,
        )

    def message_unsubscribe(self, partner_ids=None, channel_ids=None):
        self.mapped('project_id').message_unsubscribe(
            partner_ids=partner_ids,
            channel_ids=channel_ids)
        return super().message_unsubscribe(
            partner_ids=partner_ids,
            channel_ids=channel_ids)

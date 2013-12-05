# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm
from openerp.tools.translate import _


class travel_passenger(orm.Model):
    _description = 'Passenger on travel'
    _name = 'travel.passenger'
    _inherit = ['mail.thread']
    _columns = {
        'partner_id': fields.many2one('res.partner', 'Name', required=True, ondelete='cascade',
                                        help="Name of Passenger."),
        'travel_id': fields.many2one('travel.travel', 'Travel',
                                     help='Travel on which the passenger is going.'),
        'department_id': fields.many2one('hr.department', 'Department'),
    }

    def name_get(self, cr, uid, ids, context=None):
        return [(i.id, i.partner_id.name) for i in self.browse(cr, uid, ids, context=context)]

    def action_passenger_form_view(self, cr, uid, ids, context=None):
        return {
            'name': _('Passenger'),
            'res_model': 'travel.passenger',
            'view_mode': 'form',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': ids[0],
            'context': context,
        }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

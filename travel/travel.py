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


class travel_passenger(orm.Model):
    _description = 'Passenger on travel'
    _name = 'travel.passenger'
    _columns = {
        'name': fields.many2one('res.partner', 'Name', required=True, ondelete='cascade',
                                help="Name of partner."),
        'date': fields.datetime('Date', required=True, help='Time of departure.')
    }


class travel_travel(orm.Model):
    _description = 'Travel'
    _name = 'travel.travel'
    _columns = {
        'name': fields.char('Name', size=256, required=True, select=True,
                            help='Name of travel.'),
        'city_id': fields.many2one('res.country.state.city', 'City', required='True',
                                   help='Destination city of travel.'),
        'date_start': fields.date('Start Date', required=True),
        'date_stop': fields.date('End Date', required=True),
        'passenger_ids': fields.many2many('travel.passenger', 'travel_travel_passenger_rel', 'travel_id',
                                          'travel_passenger_id', 'Passengers', help='List of passengers.'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

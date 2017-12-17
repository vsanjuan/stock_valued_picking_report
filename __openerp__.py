# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2014 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#                       Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
#    Copyright (c) 2015 Antiun Ingenieria (http://www.antiun.com)
#                       Antonio Espinosa <antonioea@antiun.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Valued picking list",
    "version": "8.0.0.2.0",
    "author": "Acelerem",
    "website": "www.acelerem.com",
    "category": "Warehouse Management",
    "license": "GPL-3",
    "depends": [
        "base",
        "account",
        "stock",
        "sale",
        "delivery",
        "stock_picking_taxes",
        "web_context_tunnel"
    ],
    "data": [
        'views/res_partner_view.xml',
        'views/stock_picking_view.xml',
        'report/stock_picking_valued_report.xml',
    ],
    "installable": True
}

# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Always Show Invoice Warnings',
    'category': 'Accounting',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['warning'],
    'description': """
Always Show Invoice Warnings
============================
* Modifies the functionality of the core's warning module so that the invoice warning is always on the invoice form
""",
    'data': [
        'views/account_invoice.xml',
    ],
}

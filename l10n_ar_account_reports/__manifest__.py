# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Reportes Argentinos de Contabilidad',
    'summary': 'View and create reports',
    'category': 'Accounting',
    'description': """
Reportes Argentinos de Contabilidad
===================================
    """,
    'depends': ['account'],
    'data': [
        'data/account_financial_report_data.xml',
    ],
    'auto_install': False,
    'installable': True,
    'license': 'AGPL-3',
}

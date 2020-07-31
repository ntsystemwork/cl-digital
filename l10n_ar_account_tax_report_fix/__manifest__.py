# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Localización Argentina, Account report fix',
    'summary': 'Account Tax Report Fix',
    'category': 'Accounting',
    'author': 'NT System Work',
    'description': """
Este módulo es un parche que agrega los tipos de impuestos incorporados por el módulo withholding
de la localización arg. al reporte de impuesto de Odoo
    """,
    'depends': ['account', 'account_withholding'],
    'data': [
    ],
    'auto_install': False,
    'installable': True,
    'license': 'AGPL-3',
}

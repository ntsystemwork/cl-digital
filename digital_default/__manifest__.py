# -----------------------------------------------------------------------------
#
#    Copyright (C) 2019 NT System Work (http://www.ntsystemwork.com)
#    All Rights Reserved.
#
# -----------------------------------------------------------------------------
{
    'name': 'digital',
    'version': '11.0e.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customizacion para digital',
    'author': 'NT System Work',
    'depends': [
        # basic applications
        'sale_management',
        'account_invoicing',
        'purchase',

        # minimum modules for argentinian localizacion + utilities + fixes
        'standard_depends_ee',

        # restringir la creacion de productos
        'product_create_restriction',

        # exportacion de retenciones y percepciones automaticas.
        'l10n_ar_export_arba',
        'l10n_ar_export_sicore',

        'cash_flow',  # actualizar cashflow

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    #
    # Here begins docker-odoo-environment manifest
    # --------------------------------------------

    # port where odoo starts serving pages
    'port': '8069',

    'repos': [
        {'usr': 'ntsystemwork', 'repo': 'cl-digital', 'branch': '11.0',
         'ssh': True},

        {'usr': 'gcaceres93', 'repo': 'project_stock', 'branch': '11.0',
         'ssh': True, 'host': 'github.com-sati'},
        {'usr': 'gcaceres93', 'repo': 'fd', 'branch': '11.0',
         'ssh': True, 'host': 'github.com-sati'},

        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '11.0'},

        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'sale', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'product', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'partner', 'branch': '11.0'},
        {'usr': 'ingadhoc', 'repo': 'account-invoicing', 'branch': '11.0'},

        {'usr': 'oca', 'repo': 'partner-contact', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'web', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-tools', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'social', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'sale-workflow', 'branch': '11.0'},
        {'usr': 'oca', 'repo': 'server-ux', 'branch': '11.0'},

    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent',
         'ver': '11.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '11.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ],
}

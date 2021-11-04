# -*- coding: utf-8 -*-
{
    'name': "wiku laundry",

    'summary': """
        WIKU LAUNDRY SYSTEM MANAGEMENT""",

    'description': """
        Ini adalah sistem wikulaundry
    """,

    'author': "My Company",
    'website': "http://srikandiart.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/wikulaundry_views.xml',
        'views/wikulaundry_caracuci.xml',
        'views/wikulaundry_ordercuci.xml',
        'views/wikulaundry_contact.xml',
        'views/wikulaundry_contact_pegawai.xml',
        'views/wikulaundry_bahanalatcuci.xml',
        'views/wikulaundry_daftarsupplier.xml',
        'views/wikulaundry_pembayaran.xml',
        'views/wikulaundry_akunting.xml',
        'views/templates.xml',
        'report/report.xml',
        'report/orderinvoice.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

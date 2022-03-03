# -*- coding: utf-8 -*-
{
    'name': "odoo_final_md",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/empresa_report.xml',
        'report/residencias_report.xml',
        'report/profesionales_salud_report.xml',
        'report/ancianos_report.xml',
        'report/factura_report.xml',
        'report/recibo_report.xml',
        'report/enfermeria_report.xml',
        'report/fisoterapia_report.xml',
        'report/servicios_limpieza_report.xml',
        'report/hospedaje_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

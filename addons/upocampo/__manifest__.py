# -*- coding: utf-8 -*-
{
    'name': "upocampo",

    'summary': """Gestion UPOCAMPO""",

    'description': """ Gestion de habitaciones, clientes, actividades, reserva, descuentos, inscripciones, empleados y puestos de trabajos.""",

    'author': "Grupo 3",
    'website': "https://github.com/jucargoe/upocampo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration/Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/reservas_views.xml',
        'views/descuentos_views.xml',
        'views/habitaciones_views.xml',
        'views/clientes_views.xml',
        'views/inscripciones_views.xml',
        'views/actividades_views.xml',
        'views/empleados_views.xml',
        'views/puestos_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}

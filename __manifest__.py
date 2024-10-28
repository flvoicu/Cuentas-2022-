# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cuentas',
    'version': '1.0',
    'category': 'Final',
    'description': "Modúlo para gestionar una cuenta",
    'summary': 'Gestión de cuentas',
    'sequence': 1,
    'depends': [
        'base',
    ],
    'data': [
        'vistas/cuentas_vistas.xml',
        'reports/report.xml',
        'security/ir.model.access.csv',
        'security/tools_security.xml'
        ],
    
    'installable': True,
    'application': True,
    
}

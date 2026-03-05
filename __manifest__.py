# -*- coding: utf-8 -*-
{
    'name': 'Sale Order - Project Field Layout',
    'version': '18.0.1.0.0',
    'summary': 'Mueve project_id debajo de client_order_ref en la orden de venta.',
    'category': 'Sales',
    'author': 'Mauro Bogado, Exemax',
    'depends': [
        'sale_stock',      # provee sale_stock_client_order_ref.view_order_form_client_order_ref
        'sale_project',    # provee sale_project.view_order_form_inherit_sale_project
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
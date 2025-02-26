{
    'name': 'Credit Request',
    'version': '1.0',
    'summary': 'Manage credit requests for contacts',
    'description': 'Module to manage credit requests for contacts',
    'author': 'Your Name',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/credit_request_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}
{
    'name': 'POS Ticket Modification',
    'version': '1.0',
    'summary': 'Custom modification for the POS ticket',
    'description': 'Add custom modifications to the POS ticket',
    'author': 'Your Name',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_ticket_modification.xml',
    ],
    'qweb': [
        'static/src/js/pos_ticket_modification.xml',
    ],
    'installable': True,
    'auto_install': False,
}

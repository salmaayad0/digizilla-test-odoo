{
    'name': 'digizilla_test',
    "description" : "digizilla is a software house",
    'version': '1.0',
    'author': 'salma ayad',
    'depends': ['base', 'web'],
    'data': ['reports/report.xml',
              'reports/digizilla_report.xml',
              'views/digizilla_view.xml',
              ],
    'qweb': [
        'static/src/xml/digizilla_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'test/static/js/custom.js',
        ],
    },
}
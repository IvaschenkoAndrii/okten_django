SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name':'Autorization',
            'in':'header'
        }
    },
    'USE_SESSION_AUTH':None
}

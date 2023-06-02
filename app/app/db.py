import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'plagioDjango',
        'USER': 'jaime',
        'PASSWORD': 'jaime1234',
        'HOST': 'localhost', # dirección IP del servidor de la base de datos
        'PORT': '3306', # el puerto que corresponda
    }
}
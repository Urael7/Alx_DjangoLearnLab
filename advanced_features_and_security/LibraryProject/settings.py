INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bookshelf',        # App containing CustomUser
    'relationship_app', # Other app
]

# Point to the correct app where CustomUser is defined
AUTH_USER_MODEL = 'bookshelf.CustomUser'
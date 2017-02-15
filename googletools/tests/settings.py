DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.sites',
    'googletools',
]

SECRET_KEY = 'secret'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
            ],
            'loaders': [
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

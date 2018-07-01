from .settings import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dashboard',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}

INSTALLED_APPS += [

    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
#
# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'CACHE': False,
#         'BUNDLE_DIR_NAME': '/dist/',#('/build/' if DEBUG else '/dist/'),
#         # 'BUNDLE_DIR_NAME': '/build/',#('/build/' if DEBUG else '/dist/'),
#         'STATS_FILE': os.path.join(settings.BASE_DIR, 'webpack-stats.json'),
#         # 'STATS_FILE': os.path.join(settings.BASE_DIR, 'webpack-stats-local.json'),
#     }
# }
#

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "astatic")
]

INTERNAL_IPS = '127.0.0.1'

from pathlib import Path
import os,sys
import django_heroku

django_heroku.settings(locals())
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-n!n*pn*ece+*v7j@f#+89@h%7)ly+jo$^*mn1pynx64)fb!w2z'


DEBUG = False


# icazer verdiyimiz IP
ALLOWED_HOSTS = ['https://pavshop.herokuapp.com']

AUTH_USER_MODEL = 'account.User'
# Application definition

INSTALLED_APPS = [
    'jet',
    'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about',
    'blog',
    'account',
    'home',
    'product',
    'contact',
    'social_django',
    'shop',
    'ckeditor',
  


]





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', 
    # yazdigimiz middleware register edirik
    'home.middleware.BlackListMiddleware',
    # 'shop.middleware.auth_middleware',

    # social auth
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'mydjangoproject.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # multi language
                'social_django.context_processors.backends',  # social auth
                'social_django.context_processors.login_redirect', # social auth
                'product.views.categories',
                'shop.context_processors.basket',
                'shop.context_processors.global_product_category',
                'django.template.context_processors.request',
            ],
        },
    },
]




JET_DEFAULT_THEME = 'green'
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]





WSGI_APPLICATION = 'mydjangoproject.wsgi.application'




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'shopdb',
#         'USER': 'admin',
#         'PASSWORD': '12345',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}




AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
  
)

AUTH_USER_MODEL = 'account.User'




from django.urls import reverse_lazy

LOGIN_URL = reverse_lazy('account:login')
LOGIN_REDIRECT_URL = reverse_lazy('home:index')
LOGOUT_URL = reverse_lazy('account:logout')
LOGOUT_REDIRECT_URL = reverse_lazy('account:login')

SOCIAL_AUTH_FACEBOOK_KEY='610447883549138'
SOCIAL_AUTH_FACEBOOK_SECRET = 'cb8a14986fe04f15217167830d21a5ad'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_friends']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields' : 'id,name,email,picture'
}



SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '96253623111-1hri97dnv1glth49i901jos51m9efoch.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'





CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'en-az'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


from django.utils.translation import gettext_lazy as _

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('az', ugettext('Azerbaijan')),
    ('ru', ugettext('Russian')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FROM_EMAIL = 'mirzeyevmehman2002@gmail.com'





EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# kimden email gedir
EMAIL_HOST_USER = 'mirzeyevmehman2002@gmail.com'
EMAIL_HOST_PASSWORD = 'tpjfrcyjdkyheyud'
# 1. gmailde security git
# 2. 2-terefli qoruma aktiv olmalidir
# 3 app passwords custom app yaradib kodu kopyala bura at
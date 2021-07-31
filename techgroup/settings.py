import os
from django.utils.translation import ugettext_lazy as _
import celery
from celery.schedules import crontab

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^167hsc-kan=mc_hyw4!!5*)2^j18_i+i%(_m$6(lb%y4z)0b_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'djcelery',
    'micro_admin',
    'pages',
    'micro_blog',
    'sorl.thumbnail',
    'search',
    'compressor',
    'django_simple_forum',
    'simple_pagination',
    'django_webpacker',
]

MIDDLEWARE = [
  'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'microsite.middleware.CountryMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'htmlmin.middleware.HtmlMinifyMiddleware',
    # 'htmlmin.middleware.MarkRequestMiddleware',
    'microsite.middleware.LowerCased',
    'microsite.middleware.RequestSessionMiddleware',
    'microsite.middleware.DetectMobileBrowser',
    'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = 'techgroup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
celery.setup_loader()
WSGI_APPLICATION = 'techgroup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    # ... your other backends
    'admin.auth_backend.PasswordlessAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]
    


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

COUNTRY_COOKIE_NAME = 'django_country'
COUNTRY_COOKIE_AGE = None
COUNTRY_COOKIE_DOMAIN = None
COUNTRY_COOKIE_PATH = '/'

LOCALE_PATHS = [BASE_DIR + '/locale', ]
    

LANGUAGES = [
    ('en', _('India')),
    ('us', _('US')),
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


USE_COUNTRY_URL = True

USE_TZ = False

LOGIN_URL = '/portal/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR + '/static',)

BLOG_IMAGES = BASE_DIR + '/static/blog/'
TEAM_IMAGES = BASE_DIR + '/static/team/'
CLIENT_IMAGES = BASE_DIR + '/static/client/'
TRAINER_IMAGES = BASE_DIR + '/static/trainer/'
COURSE_IMAGES = BASE_DIR + '/static/course/'
QACAT_IMAGES = BASE_DIR + '/static/qacategory/'

MEDIA_ROOT = BASE_DIR
SITE_BLOG_URL = "/blog/"
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + "/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
)

CELERY_TIMEZONE = "Asia/Calcutta"

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

CELERYBEAT_SCHEDULE = {
    # Executes every day evening at 5:00 PM GMT +5.30
    'run-every-sat-morning': {
        'task': 'micro_blog.tasks.report_on_blog_post_published_limit',
        'schedule': crontab(hour='10', minute='00', day_of_week='sat'),
    },
}

SG_USER = os.getenv('SGUSER') if os.getenv('SGUSER') else ''
SG_PWD = os.getenv('SGPWD') if os.getenv('SGPWD') else ''
SG_AUTHORIZATION = os.getenv('SGAUTHORIZATION') if os.getenv('SGAUTHORIZATION') else ''


GGL_URL_API_KEY = os.getenv('GGLAPIKEY') if os.getenv('GGLAPIKEY') else ''

GOOGLE_ANALYTICS_CODE = os.getenv('GOOGLE_ANALYTICS_CODE') if os.getenv('GOOGLE_ANALYTICS_CODE') else ''


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# ELASTICSEARCH_DEFAULT_ANALYZER = 'synonym_analyzer'

SITE_URL = "https://micropyramid.com"

if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, '/static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

query_cache_type = 0

# Haystack settings for Elasticsearch
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack_post',
        'TIMEOUT': 60,
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_DEFAULT_OPERATOR = 'OR'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

INTERNAL_IPS = ('127.0.0.1', 'localhost', '183.82.113.154')

# DEBUG_TOOLBAR_PATCH_SETTINGS = False
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     # 'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# CACHE_MIDDLEWARE_ALIAS = 'default'  # The cache alias to use for storage.
# CACHE_MIDDLEWARE_SECONDS = 10   # The number of seconds each page should be cached.
# CACHE_MIDDLEWARE_KEY_PREFIX = 'techgroup'
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
# CACHE_IGNORE_REGEXPS = (
#     r'/admin.*',
# )
SENTRY_ENABLED = False
if SENTRY_ENABLED:
    if os.getenv('SENTRYDSN') is not None:
        RAVEN_CONFIG = {
            'dsn': os.getenv('SENTRYDSN'),
        }
        INSTALLED_APPS = INSTALLED_APPS + (
            'raven.contrib.django.raven_compat',
        )
        MIDDLEWARE_CLASSES = [
          'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
          'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
        ] 
        MIDDLEWARE_CLASSES += MIDDLEWARE_CLASSES
        LOGGING = {
            'version': 1,
            'disable_existing_loggers': True,
            'root': {
                'level': 'WARNING',
                'handlers': ['sentry'],
            },
            'formatters': {
                'verbose': {
                    'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
                },
            },
            'handlers': {
                'sentry': {
                    'level': 'ERROR',
                    'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                },
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose'
                }
            },
            'loggers': {
                'django.db.backends': {
                    'level': 'ERROR',
                    'handlers': ['console'],
                    'propagate': False,
                },
                'raven': {
                    'level': 'DEBUG',
                    'handlers': ['console'],
                    'propagate': False,
                },
                'sentry.errors': {
                    'level': 'DEBUG',
                    'handlers': ['console'],
                    'propagate': False,
                },
            },
        }

# MODELTRANSLATION_DEFAULT_LANGUAGE='en'

# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# )

GP_CLIENT_ID = os.getenv('GPCLIENTID')
GP_CLIENT_SECRET = os.getenv('GPCLIENTSECRET')


WEB_PACK_FILES = [
    {'html_file_name': 'templates/site/base.html',
     'webpack_js': 'index',
    },
    {'html_file_name': 'templates/site/index.html',
     'webpack_js': 'index',
     },
    {'html_file_name': 'templates/admin/base.html',
     'webpack_js': 'portal',
     },
]


# ENABLE_DJANGO_WEBPACK_S3_STORAGES = False
# AWS_BUCKET_NAME = ''
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CAPTCHA_SECRET_KEY = os.getenv('CAPTCHASECRETKEY')
CAPTCHA_KEY = os.getenv('CAPTCHAKEY')
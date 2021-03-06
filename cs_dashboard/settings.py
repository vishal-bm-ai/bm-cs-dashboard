"""
Django settings for cs_dashboard project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
from datetime import timedelta, datetime
import socket

import dj_database_url
from celery.schedules import crontab
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3zrv5=&c+!5hm2v#!)h6e3$wvz@!)3*n)s)b1vxdjl(+!p#0fb'

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
    
    'django.contrib.postgres',
    'corsheaders',
    'rest_framework',
    'rest_framework_tracking',
    'drf_yasg',
    'django_prometheus',
    'bm_users',
    'bright_commons',
    'yodleeapp',
    'plaidapp',
    'finicityapp',
    'acroapp',
    'unifiedaccountagg',
    'unifiedaccountagg_events',
    'django_tables2',
    'django_admin_listfilter_dropdown',
    'admin_totals',
    'taggit',
    'subscriptions',
    'eventmanagementsystem',
    'credit',
    'paymentsscratch',
    # 'monetization',
    # 'twilioapp',
    'liability_manager',
    'paymentsfrontend',
    # 'monetization',
    # 'twilioapp',
    'inference',
    'nortridge',
    'driver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cs_dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cs_dashboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

db_backend_master_config = dj_database_url.parse(config('DATABASE_URL_BACKEND_MASTER'))
db_payments_config = dj_database_url.parse(config('DATABASE_URL_PAYMENTS'))
db_default_config = dj_database_url.parse(config('DATABASE_URL_DEFAULT'))


DATABASES = {
    'default': db_default_config,
}

# DATABASE_ROUTERS = ['cs_dashboard.router.AuthRouter','cs_dashboard.router.DBRouter']

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


PLAID_CLIENT_ID = config('PLAID_CLIENT_ID', default='')
PLAID_PUBLIC_KEY = config('PLAID_PUBLIC_KEY', default='')
PLAID_SECRET_SANDBOX = config('PLAID_SECRET_SANDBOX', default='')
PLAID_PRODUCTS = config('PLAID_PRODUCTS', default='')
PLAID_ENV = config('PLAID_ENV', default='')
PLAID_API_VERSION = config('PLAID_API_VERSION', default='')
PLAID_SECRET_DEVELOPMENT = config('PLAID_SECRET_DEVELOPMENT', default='')
PLAID_SECRET_PRODUCTION = config('PLAID_SECRET_PRODUCTION', default='')

# Used for Promethues & Checking for Non QA Env (say Payments)
DEPLOYMENT_ENV = config('DEPLOYMENT_ENV', default='')
CLUSTER = config('CLUSTER', default='')
STACK = config('STACK', default='')

LOCAL_TMP_DIR = config('LOCAL_TMP_DIR', default='')
S3_EMS_BUCKET = config('S3_EMS_BUCKET', default='')
EMS_URL = config('EMS_URL', default='')

MAX_PAYMENT_AMOUNT = int(config('MAX_PAYMENT_AMOUNT', default=2500))

# Secret used for Hash Generation of Action Link Data
LINK_ENCODING_SECRET = config('LINK_ENCODING_SECRET', default='')

KYC_CHECK_URL = config('KYC_CHECK_URL', default='')

PAYMENTS_ENDPOINT = config('PAYMENTS_ENDPOINT', default='')

# Secret used for internal service interactions which are sensitive in nature. TODO: Add Service RBAC
API_SECRET = config('API_SECRET', default='')

# LB For Backend Master
HYDRA_HOST = config('HYDRA_HOST', default='')

PAYMENT_CAMPAIGN_IDS = (config('PAYMENT_CAMPAIGN_IDS', default='')).split(',')

PAYMENTS_READ_ENDPOINT = config('PAYMENTS_READ_ENDPOINT', default='')

# Alerting
PAGER_DUTY_HOST = config('PAGER_DUTY_HOST', default='')
PAGER_DUTY_INTEGRATION_KEY = config('PAGER_DUTY_INTEGRATION_KEY', default='')

# Duplicate as SEND_OPT_ENDPOINT. TODO: Needs revision
EMAIL_ENDPOINT = config('EMAIL_ENDPOINT', default='')

DEFAULT_PAYMENT_EMAIL_RECIPIENTS = (config('DEFAULT_PAYMENT_EMAIL_RECIPIENTS', default='')).split(',')

LOGIN_HOST = config('LOGIN_HOST', default='')

DSI_VALIDITITY_IN_HOURS = config('DSI_VALIDITITY_IN_HOURS', default=24, cast=int)

DEBT_SUBSCRIPTION_LAUNCH_DATE_STR = config('DEBT_SUBSCRIPTION_LAUNCH_DATE', default='2019-12-13')
DEBT_SUBSCRIPTION_LAUNCH_DATE = datetime.strptime(DEBT_SUBSCRIPTION_LAUNCH_DATE_STR, "%Y-%m-%d").date()

DEBT_ADMIN_EMAILS = (config('DEBT_ADMIN_EMAILS', default='')).split(',')

SENDGRID_HOST = config('SENDGRID_HOST', default='')
SENDGRID_EV_API_KEY = config('SENDGRID_EV_API_KEY', default='')

ZENDESK_PASSWORD = config('ZENDESK_PASSWORD', default='')

EMS_DB_CONN_STRING = config('EMS_DB_CONN_STRING', default='')

MAX_PRIMARY_NUDGE_IMPRESSIONS = config('MAX_PRIMARY_NUDGE_IMPRESSIONS', default=2, cast=int)

YODLEE_REQUEST_VERIFY = config('YODLEE_REQUEST_VERIFY', default=True, cast=bool)

EFX_HOST = config('EFX_HOST', default='')
EFX_ID_CLINET_ID = config('EFX_ID_CLINET_ID', default='')
EFX_ID_CLIENT_SECRET = config('EFX_ID_CLIENT_SECRET', default='')
EFX_ID_MERCHANT_ID = config('EFX_ID_MERCHANT_ID', default='')
ACRO_LAMBDA_URL = config('ACRO_LAMBDA_URL', default='')
EFX_IG_CLINET_ID = config('EFX_IG_CLINET_ID', default='')
EFX_IG_CLIENT_SECRET = config('EFX_IG_CLIENT_SECRET', default='')
EFX_IG_MERCHANT_ID = config('EFX_IG_MERCHANT_ID', default='')
SSN_ENCRYPTION_SECRET = config('SSN_ENCRYPTION_SECRET', default='')
EFX_SOFT_PULL_MEMBER_NUMBER = config('EFX_SOFT_PULL_MEMBER_NUMBER', default='')
EFX_SOFT_PULL_SECRET_CODE = config('EFX_SOFT_PULL_SECRET_CODE', default='')
FORCE_REFRESH_LIMIT = config('FORCE_REFRESH_LIMIT', cast=bool,default=False)
RESERVE_BOX_URL = config('RESERVE_BOX_URL', default='')
CREDIT_ENDPOINT = config('CREDIT_ENDPOINT', default='')
P2C_URL = config('P2C_URL', default='')
GATEWAY_TASK_ENDPOINT = config('GATEWAY_TASK_ENDPOINT', default='')

CREDIT_BANNER_SIGNUP_HOUR_DIFF = config('CREDIT_BANNER_SIGNUP_HOUR_DIFF', default=1, cast=int)
DEBT_MANAGER_HOST = config('DEBT_MANAGER_HOST', default='')
DEBT_MANAGER_ENDPOINT = config('DEBT_MANAGER_ENDPOINT', default='')

USER_STATE_QUEUE = config('USER_STATE_QUEUE', default='gateway_bm_users')
USER_NOTIFICATIONS_QUEUE = config('USER_NOTIFICATIONS_QUEUE', default='gateway_bm_users')
USER_ACCOUNTS_QUEUE = config('USER_ACCOUNTS_QUEUE', default='gateway_unifiedaccountagg_user_linked_accounts')
USER_ACCOUNTS_TOP_N_TXN_QUEUE = config('USER_ACCOUNTS_TOP_N_TXN_QUEUE', default='gateway_unifiedaccountagg_transactions')
USER_PREFERENCES_QUEUE = config('USER_PREFERENCES_QUEUE', default='gateway_bm_users')
ALSM_STATE_QUEUE = config('ALSM_STATE_QUEUE', default='gateway_unifiedaccountagg_alsm')
USER_PROFILE_QUEUE = config('USER_PROFILE_QUEUE', default='gateway_bm_users')
USER_BRIGHT_SMART_ACCOUNT_CONFIG_QUEUE = config('USER_BRIGHT_SMART_ACCOUNT_CONFIG_QUEUE', default='gateway_bm_users')
USER_SUBSCRIPTION_STATE_QUEUE = config('USER_SUBSCRIPTION_STATE_QUEUE', default='gateway_subscriptions_state')
USER_DEBT_MANAGEMENT_SUMMARY_QUEUE = config('USER_DEBT_MANAGEMENT_SUMMARY_QUEUE', default='gateway_subscriptions_summary')
PAYMENTS_QUEUE=config('PAYMENTS_QUEUE', default='gateway_paymentsscratch_payment')

LAST_ACTIVE_SESSION_THRESHOLD_DAYS = config('LAST_ACTIVE_SESSION_THRESHOLD_DAYS', default=7, cast=int)


PRIVATE_KEY_DEV = get_private_key(config('PRIVATE_KEY_PATH_DEV', default='')) if config('PRIVATE_KEY_PATH_DEV', default='')!='' else None
PRIVATE_KEY_PROD = get_private_key(config('PRIVATE_KEY_PATH_PROD', default='')) if config('PRIVATE_KEY_PATH_PROD', default='')!='' else None

ISSUER_ID_DEV = config('ISSUER_ID_DEV', default='')
ISSUER_ID_PROD = config('ISSUER_ID_PROD', default='')

YODLEE_ENVIRONMENT_DEV = config('YODLEE_ENVIRONMENT_DEV', default='')
YODLEE_ENVIRONMENT_PROD = config('YODLEE_ENVIRONMENT_PROD', default='')

VALUE_ENGINE_HOST = config('VALUE_ENGINE_HOST', default='')

VALUE_ENGINE_SWITCH_RISK_SERVICE = config("VALUE_ENGINE_SWITCH_RISK_SERVICE", cast=bool,default=False)

FIREBASE_ADD_FCM = config('FIREBASE_ADD_FCM', default='')
FIREBASE_HOST = config('FIREBASE_HOST', default='')

FIREBASE_CRED_PATH = os.path.join(BASE_DIR, config('FIREBASE_CRED_PATH', default='')) if config('FIREBASE_CRED_PATH', default='')!='' else ''
SENDER_UID = config("SENDER_UID", default='')
SEND_OPT_ENDPOINT = config("SEND_OPT_ENDPOINT", default='')

SINGLE_USER_TEST = config('SINGLE_USER_TEST', cast=bool, default=False)
SINGLE_USER_NAME = config('SINGLE_USER_NAME', default='')
SINGLE_USER_EMAIL = config('SINGLE_USER_EMAIL', default='')

CELERY_BROKER_URL = 'amqp://localhost'
UNIFIED_TRIGGER = config('UNIFIED_TRIGGER', cast=bool, default=True)

API_TESTING = config("API_TESTING", cast=bool, default=False)

DEBUG_LOGGER_DJANGO = 'django'
DEBUG_LOGGER_USER = "user"
DEBUG_CELERY_USER = "celery"
DEBUG_LOGGER_YODLEE = "yodlee"
DEBUG_LOGGER_UNIFIED = "unifiedaccountagg"
PAYMENTS_LOGGER = 'payments'

MACHINE_NAME = socket.gethostname()
SEGMENT_WRITE_KEY = config('SEGMENT_WRITE_KEY', default='')
NOTIFICATION_ENDPOINT = config('NOTIFICATION_ENDPOINT',default='')
EVOLVE_SFTP_INSTANCE_AWS_USER_AND_IP = config('EVOLVE_SFTP_INSTANCE_AWS_USER_AND_IP', default='')
EMS_ENDPOINT = config('EMS_ENDPOINT', default='')
EVOLVE_SFTP_INSTANCE_ID = config('EVOLVE_SFTP_INSTANCE_ID', default='')
EVOLVE_SFTP_INSTANCE_AWS_ZONE = config('EVOLVE_SFTP_INSTANCE_AWS_ZONE', default='')
EMS_SENDER_ID = config('EMS_SENDER_ID', default='')
PATH_TO_PUBLIC_KEY = config('PATH_TO_PUBLIC_KEY', default='')
PATH_TO_EVOLVE_SFTP_PUBLIC_KEY = config('PATH_TO_EVOLVE_SFTP_PUBLIC_KEY', default='')

BACKEND_FUSION_ENDPOINT = config('BACKEND_FUSION_ENDPOINT', default='')
BACKEND_ENDPOINT = config('BACKEND_ENDPOINT', default='')
BACKEND_FUSION_APP_VERSION = config('BACKEND_FUSION_APP_VERSION', default='')

INTEGRATION_WITH_BACKEND = config('INTEGRATION_WITH_BACKEND', cast=bool, default=True)
ENABLE_P2C_CHECK = config('ENABLE_P2C_CHECK', cast=bool, default=True)

YODLEE_ISSUER_ID_DEV = config('YODLEE_ISSUER_ID_DEV', default='')
YODLEE_PRIVATE_KEY_PATH_DEV = config('YODLEE_PRIVATE_KEY_PATH_DEV', default='')
YODLEE_DEV_ENDPOINT = config('YODLEE_DEV_ENDPOINT', default='')

YODLEE_ISSUER_ID_PROD = config('YODLEE_ISSUER_ID_PROD', default='')
YODLEE_PRIVATE_KEY_PATH_PROD = config('YODLEE_PRIVATE_KEY_PATH_PROD', default='')
YODLEE_PROD_ENDPOINT = config('YODLEE_PROD_ENDPOINT', default='')

FINICITY_APP_KEY = config('FINICITY_APP_KEY', default='')
FINICITY_PARTNER_SECRET = config('FINICITY_PARTNER_SECRET', default='')
FINICITY_PARTNER_ID = config('FINICITY_PARTNER_ID', default='')

PAGER_DUTY_HOST = config('PAGER_DUTY_HOST', default='')
PAGER_DUTY_INTEGRATION_KEY = config('PAGER_DUTY_INTEGRATION_KEY', default='')
FED_ACH_ROUTING_DIR_URL = config('FED_ACH_ROUTING_DIR_URL', default='')
FED_ACH_DIR_DOWNLOAD_CODE = config('FED_ACH_DIR_DOWNLOAD_CODE', default='')

RISK_SERVICE_URL = config('RISK_SERVICE_URL', default='')
TABAPAY_P2C_TRANSACTIONS_DIRECTORY = config('TABAPAY_P2C_TRANSACTIONS_DIRECTORY', default='/tmp/')

TABAPAY_REPORTS_BUCKET_NAME = config('TABAPAY_REPORTS_BUCKET_NAME', default='brightmoney-tabapay-reports')
EVOLVE_ACCOUNT_ACTIVITY_DIRECTORY = config('EVOLVE_ACCOUNT_ACTIVITY_DIRECTORY', default='/tmp/')

PAYMENTS_FRONTEND_ENDPOINT = config('PAYMENTS_FRONTEND_ENDPOINT', default='')
USER_REPORTS_DIRECTORY = config('USER_REPORTS_DIRECTORY', default='')
PAYMENTS_BUCKET = config('PAYMENTS_BUCKET', default='brightmoney-payments')

SUBMIT_PAYMENT_API_SECRET = config('SUBMIT_PAYMENT_API_SECRET', default='')

GATEWAY_TASK_TRIGGER_URL = config('GATEWAY_TASK_TRIGGER_URL', default='')

VALUE_ENGINE_URL = config('VALUE_ENGINE_URL', default='')
BACKEND_URL = config('BACKEND_URL', default='')
RETURNS_DIRECTORY = config('RETURNS_DIRECTORY', default='/tmp/')

BRIGHT_ACCOUNT_UPDATE_QUEUE = config('BRIGHT_ACCOUNT_UPDATE_QUEUE', default='')
PAYMENT_UPDATE_QUEUE = config('PAYMENT_UPDATE_QUEUE', default='')
NACHA_BASE_DIR = config('NACHA_BASE_DIR', default='/tmp')

S3_EMS_BUCKET = config('S3_EMS_BUCKET', default='bill-dev-test')
CONTACT_NUMBER_OFFSET = config('CONTACT_NUMBER_OFFSET', default=0)
LOAN_NUMBER_OFFSET = config('LOAN_NUMBER_OFFSET', default=0)

DATABASE_URL = config('DATABASE_URL', default='postgres://postgres:vishal@localhost:5432/')

AUTH_USER_MODEL = 'bm_users.BrightUser'
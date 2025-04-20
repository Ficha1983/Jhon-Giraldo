
# Django settings for django_db_project

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-1#%=wht!8!z&8z5d(yys_27d==1!3e9'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Agregar aplicaciones específicas de la base de datos
    'django.contrib.postgres', # Para PostgreSQL
    'rest_framework',  # Django Rest Framework
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

ROOT_URLCONF = 'django_db_project.urls'

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

WSGI_APPLICATION = 'django_db_project.wsgi.application'

# MySQL Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fiche3066478',  # Nombre de tu base de datos
        'USER': '',  # Tu nombre de usuario de MySQL
        'PASSWORD': 'Jesucristo0728@',  # Tu contraseña de MySQL
        'HOST': 'localhost',  # Cambia si usas un servidor remoto
        'PORT': '3306',  # El puerto predeterminado de MySQL
    }
}

# PostgreSQL Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fiche3066478',  # Nombre de tu base de datos
        'USER': 'postgres',  # Tu nombre de usuario de PostgreSQL
        'PASSWORD': 'Jesucristo0728@',  # Tu contraseña de PostgreSQL
        'HOST': 'localhost',  # Cambia si usas un servidor remoto
        'PORT': '5432',  # El puerto predeterminado de PostgreSQL
    }
}


# MongoDB Configuration using Djongo
DATABASES['mongodb'] = {
    'ENGINE': 'djongo',
    'NAME': 'fiche3066478', # Nombre de tu base de datos
    'CLIENT': {
        'host': 'mongodb://localhost:27017', # Cambia si usas un servidor remoto o autenticación
    }
}

# Password validation
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

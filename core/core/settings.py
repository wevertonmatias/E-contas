import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'io16obt1dv%qr2!3wix52z2-(gckfohx(ky*@bjmkmg0s-wbov'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'E_contas',
    'baton.autodiscover',
    'bootstrap',
    'easy_pdf',
    'bootstrapform',
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

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'static'
]

# CONFIGURAÇÕES PERSONALIZADAS
DATE_INPUT_FORMATS = ['%d/%m/%Y']
# CONFIGURAÇÕES DO ADM-BATON

BATON = {
    'SITE_HEADER': 'E-Contas',
    'SITE_TITLE': 'E-Contas',
    'INDEX_TITLE': 'E-Contas Administração',
    'SUPPORT_HREF': 'http://127.0.0.1:8000/econtas/contato',
    'COPYRIGHT': 'copyright © 2019 <a href="http://127.0.0.1:8000/econtas/contato">E-Contas S.A </a>',  # noqa
    'POWERED_BY': '<a href="https://github.com/wevertonmatias">Weverton Matias</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'MENU': (
        {'type': 'title', 'label': 'main', 'apps': ('auth',)},
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        {'type': 'title', 'label': 'Contents', 'apps': ('flatpages',)},
        {'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages'},
        {'type': 'free', 'icon': 'fas fa-print', 'label': 'Relatórios', 'url': 'http://127.0.0.1:8000/econtas/adm/relatorio/'},
        {'type': 'free', 'icon': 'fas fa-chart-pie', 'label': 'Gráfico', 'url': 'http://127.0.0.1:8000/econtas/adm/grafico/'},
        {'type': 'free', 'icon': 'fas fa-plus-circle', 'label': 'Cadastrar', 'children': [
            {'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp', 'icon': 'fa fa-gavel'},
            {'type': 'free', 'label': 'Vendas', 'url': ''},
            {'type': 'free', 'label': 'Pagamentos', 'url': ''},
            {'type': 'free', 'label': 'Empresas', 'url': 'http://127.0.0.1:8000/econtas/adm/cadastro/empresa/'},
            {'type': 'free', 'label': 'Fornecedores', 'url': ''},
            {'type': 'free', 'label': 'Cidades', 'url': ''},
            {'type': 'free', 'label': 'Estados', 'url': ''},
            {'type': 'free', 'label': 'Local de Pagamento', 'url': ''},
            {'type': 'free', 'label': 'Status do Pagamento', 'url': ''},
        ]},
        {'type': 'free', 'icon': 'fas fa-edit', 'label': 'Listar/Atualizar/Deletar', 'children': [
            {'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp', 'icon': 'fa fa-gavel'},
            {'type': 'free', 'label': 'Vendas', 'url': ''},
            {'type': 'free', 'label': 'Pagamentos', 'url': ''},
            {'type': 'free', 'label': 'Empresas', 'url': 'http://127.0.0.1:8000/econtas/adm/lista/empresa/'},
            {'type': 'free', 'label': 'Fornecedores', 'url': ''},
            {'type': 'free', 'label': 'Cidades', 'url': ''},
            {'type': 'free', 'label': 'Estados', 'url': ''},
            {'type': 'free', 'label': 'Local de Pagamento', 'url': ''},
            {'type': 'free', 'label': 'Status do Pagamento', 'url': ''},
        ]},

    ),
    'ANALYTICS': {
        'CREDENTIALS': os.path.join(BASE_DIR, 'credentials.json'),
        'VIEW_ID': '12345678',
    }
}

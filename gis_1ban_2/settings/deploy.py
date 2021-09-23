from .base import *

def read_secrets(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secrets('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG가 True이면 디버그 메세지를 모두 출력
# 개발과정에서 필요하나 배포과정에서는 출력할 필요없음
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secrets('MARIADB_USER'),
        'PASSWORD': read_secrets('MARIADB_PASSWORD'),
        # 'HOST'는 mariadb container의 이름과 동일
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
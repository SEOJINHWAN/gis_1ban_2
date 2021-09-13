from .base import *

env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')

    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

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
        'USER': 'django',
        'PASSWORD': '1q2w3e4r!',
        # 'HOST'는 mariadb container의 이름과 동일
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
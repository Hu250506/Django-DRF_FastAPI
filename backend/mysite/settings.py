from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# INSTALLED_APPS = [
#     # DRF
#     "rest_framework",

#     # apps
#     "apps.accounts",
#     "apps.products",
#     "apps.reviews",
#     "apps.interactions",
#     "apps.ai_gateway",
# ]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # DRF
    "rest_framework",

    # apps
    "apps.accounts",
    "apps.products",
    "apps.reviews",
    "apps.interactions",
    "apps.ai_gateway",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
AUTH_USER_MODEL = "accounts.User"

# 이미지 업로드 파일 접근 경로  
MEDIA_URL = "/media/"   
# 실제 업로드 파일 저장 폴더  
MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = "/static/"  
STATICFILES_DIRS = [BASE_DIR / "static"]

SECRET_KEY = "django-insecure-개발용-아무문자열이나-길게"

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = "mysite.urls"
WSGI_APPLICATION = "mysite.wsgi.application"
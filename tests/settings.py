import os

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "payments_portmone"))
TEMPLATES = [
    {"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [os.path.join(PROJECT_ROOT, "templates")]}
]

SECRET_KEY = "empty"
PAYMENT_HOST = "example.com"


INSTALLED_APPS = ["django.contrib.contenttypes", "payments", "payments_portmone"]

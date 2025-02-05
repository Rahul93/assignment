from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Use console for email backend in development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
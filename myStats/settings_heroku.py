from .settings import *
import django_heroku

django_heroku.settings(locals())


DEBUG = False

# To be completed only with the deploy server
# ALLOWED_HOSTS = []

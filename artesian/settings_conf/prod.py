from artesian.settings_conf.base import *
# run this command to check deployment security checklist 'django-admin check --deploy'

DEBUG = False

# its not recommended to use wild card *, but for now let it be.
ALLOWED_HOSTS = ['*']

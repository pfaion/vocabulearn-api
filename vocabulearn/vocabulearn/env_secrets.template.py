# This file stores sensitive information that should not get synced to public code repositories. It
# also allows for running different configurations between local debugging vs production. You can
# either copy this file to 'env_secrets.py' and fill in the empty values, or define local
# environment variables in the same fashion. The application will look for the 'env_secrets.py'
# first.

secrets = dict(
    # your django secret key
    SECRET_KEY='',
    # you probably want that to be 1 for local debugging, 0 for actual production
    DJANGO_DEBUG=1,
    # your database url (postgresql)
    DATABASE_URL='',
    # leave empty for local debugging (when DJANGO_DEBUG=1), actual hostname otherwise
    ALLOWED_HOSTS='',
)

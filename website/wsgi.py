"""
WSGI config for locallibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/

-----------------------------------------------------------------------
Bu dosya Django uygulamasinin web sunucusu ile haberlesmesini sagliyor.
-----------------------------------------------------------------------
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")

application = get_wsgi_application()

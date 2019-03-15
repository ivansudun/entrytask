"""
WSGI config for entrytask project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os,sys
from os.path import join,dirname,abspath
sys.path.insert(0,dirname(dirname(abspath(__file__))))
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entrytask.settings")

application = get_wsgi_application()

import os
import sys

path = '/var/www/detour'
if path not in sys.path:
    sys.path.append(path)
    sys.path.append(path + "/detour_news")

os.environ['DJANGO_SETTINGS_MODULE'] = 'detour_news.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

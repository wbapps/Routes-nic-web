#!/usr/bin/python
import sys
import os
import site
 
BASE_DIR = os.path.join(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

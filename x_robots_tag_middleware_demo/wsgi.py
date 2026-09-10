"""WSGI config for the demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "x_robots_tag_middleware_demo.settings")

application = get_wsgi_application()

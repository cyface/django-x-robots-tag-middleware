"""ASGI config for the demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "x_robots_tag_middleware_demo.settings")

application = get_asgi_application()

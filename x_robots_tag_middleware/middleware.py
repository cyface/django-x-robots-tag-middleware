"""Django X-Robots-Tag Middleware"""

from django.conf import settings
import logging

LOGGER = logging.getLogger(name='x_robots_tag_middleware')


class XRobotsTagMiddleware(object):
    """Adds X-Robots-Tag Based on Settings"""

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        LOGGER.debug('x_robots_tag_middleware')
        response = self.get_response(request)

        if settings.X_ROBOTS_TAG:
            response['X-Robots-Tag'] = ','.join(settings.X_ROBOTS_TAG)
            LOGGER.debug('x_robots_tag_middleware.x_robots_tag: ' + ','.join(settings.X_ROBOTS_TAG))

        return response


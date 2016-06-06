"""Django X-Robots-Tag Middleware"""

from django.conf import settings
import logging

LOGGER = logging.getLogger(name='x_robots_tag_middleware')


class XRobotsTagMiddleware(object):
    """Adds X-Robots-Tag Based on Settings"""

    def process_response(self, request, response):
        """
            Adds X-Robots Tag to Response Base on X_ROBOTS_TAG setting, which should be a list of values for the header.
            Value Options here: https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag?hl=en#using-the-x-robots-tag-http-header
        """

        LOGGER.debug('x_robots_tag_middleware')

        if settings.X_ROBOTS_TAG:
            response['X-Robots-Tag'] = ','.join(settings.X_ROBOTS_TAG)
            LOGGER.debug('x_robots_tag_middleware.x_robots_tag: ' + ','.join(settings.X_ROBOTS_TAG))

        return response

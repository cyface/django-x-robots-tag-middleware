"""Django X-Robots-Tag Middleware"""

from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class XRobotsTagMiddleware(object):
    """Adds X-Robots-Tag Based on Settings"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.debug("x_robots_tag_middleware")
        response = self.get_response(request)

        if settings.X_ROBOTS_TAG:
            response["X-Robots-Tag"] = ",".join(settings.X_ROBOTS_TAG)
            logger.debug(f"x_robots_tag: {settings.X_ROBOTS_TAG}")

        return response

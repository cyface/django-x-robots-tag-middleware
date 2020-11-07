from django.test import TestCase, override_settings
import logging

logger = logging.getLogger(__name__)


class XRobotsMiddlewareTests(TestCase):
    """Tests Terms and Conditions Module"""

    def test_middleware(self):
        """
        Validate that a middleware sets X-Robots-Tag
        Depends on settings and setup in the _demo project
        """

        logger.debug("Test Middleware")
        response = self.client.get("/")
        self.assertIn("x-robots-tag", response._headers)
        self.assertEqual(
            response._headers.get("x-robots-tag", ""),
            ("X-Robots-Tag", "noindex,nofollow"),
        )

    @override_settings(X_ROBOTS_TAG=None)
    def test_middleware_no_setting(self):
        """
        Validate that a middleware sets X-Robots-Tag
        Depends on settings and setup in the _demo project
        """

        logger.debug("Test Middleware No Setting")
        response = self.client.get("/")
        self.assertNotIn("x-robots-tag", response._headers)
        self.assertContains(response, "This is the test page!")

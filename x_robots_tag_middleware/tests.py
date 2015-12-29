from django.test import TestCase
import logging

LOGGER = logging.getLogger(name='x_robots_tag_middleware')


class XRobotsMiddlewareTests(TestCase):
    """Tests Terms and Conditions Module"""

    def test_middleware(self):
        """
            Validate that a middleware sets X-Robots-Tag
            Depends on settings and setup in the _demo proj
        """

        LOGGER.debug('Test Middleware')
        response = self.client.get('/')
        self.assertIn('x-robots-tag', response._headers)
        self.assertEqual(response._headers.get('x-robots-tag', ''), ('X-Robots-Tag', 'noindex,nofollow'))

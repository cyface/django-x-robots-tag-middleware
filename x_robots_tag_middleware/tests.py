"""Tests for the X-Robots-Tag middleware."""

from django.conf import settings
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings

from x_robots_tag_middleware.middleware import XRobotsTagMiddleware


class XRobotsTagMiddlewareTests(SimpleTestCase):
    """Exercises the middleware through the demo project's settings and URLs."""

    def test_header_added(self):
        """The header is built from the list in the demo settings."""
        response = self.client.get("/")
        self.assertEqual(response.headers["X-Robots-Tag"], "noindex,nofollow")
        self.assertContains(response, "This is the test page!")

    def test_header_lookup_is_case_insensitive(self):
        """``response.headers`` is case-insensitive, as HTTP headers are."""
        response = self.client.get("/")
        self.assertEqual(response.headers["x-robots-tag"], "noindex,nofollow")

    @override_settings(X_ROBOTS_TAG=["noarchive"])
    def test_header_uses_current_setting(self):
        """The header reflects the setting at request time."""
        response = self.client.get("/")
        self.assertEqual(response.headers["X-Robots-Tag"], "noarchive")

    @override_settings(X_ROBOTS_TAG="noindex, nofollow")
    def test_setting_may_be_a_string(self):
        """A plain string setting is passed through unchanged."""
        response = self.client.get("/")
        self.assertEqual(response.headers["X-Robots-Tag"], "noindex, nofollow")

    @override_settings(X_ROBOTS_TAG=None)
    def test_no_header_when_setting_is_none(self):
        response = self.client.get("/")
        self.assertNotIn("X-Robots-Tag", response.headers)
        self.assertContains(response, "This is the test page!")

    @override_settings(X_ROBOTS_TAG=[])
    def test_no_header_when_setting_is_empty(self):
        response = self.client.get("/")
        self.assertNotIn("X-Robots-Tag", response.headers)

    def test_no_header_when_setting_is_absent(self):
        """A project that never defines ``X_ROBOTS_TAG`` still works."""
        with self.settings():
            del settings.X_ROBOTS_TAG
            response = self.client.get("/")
        self.assertNotIn("X-Robots-Tag", response.headers)
        self.assertContains(response, "This is the test page!")


class XRobotsTagMiddlewareAsyncTests(SimpleTestCase):
    """The middleware must work natively under ASGI as well as WSGI."""

    async def test_header_added_via_async_client(self):
        response = await self.async_client.get("/")
        self.assertEqual(response.headers["X-Robots-Tag"], "noindex,nofollow")

    @override_settings(X_ROBOTS_TAG=None)
    async def test_no_header_via_async_client(self):
        response = await self.async_client.get("/")
        self.assertNotIn("X-Robots-Tag", response.headers)

    def test_sync_get_response_stays_sync(self):
        """A sync ``get_response`` must not make the middleware awaitable."""
        middleware = XRobotsTagMiddleware(lambda request: HttpResponse())
        self.assertFalse(middleware.async_mode)

    async def test_async_get_response_is_adapted(self):
        """An async ``get_response`` puts the middleware in async mode."""

        async def get_response(request):
            return HttpResponse()

        middleware = XRobotsTagMiddleware(get_response)
        self.assertTrue(middleware.async_mode)
        response = await middleware(None)
        self.assertEqual(response.headers["X-Robots-Tag"], "noindex,nofollow")

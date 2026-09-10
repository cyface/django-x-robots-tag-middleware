"""Django X-Robots-Tag Middleware."""

from __future__ import annotations

import logging
from collections.abc import Awaitable, Callable
from typing import TypeAlias

from asgiref.sync import iscoroutinefunction, markcoroutinefunction
from django.conf import settings
from django.http import HttpRequest, HttpResponseBase

logger = logging.getLogger(__name__)

GetResponse: TypeAlias = (
    Callable[[HttpRequest], HttpResponseBase]
    | Callable[[HttpRequest], Awaitable[HttpResponseBase]]
)

HEADER_NAME = "X-Robots-Tag"


class XRobotsTagMiddleware:
    """Adds the ``X-Robots-Tag`` header to every response, based on settings.

    The header value comes from the ``X_ROBOTS_TAG`` setting, which may be a
    string (``"noindex, nofollow"``) or an iterable of directives
    (``["noindex", "nofollow"]``). When the setting is missing or empty, no
    header is added.

    Works under both WSGI and ASGI.
    """

    sync_capable = True
    async_capable = True

    def __init__(self, get_response: GetResponse) -> None:
        self.get_response = get_response
        self.async_mode = iscoroutinefunction(get_response)
        if self.async_mode:
            # Tell Django this instance is awaitable so it is not run in a
            # thread pool under ASGI.
            markcoroutinefunction(self)

    def __call__(
        self, request: HttpRequest
    ) -> HttpResponseBase | Awaitable[HttpResponseBase]:
        if self.async_mode:
            return self.__acall__(request)
        response = self.get_response(request)
        return self.process_response(response)

    async def __acall__(self, request: HttpRequest) -> HttpResponseBase:
        response = await self.get_response(request)
        return self.process_response(response)

    def process_response(self, response: HttpResponseBase) -> HttpResponseBase:
        """Set the ``X-Robots-Tag`` header on the response, if configured."""
        header_value = self.get_header_value()
        if header_value:
            response.headers[HEADER_NAME] = header_value
            logger.debug("%s: %s", HEADER_NAME, header_value)
        return response

    @staticmethod
    def get_header_value() -> str:
        """Build the header value from the ``X_ROBOTS_TAG`` setting."""
        x_robots_tag = getattr(settings, "X_ROBOTS_TAG", None)
        if not x_robots_tag:
            return ""
        if isinstance(x_robots_tag, str):
            return x_robots_tag
        return ",".join(x_robots_tag)

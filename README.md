Django X-Robots-Tag Middleware
===============================

[![PyPi Package Version](https://badge.fury.io/py/django-x-robots-tag-middleware.svg)](http://badge.fury.io/py/django-x-robots-tag-middleware) ![Python package](https://github.com/cyface/django-x-robots-tag-middleware/workflows/Python%20package/badge.svg) [![codecov](https://codecov.io/gh/cyface/django-x-robots-tag-middleware/branch/master/graph/badge.svg?token=RvtjZ2bngZ)](https://codecov.io/gh/cyface/django-x-robots-tag-middleware)

Simple Django middleware to send the ``X-Robots-Tag`` header to all URLs.  Useful for ensuring a site in development is not accidentally picked up and indexed until it is ready.

Installation
------------

From [pypi](https://pypi.python.org):

    $ pip install django-x-robots-tag-middleware

Usage
-----

1. Add ``"x_robots_middleware.XRobotsMiddleware",`` to your middleware list in settings.py.

2. Add ``X_ROBOTS_TAG = ["noindex", "nofollow"]`` to your settings.py with the values you want for the X_ROBOTS_TAG.

Details about the values for the tag and what they do can be found [in the Google Documentation](https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag?hl=en#using-the-x-robots-tag-http-header).


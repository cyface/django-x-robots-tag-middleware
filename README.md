django-x-robots-middleware
===============================

[![PyPi Version](https://badge.fury.io/py/django-x-robots-tag-middleware.svg)](http://badge.fury.io/py/django-x-robots-tag-middleware)

[![Travis CI Build](https://travis-ci.org/cyface/django-x-robots-tag-middleware.svg?branch=master)](https://travis-ci.org/cyface/django-x-robots-tag-middleware)

[![Coveralls Code Coverage](https://coveralls.io/repos/cyface/django-x-robots-tag-middleware/badge.svg?branch=master&service=github)](https://coveralls.io/github/cyface/django-x-robots-tag-middleware?branch=master)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/cyface/django-x-robots-tag-middleware/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/cyface/django-x-robots-tag-middleware/?branch=master)

Simple Django middleware to use the ``X-Robots-Tag`` header based on a config param.

Installation
------------

From `pypi <https://pypi.python.org>`_::

    $ pip install django-x-robots-tag-middleware

or::

    $ easy_install django-x-robots-tag-middleware

or clone from `github <http://github.com>`_::

    $ git clone git://github.com/cyface/django-x-robots-tag-middleware.git


Usage
-----

Just add ``x_robots_middleware.XRobotsMiddleware`` to your middleware.

And add this config param:

``X_ROBOTS_TAG = ['noindex','nofollow']``

Details about the values for the tag and what they do can be found `in the Google Documentation <https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag?hl=en#using-the-x-robots-tag-http-header>`_.


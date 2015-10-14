===============================
django-x-robots-middleware
===============================

.. image:: https://badge.fury.io/py/django-x-robots-middleware.svg
    :target: http://badge.fury.io/py/django-x-robots-middleware

.. image:: https://travis-ci.org/cyface/django-x-robots-middleware.svg?branch=master
    :target: https://travis-ci.org/cyface/django-x-robots-middleware

.. image:: https://coveralls.io/repos/cyface/django-x-robots-middleware/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/cyface/django-x-robots-middleware?branch=master

Simple Django middleware to use the ``X-Robots-Tag`` header based on a config param.

Installation
------------

From `pypi <https://pypi.python.org>`_::

    $ pip install django-x-robots-middleware

or::

    $ easy_install django-x-robots-middleware

or clone from `github <http://github.com>`_::

    $ git clone git://github.com/cyface/django-x-robots-middleware.git


Usage
-----

Just add ``x_robots_middleware.XRobotsMiddleware`` to your middleware.

And add this config param:

``X_ROBOTS_TAG = ['noindex','nofollow']``

Details about the values for the tag and what they do can be found `In the Google Documentation <https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag?hl=en#using-the-x-robots-tag-http-header>`_.


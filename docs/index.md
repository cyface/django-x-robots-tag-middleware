Simple Django middleware to use the ``X-Robots-Tag`` header based on a config param.

## Installation

From [PyPi](https://pypi.python.org):

    $ pip install django-x-robots-tag-middleware

or:

    $ easy_install django-x-robots-tag-middleware

or clone from [GitHub](http://github.com):

    $ git clone git://github.com/cyface/django-x-robots-tag-middleware.git


## Usage

1. Add ``'x_robots_middleware.XRobotsMiddleware',`` to your middleware list in settings.py.

2. Add ``X_ROBOTS_TAG = ['noindex','nofollow']`` to your settings.py with the settings you want for the X_ROBOTS_TAG.

Details about the values for the tag and what they do can be found [in the Google Documentation](https://developers.google.com/webmasters/control-crawl-index/docs/robots_meta_tag?hl=en#using-the-x-robots-tag-http-header).

## Dependencies
* Django >= 1.8
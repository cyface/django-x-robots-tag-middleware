# Django X-Robots-Tag Middleware

[![PyPi Package Version](https://badge.fury.io/py/django-x-robots-tag-middleware.svg)](https://badge.fury.io/py/django-x-robots-tag-middleware) [![Python package](https://github.com/cyface/django-x-robots-tag-middleware/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/cyface/django-x-robots-tag-middleware/actions/workflows/python-package.yml) [![codecov](https://codecov.io/gh/cyface/django-x-robots-tag-middleware/branch/main/graph/badge.svg?token=RvtjZ2bngZ)](https://codecov.io/gh/cyface/django-x-robots-tag-middleware)

Simple Django middleware to send the `X-Robots-Tag` header on all responses. Useful for
ensuring a site in development is not accidentally picked up and indexed until it is ready.

Works under both WSGI and ASGI, and is fully type annotated.

## Requirements

- Python 3.10+
- Django 5.2+

## Installation

From [PyPI](https://pypi.org/project/django-x-robots-tag-middleware/):

```console
$ python -m pip install django-x-robots-tag-middleware
```

## Usage

1. Add the middleware to `MIDDLEWARE` in your `settings.py`:

   ```python
   MIDDLEWARE = [
       # ...
       "x_robots_tag_middleware.middleware.XRobotsTagMiddleware",
   ]
   ```

2. Add `X_ROBOTS_TAG` to your `settings.py` with the directives you want:

   ```python
   X_ROBOTS_TAG = ["noindex", "nofollow"]
   ```

   The setting may be a list of directives (joined with commas) or a plain string:

   ```python
   X_ROBOTS_TAG = "noindex, nofollow"
   ```

   If `X_ROBOTS_TAG` is unset, `None`, or empty, no header is added — so you can enable
   the header per environment without changing your middleware list:

   ```python
   # settings/staging.py
   X_ROBOTS_TAG = ["noindex", "nofollow"]

   # settings/production.py
   X_ROBOTS_TAG = None
   ```

Details about the values for the tag and what they do can be found
[in the Google documentation](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#xrobotstag).

## Development

This project uses [uv](https://docs.astral.sh/uv/) for packaging and dependency
management (with the `uv_build` backend) and [Ruff](https://docs.astral.sh/ruff/) for
linting and formatting.

```console
$ uv sync --group dev                    # create .venv from uv.lock
$ uv run python manage.py test           # run the test suite
$ uv run coverage run manage.py test     # ...with coverage
$ uv run coverage report
$ uv run ruff check . && uv run ruff format .
$ uv build                               # build the sdist and wheel
```

To test against a specific Django version:

```console
$ uv pip install "Django~=6.0.0"
$ uv run --no-sync python manage.py test
```

Optionally, install the pre-commit hooks:

```console
$ uvx pre-commit install
```

The tests run against the `x_robots_tag_middleware_demo` project included in this repo.

## License

MIT — see [LICENSE](LICENSE).

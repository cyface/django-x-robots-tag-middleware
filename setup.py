from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="django-x-robots-tag-middleware",
    version="1.3.3",
    url="https://github.com/cyface/django-x-robots-tag-middleware",
    license="MIT",
    description="Enables returning the X-Robots-Tag header based on Django settings.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Tim White",
    author_email="tim@cyface.com",
    packages=find_packages(
        exclude=("x_robots_tag_middleware_demo", "tests", "devscripts")
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "django>=1.10",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
    ],
)

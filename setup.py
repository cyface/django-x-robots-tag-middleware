from setuptools import setup, find_packages

setup(
    name="django-x-robots-tag-middleware",
    version="0.1.7",
    url='http://timlwhite.com',
    license='BSD',
    description="Enables returning the X-Robots-Tag header based on Django settings.",
    long_description=open('README.rst').read(),

    author='Tim White',
    author_email='tim@cyface.com',

    packages=find_packages(exclude=('x_robots_tag_middleware_demo', 'tests', 'devscripts')),
    include_package_data=True,
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

from setuptools import setup, find_packages

setup(
    name="django-x-robots-tag-middleware",
    version="1.3",
    url='https://github.com/cyface/django-x-robots-tag-middleware',
    license='BSD',
    description="Enables returning the X-Robots-Tag header based on Django settings.",
    long_description=open('README.rst').read(),

    author='Tim White',
    author_email='tim@cyface.com',

    packages=find_packages(exclude=('x_robots_tag_middleware_demo', 'tests', 'devscripts')),
    include_package_data=True,
    zip_safe=False,
    install_requires=['django>=1.8.3', ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

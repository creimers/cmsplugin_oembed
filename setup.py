try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import djangocms_oembed

version = djangocms_oembed.__version__

setup(
    name = 'djangocms_oembed',
    packages = ['djangocms_oembed'],
    include_package_data = True,
    version = version,
    description = "Responsive video embedding for djangocms",
    author = 'Christoph Reimers',
    author_email = 'christoph@superservice-international.com',
    license='BSD License',
    url = 'https://github.com/creimers/djangocms_oembed',
    keywords = ['djangocms', 'django', 'responsive', 'oembed', 'video'], 
    install_requires = [
        'django-cms>=3.0',
        'django-embed-video>=1.0.0',
    ],
    classifiers = [
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)

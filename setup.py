# coding: utf-8

"""
    MX API
    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "django_atrium"
VERSION = "1.2.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["atrium >= 2.8.0", "python-dotenv >= 0.10.3"]

setup(
    version=VERSION,
    install_requires=REQUIRES,
)

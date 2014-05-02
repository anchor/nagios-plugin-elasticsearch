#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="nagios-plugin-elasticsearch",
    verion="1.0",
    packages=find_packages(),
    url="https://github.com/anchor/nagios-plugin-elasticsearch",
    scripts=["check_elasticsearch"],
    licence="MIT",
    install_requires=[str(req.req) for req in
                          parse_requirements("requirements.txt")],
    include_package_data=True
)

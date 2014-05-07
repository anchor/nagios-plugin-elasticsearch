#!/usr/bin/env python

from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="nagios-plugin-elasticsearch",
    version="1.0.0",
    packages=find_packages(),
    url="https://github.com/anchor/nagios-plugin-elasticsearch",
    maintainer="Sharif Olorin",
    maintainer_email="sio@tesser.org",
    author="Saj Goonatilleke",
    author_email="sg@redu.cx",
    scripts=["check_elasticsearch"],
    license="MIT",
    install_requires=[str(req.req) for req in
                          parse_requirements("requirements.txt")],
    include_package_data=True
)

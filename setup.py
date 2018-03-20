#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

requirements = []

setup_requirements = [
    'pytest-runner',
    # TODO(sdague): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='hvopen-website',
    version='0.1.0',
    description="Python tooling for hvopen website",
    long_description="",
    author="Sean Dague",
    author_email='sean@dague.net',
    url='https://github.com/hvopen/hvopen-website',
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='hvopen-website',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)

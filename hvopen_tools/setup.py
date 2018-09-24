#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'Markdown>=2.6',
    'python-frontmatter>=0.4.2',
    'requests>=2.18',
    'python-dateutil'
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'flake8']

setup(
    author="Sean Dague",
    author_email='sean@dague.net ',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Publishing tools for HV Open Website",
    entry_points={
        'console_scripts': [
            'meetup-sync=hvopen_tools.cmd.meetup:main',
            'mailchimp-sync=hvopen_tools.cmd.mailchimp:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='hvopen_tools',
    name='hvopen_tools',
    packages=find_packages(include=['hvopen_tools*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sdague/hvopen_tools',
    version='0.1.0',
    zip_safe=False,
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'autopep8'
]

setup_requirements = []

test_requirements = []

setup(
    author="Adam Hitchcock",
    author_email='adam@northisup.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='autopep8_autoline',
    name='autopep8_autoline',
    packages=find_packages(include=['autopep8_autoline']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/NorthIsUp/autopep8_autoline',
    version='0.1.0',
    zip_safe=False,
    entry_points={'console_scripts': [
        'autopep8-autoline = autopep8_autoline:main']},
)

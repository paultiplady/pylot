#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(
    name='pylot',
    version='0.1.0',
    description='Kubernetes deploy tool',
    author='Paul Tiplady',
    author_email='paul@qwil.co',
    packages=find_packages(),
    requires=[
        'docopt',
        'kubernetes',
    ],
    entry_points={
        'console_scripts': [
            'pylot = pylot.__main__:main'
        ],
    },
)

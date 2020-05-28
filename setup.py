#!/usr/bin/env python

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

import sys

from setuptools import find_packages
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

try:
    from pip._internal.req import parse_requirements
except:
    from pip.req import parse_requirements

if __name__ == '__main__':
    setup(name='nlg-eval',
          version='2.3',
          description="Wrapper for multiple NLG evaluation methods and metrics.",
          author='Shikhar Sharma, Hannes Schulz, Justin Harris',
          author_email='shikhar.sharma@microsoft.com, hannes.schulz@microsoft.com, justin.harris@microsoft.com',
          url='https://github.com/Maluuba/nlg-eval',
          packages=find_packages(),
          include_package_data=True,
          scripts=['bin/nlg-eval'],
          install_requires=[
            'click>=6.3',
            'nltk>=3.1',
            'numpy>=1.11.0',
            'psutil>=5.6.2',
            'requests>=2.19',
            'six>=1.11',
            'scipy>=0.17.0',
            'scikit-learn>=0.17',
            'gensim>=3',
            'Theano>=0.8.1',
            'tqdm>=4.24',
            'xdg'
          ],
    )

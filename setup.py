#!/usr/bin/env python
# coding=utf8

import os
import sys

from setuptools import setup, find_packages

if sys.version_info < (2, 7):
    tests_require = ['unittest2', 'mock']
    test_suite = 'unittest2.collector'
else:
    tests_require = ['mock']
    test_suite = 'unittest.collector'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='simplekv',
      version='0.4',
      description='A simple key-value storage for binary data.',
      long_description=read('README.rst'),
      keywords='key-value-store storage key-value db database',
      author='Marc Brinkmann',
      author_email='git@marcbrinkmann.de',
      url='http://github.com/mbr/simplekv',
      license='MIT',
      packages=find_packages(exclude=['test']),
      py_modules=[],
      tests_require=tests_require,
      test_suite='unittest2.collector',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Database',
          'Topic :: Software Development :: Libraries',
      ]
     )

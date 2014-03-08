#!/usr/bin/env python

from distutils.core import setup

setup(name='rasp-clock',
      version='0.1',
      py_modules=['display'],
      scripts=['clock.py'],
      requires=['circuits', 'pymetar'])

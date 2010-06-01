#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='epywing',
    version='0.1',
    description='Simple EPWING reader library',
    author='Alex Ehlke',
    author_email='manabi.org@gmail.com',
    url='http://www.manabi.org/epywing',
    #packages=['epywing'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    #package_dir={'epywing': 'src/epywing'},
    install_requires=[
       'lxml>=2.2.4',
       'ebmodule==2.0',
    ]
)


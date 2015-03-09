#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = 'versioneer-gbp-demo'

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = name + '/_version.py'
versioneer.versionfile_build = name + '/_version.py'
versioneer.tag_prefix = 'v'
versioneer.parentdir_prefix = name + '-'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name=name,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Versioneer/Git-Buildpackage Demo",
    long_description=readme,
    author="Dan Lipsitt",
    author_email='danlipsitt@gmail.com',
    url='https://github.com/DanLipsitt/versioneer-gbp-demo',
    packages=[name],
    package_dir={name: name},
    include_package_data=True,
    install_requires=requirements,
)

#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

import sys
import setuptools
import importlib.util


def import_pyhton_file(module_name, file_path):
    # Import module from file: https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='emmorph2ud2',
    version=getattr(import_pyhton_file('version', 'emmorph2ud2/version.py'), '__version__'),
    author='vadno',  # Will warn about missing e-mail
    description='A module for marking single word and multi-word units in POS-tagged text',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vadno/emmorph2ud2',
    # license='GNU Lesser General Public License v3 (LGPLv3)',  # Never really used in favour of classifiers
    # platforms='any',  # Never really used in favour of classifiers
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
    install_requires=['xtsv>=1.0,<2.0',  # TODO: List dependencies at only one file requirements.txt vs. setup.py
                      ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'emmorph2ud2=emmorph2ud2.__main__:main',
        ]
    },
)

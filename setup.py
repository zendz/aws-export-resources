#!/usr/bin/env python3
"""
Setup script for AWS Export Resources
"""

import os
import sys
from setuptools import setup, find_packages

# Read version directly from _version.py
version_file = os.path.join(os.path.dirname(__file__), 'src', '_version.py')
version_info = {}
with open(version_file) as f:
    exec(f.read(), version_info)

VERSION = version_info['__version__']

# Read requirements
with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aws-export-resources',
    version=VERSION,
    author='Nattait Nandawarang',
    author_email='github-issues-only@gosoft.co.th',
    description='A comprehensive AWS resource inventory tool that exports detailed information about AWS resources across multiple profiles to Excel format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zendz/aws-export-resources',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'aws-export-resources=aws_export_resources:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
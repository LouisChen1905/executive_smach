#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

package_name = 'smach'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages('src'),
#    packages=find_namespace_packages(where="src"),
    py_modules=[
      'smach.concurrence',
      'smach.container',
      'smach.exceptions',
      'smach.iterator',
      'smach.log',
      'smach.sequence',
      'smach.state',
      'smach.state_machine',
      'smach.user_data',
      'smach.util'
      ],
    package_dir={"": "src"},
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Louis Chen',
    maintainer_email='cszzys@gmail.com',
    description='TODO: Package description',
    license='Apache License, Version 2.0',
    test_suite='test',
    tests_require=['pytest'],
    )

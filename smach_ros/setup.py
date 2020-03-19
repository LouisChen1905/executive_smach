#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

package_name = 'smach_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages('src', exclude=['test']),
    py_modules=[
      'smach_ros.action_server_wrapper',
      'smach_ros.condition',
      'smach_ros.introspection',
      'smach_ros.monitor_state',
      'smach_ros.service_state',
      'smach_ros.simple_action_state',
      'smach_ros.util'
      ],
    package_dir={"": "src"},
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Louis Chen',
    maintainer_email='cszzys@gmail.com',
    license='Apache License, Version 2.0',
    test_suite='test',
    tests_require=['pytest'],
)

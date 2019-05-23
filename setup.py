# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="py-attribute-resource",
    version="1.0.1",
    description="Python module for file attribute management",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/py-attribute-resource.git",
    packages=find_packages(exclude=["test"]),
    install_requires=["py_status_resource"],
    tests_require=["py_file_resource", "py_directory_resource"],
    dependency_links=[
        "git+https://github.com/JhonnyBravo/py-status-resource.git#egg=py_status_resource",
        "git+https://github.com/JhonnyBravo/py-file-resource.git#egg=py_file_resource",
        "git+https://github.com/JhonnyBravo/py-directory-resource.git#egg=py_directory_resource"
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)

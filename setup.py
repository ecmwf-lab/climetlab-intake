#!/usr/bin/env python
# (C) Copyright 2021 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


package_name = "climetlab_intake"  # noqa: E501

version = None
lines = read(f"{package_name}/version").split("\n")
if lines:
    version = lines[0]

assert version


extras_require = {}

setuptools.setup(
    name=package_name,
    version=version,
    description=("A source plugin for climetlab for intake"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Florian Pinault",
    author_email="florian.pinault@ecmwf.int",
    url="https://github.com/ecmwf-lab/climetlab-intake",
    license="Apache License Version 2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "climetlab>=0.8.30",
        "intake",
        "intake-xarray",
    ],
    extras_require=extras_require,
    zip_safe=True,
    entry_points={
        "climetlab.sources": [
            "intake = climetlab_intake.intake_source.IntakeSource",
        ]
    },
    keywords="meteorology",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)

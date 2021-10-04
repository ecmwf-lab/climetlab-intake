#!/usr/bin/env python3
# (C) Copyright 2021 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

# import climetlab as cml
from climetlab import Source

__version__ = "0.1.0"

URL = "https://storage.ecmwf.europeanweather.cloud"

PATTERN = (
    "{url}/climetlab/test-data/0.5/fixtures/"
    "climetlab-cookiecutter-dataset/{year}-{parameter}.grib"
)


class IntakeSource(Source):
    name = None

    dataset = None

    def __init__(self, year, parameter):
        pass

    def to_xarray():
        pass

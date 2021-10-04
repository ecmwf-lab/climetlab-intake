#!/usr/bin/env python3
# (C) Copyright 2021 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import intake
# import climetlab as cml
from climetlab import Source

__version__ = "0.1.0"


class IntakeSource(Source):
    name = None

    dataset = None

    def __init__(self, catalog, item):
        self.catalog = intake.open_catalog(catalog)
        self.item_name = item

    def _get_catalog_item(self, item_name):
        return self.catalog[item_name]

    def to_xarray(self):

        import xarray as xr

        item = self._get_catalog_item(self.item_name)
        da = item.read()

        assert isinstance(da, xr.DataArray)

        return da.to_dataset(name=self.item_name)

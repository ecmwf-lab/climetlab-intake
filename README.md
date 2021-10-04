## climetlab-intake

A dataset plugin for climetlab for the dataset intake/lkqsjd.


Features
--------

In this README is a description of how to get the intake.

## Datasets description

There are two datasets: 

### 1 : `lkqsjd`
TODO


### 2 : TODO
TODO


## Using climetlab to access the data (supports grib, netcdf and zarr)

See the [demo notebooks](https://github.com/ecmwf-lab/climetlab-intake/tree/main/notebooks)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ecmwf-lab/climetlab-intake/main?urlpath=lab)


- [lkqsjd.ipynb](https://github.com/ecmwf-lab/climetlab-intake/tree/main/notebooks/demo_lkqsjd.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/ecmwf-lab/climetlab-intake/blob/main/notebooks/demo_lkqsjd.ipynb) 
[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ecmwf-lab/climetlab-intake/blob/main/notebooks/demo_lkqsjd.ipynb) 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ecmwf-lab/climetlab-intake/main?filepath=notebooks/demo_lkqsjd.ipynb)
[<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](https://deepnote.com/launch?name=MyProject&url=https://github.com/ecmwf-lab/climetlab-intake/tree/main/notebooks/demo_my_dataset.ipynb)


- TODO.


The climetlab python package allows easy access to the data with a few lines of code such as:
``` python

!pip install climetlab climetlab-intake
import climetlab as cml
ds = cml.load_dataset("intake-lkqsjd", date="20201231")
ds.to_xarray()
```


Support and contributing
------------------------

Either open a issue on github if this is a github repository, or send an email to email@example.com.

LICENSE
-------

See the LICENSE file.
License: [Apache License 2.0](LICENSE) In applying this licence, ECMWF does not waive the privileges and immunities 
granted to it by virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

Authors
-------

Florian Pinault and al.

See also the CONTRIBUTORS.md file.

## climetlab-intake

A dataset plugin to integrate intake dataset with climetlab. 

This is a miminal working example.

TODO
----

- Add integration with climetlab cache.
- Test on other example of intake datasets.


Features
--------

In this README is a description of how to get the intake.


## Using climetlab to access the data

See the [demo notebooks](https://github.com/ecmwf-lab/climetlab-intake/tree/main/notebooks)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ecmwf-lab/climetlab-intake/main?urlpath=lab)


- [demo_source_intake.ipynb](https://github.com/ecmwf-lab/climetlab-intake/tree/main/notebooks/demo_source_intake.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/ecmwf-lab/climetlab-intake/blob/main/notebooks/demo_source-intake.ipynb) 
[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ecmwf-lab/climetlab-intake/blob/main/notebooks/demo_source_intake.ipynb) 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ecmwf-lab/climetlab-intake/main?filepath=notebooks/demo_source_intake.ipynb)
[<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](https://deepnote.com/launch?name=MyProject&url=https://github.com/ecmwf-lab/climetlab-intake/tree/main/notebooks/demo_my_dataset.ipynb)




The climetlab python package allows easy access to the data with a few lines of code such as:
``` python

!pip install climetlab climetlab-intake
import climetlab as cml
ds = cml.load_souce("intake", catalog=..., item=...)
ds.to_xarray()
```


Support and contributing
------------------------

Either open a issue on github if this is a github repository.

LICENSE
-------

See the LICENSE file.
License: [Apache License 2.0](LICENSE) In applying this licence, ECMWF does not waive the privileges and immunities 
granted to it by virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

Authors
-------

Florian Pinault and al.

See also the CONTRIBUTORS.md file.

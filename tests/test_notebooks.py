#!/usr/bin/env python3# (C) Copyright 2021 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import os
import re
import sys

import nbformat
import pytest
from nbconvert.preprocessors import ExecutePreprocessor

# See https://www.blog.pythonlibrary.org/2018/10/16/testing-jupyter-notebooks/


EXAMPLES = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "notebooks",
)

SKIP = ("demo_do_not_test_me.ipynb",)


def notebooks_list():

    notebooks = []
    for path in os.listdir(EXAMPLES):
        # ignore notebooks starting with '_'
        if re.match(r"[^_].*\.ipynb$", path):
            if "Copy" not in path:  # ignore notebook including 'Copy'
                notebooks.append(path)

    return sorted(notebooks)


@pytest.mark.skipif(
    sys.platform == "win32", reason="Cannot execute notebooks on Windows"
)
@pytest.mark.parametrize("path", notebooks_list())
def test_notebook(path):
    print(path)

    if path in SKIP:
        pytest.skip("Notebook marked as 'skip'")

    with open(os.path.join(EXAMPLES, path)) as f:
        nb = nbformat.read(f, as_version=4)

    proc = ExecutePreprocessor(timeout=60 * 60, kernel_name="python3")
    proc.preprocess(nb, {"metadata": {"path": EXAMPLES}})


if __name__ == "__main__":
    for k, f in sorted(globals().items()):
        if k.startswith("test_") and callable(f):
            print(k)
            f()

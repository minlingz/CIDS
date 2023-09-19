import pandas as pd
import pytest
import os

from ds import pandas_ds


def test_pandas_ds():
    summary = pandas_ds()

    # Check if the summary DataFrame has the expected mean row
    assert "mean" in summary.index
    assert "std" in summary.index
    assert "50%" in summary.index


def test_save_plot():
    # Check if "plot.png" file was created
    assert os.path.isfile("plot.png")

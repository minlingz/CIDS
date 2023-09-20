from lib import read_csv_file
from lib import generate_statistics_summary


def test_read_csv_file():
    df = read_csv_file("world-small.csv")

    # Check if the DataFrame not empty
    assert not df.empty


def test_generate_statistics_summary():
    summary = generate_statistics_summary(read_csv_file("world-small.csv"))

    # Check if the summary DataFrame has the expected mean row
    assert "mean" in summary.index
    assert "std" in summary.index
    assert "50%" in summary.index

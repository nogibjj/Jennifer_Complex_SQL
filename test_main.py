"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    """test extract function"""
    test1 = extract()
    assert test1 is not None


def test_load():
    """test load function"""
    test2 = load()
    assert test2 == "DB loaded or already loaded"


def test_query():
    """test query function"""
    test3 = query()
    assert test3 == "Query successful"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
    print("Everything passed")

"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import DBquery, CRUD_Create, CRUD_Read, CRUD_Update, CRUD_Delete


def test_extract():
    assert extract() == "data/goose_rawdata.csv"


def test_transform():
    assert load() == "GooseDB.db"


def test_DBquery():
    assert DBquery() == "Query Successfully"


def test_Create():
    assert CRUD_Create() == "Create Successfully"


def test_Read():
    assert CRUD_Read() == "Read Successfully"


def test_Update():
    assert CRUD_Update() == "Update Successfully"


def test_Delete():
    assert CRUD_Delete() == "Delete Successfully"


if __name__ == "__main__":
    test_extract()
    test_transform()
    test_DBquery()
    test_Create()
    test_Read()
    test_Update()
    test_Delete()
    print("Everything passed")

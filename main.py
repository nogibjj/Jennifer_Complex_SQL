"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import DBquery, CRUD_Create, CRUD_Read, CRUD_Update, CRUD_Delete

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
DBquery()
CRUD_Create()
CRUD_Read()
CRUD_Update()
CRUD_Delete()

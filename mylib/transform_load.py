"""
Transforms and Loads data into local databricks database
"""

import csv
import os
from databricks import sql
from dotenv import load_dotenv


def load(dataset="data/goose.csv"):
    """Transforms and Loads data into the local databricks database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)  # Skip header

    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS GooseDB (
                    name string,
                    year int,
                    team string,
                    league string,
                    goose_eggs int,
                    broken_eggs int,
                    mehs int,
                    league_average_gpct float,
                    ppf int,
                    replacement_gpct float,
                    gwar float,
                    key_retro string
                )
            """
            )
            cursor.execute("SELECT * FROM GooseDB")
            result = cursor.fetchall()
            if not result:
                print("here")

                string_sql = "INSERT INTO GooseDB VALUES"
                for i in payload:
                    # Clean data, replacing None or empty values with SQL NULL
                    clean_data = [f"'{val}'" if val != "" else "NULL" for val in i]
                    string_sql += "\n" + f"({', '.join(clean_data)}),"

                string_sql = (
                    string_sql[:-1] + ";"
                )  # Remove last comma and add semicolon
                print(string_sql)

                cursor.execute(string_sql)

            cursor.close()
            connection.close()
    return "DB loaded or already loaded"


if __name__ == "__main__":
    load()

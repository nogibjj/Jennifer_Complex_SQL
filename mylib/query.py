"""Query the database from a db connection to Databricks"""

import os
from databricks import sql
from dotenv import load_dotenv


complex_query = """
WITH goose_stats AS (
    SELECT
        team,
        league,
        COUNT(name) AS total_players,
        ROUND(AVG(goose_eggs), 1) AS avg_goose_eggs,
        ROUND(AVG(broken_eggs), 1) AS avg_broken_eggs
    FROM
        default.goosedb
    GROUP BY
        team, league
)

SELECT * FROM default.goosedb
JOIN 
    goose_stats
ON 
    default.goosedb.team = (goose_stats.team AND 
    default.goosedb.league = goose_stats.league)
ORDER BY 
    goose_stats.avg_goose_eggs DESC;
"""


def query():
    """Query the database"""
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(complex_query)
            result = cursor.fetchall()

            for row in result:
                print(row)

            cursor.close()
            connection.close()

    return "Query successful"


if __name__ == "__main__":
    query()

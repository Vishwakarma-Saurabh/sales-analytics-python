import pandas as pd
from sales_project.sales_analytics.db import get_connection


class SalesRepository:

    @staticmethod
    def create_table():

        query = """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            revenue REAL,
            month TEXT
        )
        """

        with get_connection() as conn:
            conn.execute(query)

    @staticmethod
    def insert_sample_data():

        data = [
            ("Electronics", 120.5, "Jan"),
            ("Electronics", 195.44, "Feb"),
            ("Kitchenware", 152.00, "Jan"),
            ("Stationery", 45.00, "Jan"),
            ("Fitness", 75.00, "Feb"),
            ("Office Supplies", 60.00, "Mar"),
            ("Apparel", 89.50, "Mar"),
            ("Home Office", 35.00, "Jan")
        ]

        with get_connection() as conn:
            conn.executemany(
                "INSERT INTO sales(category,revenue,month) VALUES(?,?,?)",
                data
            )

    @staticmethod
    def fetch_all():

        with get_connection() as conn:

            query = "SELECT * FROM sales"

            df = pd.read_sql_query(query, conn)

        return df
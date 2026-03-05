import sqlite3
import logging
from contextlib import contextmanager
from sales_project.sales_analytics.config import DB_PATH

logging.basicConfig(level=logging.INFO)


@contextmanager
def get_connection():
    conn = None

    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row

        yield conn

        conn.commit()

    except sqlite3.Error as e:

        if conn:
            conn.rollback()

        logging.error(f"Database error: {e}")
        raise

    finally:
        
        if conn:
            conn.close()
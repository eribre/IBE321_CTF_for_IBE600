import sqlite3


class Database(object):
    """Custom database class to handle database connections."""

    # Automatically open the database connection
    def __enter__(self):
        self.conn = sqlite3.connect("user_db.db")
        return self

    # Automatically close the database connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    # empty placeholders by default to allow for unsafe queries (sql injection)
    def __call__(self, query, placeholders=""):
        cursor = self.conn.cursor()
        try:
            result = cursor.execute(query, placeholders)
            self.conn.commit()
        except Exception as ex:
            result = ex
        return result

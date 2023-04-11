import sqlite3


class Database(object):
    def __enter__(self):
        self.conn = sqlite3.connect("user_db.db")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    # empty placeholders by default to allow for unsafe queries (sql injection)
    def __call__(self, query, placeholders=""):
        c = self.conn.cursor()
        try:
            result = c.execute(query, placeholders)
            self.conn.commit()
        except Exception as e:
            result = e
        return result

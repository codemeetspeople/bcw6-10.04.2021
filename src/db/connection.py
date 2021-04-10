import psycopg2
import psycopg2.extras

connection_parameters = {
    'database': 'shop',
    'user': 'shop',
    'password': 'shop'
}
connection = None


def get_connection():
    global connection

    if not connection:
        connection = psycopg2.connect(
            **connection_parameters,
            cursor_factory=psycopg2.extras.RealDictCursor
        )
        connection.autocommit = True
    return connection


class PGConnection():
    def __init__(self):
        self._conn = get_connection()

    def __enter__(self):
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self._conn.commit()
        self._cursor.close()


if __name__ == '__main__':
    with PGConnection() as cursor:
        cursor.execute(
            'UPDATE category SET category_title = %s WHERE category_id = %s',
            ('Health', 1)
        )

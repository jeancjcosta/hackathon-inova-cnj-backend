import psycopg2
from .connection_factory import ConnectionFactory


class ServentiasDAO:

    def __init__(self):
        self.connection = ConnectionFactory().new_connection()
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_serventias_list(self):
        try:
            self.cursor.execute("""SELECT DISTINCT * FROM cnjinova.serventias """)
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

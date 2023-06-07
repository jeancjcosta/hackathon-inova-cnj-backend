import psycopg2
from .connection_factory import ConnectionFactory


class AssuntosDAO:

    def __init__(self):
        self.connection = ConnectionFactory().new_connection()
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_assuntos_list(self):
        try:
            self.cursor.execute("""SELECT * FROM cnjinova.assuntos """)
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

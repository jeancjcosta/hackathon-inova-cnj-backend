import psycopg2
from .connection_factory import ConnectionFactory


class MovimentosDAO:

    def __init__(self):
        self.connection = ConnectionFactory().new_connection()
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_movimnetos_list(self):
        try:
            self.cursor.execute("""SELECT DISTINCT * FROM cnjinova.movimentos """)
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

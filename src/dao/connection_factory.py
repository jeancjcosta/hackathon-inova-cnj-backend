import os

import psycopg2
from dotenv import load_dotenv

load_dotenv(verbose=True)

class ConnectionFactory:

    @staticmethod
    def new_connection():
        conexao = None
        try:
            conexao = psycopg2.connect(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"), database=os.getenv("DB_DATABASE"),
                                       user=os.getenv("DB_USER"), password=os.getenv("DB_PWD"))

            conexao.cursor().execute("SET CLIENT_ENCODING TO 'UTF8'")

            # aplica os atributos extras da conexao definidos no registro da conexao
            # if config.atributos:
            #     for chave, valor in zip(config.atributos.keys(), config.atributos):
            #         conexao.setAttribute(chave, valor)
        except (Exception, psycopg2.DatabaseError) as erro:
            if conexao is not None:
                conexao.close()
            raise Exception(erro)

        return conexao

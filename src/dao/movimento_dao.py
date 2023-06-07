import json
import psycopg2
from ..Entity.movimento import Movimento
from ..Entity.dados_basicos import DadosBasicos
from .connection_factory import ConnectionFactory


class MovimentoDAO:

    def __init__(self):
        self.connection = ConnectionFactory().new_connection()
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def save_movimento(self, movimento):
        try:
            self.cursor.execute(
                "INSERT INTO cnjinova.movimento (numero, identificadormovimento, tiporesponsavelmovimento, "
                "codigonacional, datahora) "
                "VALUES (%s, %s, %s, %s, %s) ",
                [movimento.get_numero(), movimento.get_identificador_movimento(),
                 movimento.get_tipo_responsavel_movimento(),
                 movimento.get_codigo_nacional(), movimento.get_data_hora()])
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

    def get_movimento(self, *args):
        pass

    def get_movimento_list_from_json(self, path):
        with open(path, 'rb') as json_file:
            data = json.load(json_file)
        movimento_list = []
        for processo in data:
            millis_insercao = processo["millisInsercao"]
            numero = processo["dadosBasicos"]["numero"]
            if processo is not None and "movimento" in processo and processo["movimento"] is not None:
                for movimento in processo["movimento"]:
                    id_mov = movimento["identificadorMovimento"] if "identificadorMovimento" in movimento else None
                    tipo = movimento["tipoResponsavelMovimento"] if "tipoResponsavelMovimento" in movimento else None
                    if movimento is not None and "movimentoNacional" in movimento:
                        if movimento["movimentoNacional"] is not None and "codigoNacional" in movimento["movimentoNacional"]:
                            mov_nacional = movimento["movimentoNacional"]["codigoNacional"]
                        else:
                            mov_nacional = None
                    else:
                        mov_nacional = None
                    data_hora = movimento["dataHora"] if "dataHora" in movimento else None
                    mov = Movimento(millis_insercao, numero, id_mov, tipo, mov_nacional, data_hora)
                    movimento_list.append(mov)

        return movimento_list

    def get_movimento_list(self, cod_serventia, cod_classe, cod_assunto):
        try:
            self.cursor.execute(
                """
                SELECT d.assunto, d.classeprocessual, d.codigoorgao, mov.codigonacional, AVG(mov.tempo) as avg, 
                STDDEV(mov.tempo) as std, mvs.descricao
                FROM cnjinova.movimento mov INNER JOIN cnjinova.dadosbasicos d ON d.numero = mov.numero
                LEFT JOIN cnjinova.movimentos mvs on mvs.codigo = mov.codigonacional 
                WHERE d.assunto is not null and d.classeprocessual is not null and mov.codigonacional is not null
                AND d.assunto = %s AND d.classeprocessual = %s AND mov.codigonacional IN
                (
                    SELECT DISTINCT mv.codigonacional 
                    FROM cnjinova.movimento mv INNER JOIN cnjinova.dadosbasicos dd on dd.numero = mv.numero
                    WHERE dd.assunto is not null and dd.classeprocessual is not null and mv.codigonacional is not null
                    AND dd.assunto = %s AND dd.classeprocessual = %s AND dd.codigoorgao = %s
                )
                GROUP BY d.assunto, d.classeprocessual, d.codigoorgao, mov.codigonacional, mvs.descricao HAVING count(*) > 30
                order by mov.codigonacional asc
                """, [cod_assunto, cod_classe, cod_assunto, cod_classe, cod_serventia])
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

    def get_movimento_list_full(self, cod_classe, cod_assunto):
        try:
            self.cursor.execute(
                """
                SELECT d.assunto, d.classeprocessual, s.nomedavara, mov.codigonacional, AVG(mov.tempo) as avg, 
                STDDEV(mov.tempo) as std,  mvs.descricao
                FROM cnjinova.movimento mov INNER JOIN cnjinova.dadosbasicos d on d.numero = mov.numero 
                LEFT JOIN cnjinova.movimentos mvs on mvs.codigo = mov.codigonacional
                INNER JOIN cnjinova.serventias s on s.seq_orgao = d.codigoorgao
                WHERE d.assunto is not null and d.classeprocessual is not null and mov.codigonacional is not null
                AND d.assunto = %s AND d.classeprocessual = %s
                GROUP BY d.assunto, d.classeprocessual, s.nomedavara, mov.codigonacional,  mvs.descricao HAVING count(*) > 30
                order by mov.codigonacional asc
                """, [cod_assunto, cod_classe])
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

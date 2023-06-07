from .connection_factory import ConnectionFactory
from ..Entity.dados_basicos import DadosBasicos
import json
import psycopg2


class DadosBasicosDAO:

    def __init__(self):
        self.connection = ConnectionFactory().new_connection()
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def save_dados_basicos(self, dados_basicos):
        try:
            self.cursor.execute(
                "INSERT INTO cnjinova.dadosbasicos (millisinsercao, assunto, dscsistema, tamanhoprocesso, numero, "
                "procel, dataajuizamento, totalassuntos, classeprocessual, nivelsigilo, codigoorgao, competencia, "
                "codigolocalidade, siglatribunal, grau) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ",
                [dados_basicos.get_millis_insercao(), dados_basicos.get_assunto(), dados_basicos.get_dsc_sistema(),
                 dados_basicos.get_tamanho_processo(), dados_basicos.get_numero(), dados_basicos.get_procel(),
                 dados_basicos.get_data_ajuizamento(), dados_basicos.get_total_assuntos(), dados_basicos.get_classe_processual(),
                 dados_basicos.get_nivel_sigilo(), dados_basicos.get_codigo_orgao(), dados_basicos.get_competencia(),
                 dados_basicos.get_codigo_localidade(), dados_basicos.get_sigla_tribunal(), dados_basicos.get_grau()])
            self.connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

    def get_dados_basicos(self, *args):
        pass

    def get_dados_basicos_list_from_json(self, path):
        with open(path, 'rb') as json_file:
            data = json.load(json_file)
        dados_basicos_list = []
        for processo in data:
            millis_insercao = processo["millisInsercao"]
            numero = processo["dadosBasicos"]["numero"]
            if "totalAssuntos" in processo["dadosBasicos"] and processo["dadosBasicos"]["totalAssuntos"] > 0:
                if "codigoNacional" in  processo["dadosBasicos"]["assunto"][0]:
                    assunto = processo["dadosBasicos"]["assunto"][0]["codigoNacional"]
                else:
                    assunto = None
            else:
                assunto = None
            dsc_sistema = processo["dadosBasicos"]["dscSistema"] if "dscSistema" in processo["dadosBasicos"] else None
            tamanho_processo = processo["dadosBasicos"]["tamanhoProcesso"] if "tamanhoProcesso" in processo["dadosBasicos"] else None
            procel = processo["dadosBasicos"]["procEl"] if "procEl" in processo["dadosBasicos"] else None
            data_ajuizamento = processo["dadosBasicos"]["dataAjuizamento"] if "dataAjuizamento" in processo["dadosBasicos"] else None
            total_assuntos = processo["dadosBasicos"]["totalAssuntos"] if "totalAssuntos" in processo["dadosBasicos"] else None
            classe_processual = processo["dadosBasicos"]["classeProcessual"] if "classeProcessual" in processo["dadosBasicos"] else None
            nivel_sigilo = processo["dadosBasicos"]["nivelSigilo"] if "nivelSigilo" in processo["dadosBasicos"] else None

            if "orgaoJulgador" in processo["dadosBasicos"]:
                if processo["dadosBasicos"]["orgaoJulgador"] is not None and "codigoOrgao" in processo["dadosBasicos"]["orgaoJulgador"]:
                    codigo_orgao = processo["dadosBasicos"]["orgaoJulgador"]["codigoOrgao"]
                else:
                    codigo_orgao = None
            else:
                codigo_orgao = None
            competencia = processo["dadosBasicos"]["competencia"] if "competencia" in processo["dadosBasicos"] else None
            codigo_localidade = processo["dadosBasicos"]["codigoLocalidade"] if "codigoLocalidade" in processo["dadosBasicos"] else None
            sigla_tribunal = processo["siglaTribunal"] if "siglaTribunal" in processo else None
            grau = processo["grau"] if "grau" in processo else None

            dados_basicos = DadosBasicos(millis_insercao, assunto, dsc_sistema, tamanho_processo, numero, procel,
                                         data_ajuizamento, total_assuntos, classe_processual, nivel_sigilo, codigo_orgao,
                                         competencia, codigo_localidade, sigla_tribunal, grau)
            dados_basicos_list.append(dados_basicos)

        return dados_basicos_list

    def get_avg_std_processo(self, cod_serventia, cod_classe, cod_assunto):
        try:
            self.cursor.execute(
                """
                SELECT AVG(d.tempo) as avg, STDDEV(d.tempo) as std
                FROM cnjinova.dadosbasicos d
                WHERE d.assunto is not null and d.classeprocessual is not null
                AND d.assunto = %s AND d.classeprocessual = %s AND d.codigoorgao = %s
                """, [cod_assunto, cod_classe, cod_serventia])
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

    def get_avg_std_processo_all(self, cod_classe, cod_assunto):
        try:
            self.cursor.execute(
                """
                select s.nomedavara , AVG(d.tempo) as avg, STDDEV(d.tempo) as std, count(*)
                from cnjinova.dadosbasicos d inner join cnjinova.serventias s on s.seq_orgao = d.codigoorgao
                where d.classeprocessual = %s and d.assunto = %s
                group by s.nomedavara having count(*) > 50 order by count(*) desc
                """, [cod_classe, cod_assunto])
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

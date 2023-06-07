from ..dao.dados_basicos_dao import DadosBasicosDAO
import pandas as pd


class DadosBasicosService:

    def __init__(self):
        pass

    @staticmethod
    def save_dados_basicos_list(dados_basicos_list):
        dados_basicos_dao = DadosBasicosDAO()
        for dados_basicos in dados_basicos_list:
            dados_basicos_dao.save_dados_basicos(dados_basicos)
        del dados_basicos_dao

    def get_avg_std_processo(self, cod_serventia=None, cod_classe=None, cod_assunto=None):
        dados_basicos_dao = DadosBasicosDAO()
        dados_basicos_avg_std = dados_basicos_dao.get_avg_std_processo(cod_serventia, cod_classe, cod_assunto)

        return dados_basicos_avg_std

    def get_avg_std_processo_full(self, cod_classe=None, cod_assunto=None):
        dados_basicos_dao = DadosBasicosDAO()
        dados_basicos_avg_std = dados_basicos_dao.get_avg_std_processo_all(cod_classe, cod_assunto)

        return pd.DataFrame(dados_basicos_avg_std, columns=["codigoorgao", "avg", "std", "count"])
        
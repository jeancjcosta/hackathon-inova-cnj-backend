from ..dao.movimento_dao import MovimentoDAO
import pandas as pd


class MovimentosService:

    def __init__(self):
        pass

    def get_avg_std_by_movimento(self, cod_serventia=None, cod_classe=None, cod_assunto=None):
        movimneto_dao = MovimentoDAO()
        movimento_list = movimneto_dao.get_movimento_list(cod_serventia, cod_classe, cod_assunto)

        return pd.DataFrame(movimento_list, columns=["assunto", "classe", "codigoorgao", "codigonacional", "avg", "std",
                                                     "dsc_mov"])

    def get_avg_std_by_movimento_full(self, cod_classe=None, cod_assunto=None):
        movimneto_dao = MovimentoDAO()
        movimento_list = movimneto_dao.get_movimento_list_full(cod_classe, cod_assunto)

        return pd.DataFrame(movimento_list, columns=["assunto", "classe", "codigoorgao", "codigonacional", "avg", "std",
                                                     "dsc_mov"])

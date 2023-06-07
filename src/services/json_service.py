from ..dao.movimento_dao import MovimentoDAO
from ..dao.dados_basicos_dao import DadosBasicosDAO


class JsonService:

    def get_movimento_list(self):
        pass

    def get_dados_basicos_list(self):
        pass

    def get_movimento_list_from_json(self, path):
        return MovimentoDAO().get_movimento_list_from_json(path)

    def get_dados_basicos_from_json(self, path):
        return DadosBasicosDAO().get_dados_basicos_list_from_json(path)


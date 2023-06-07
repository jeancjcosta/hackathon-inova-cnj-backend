from ..services.json_service import JsonService
from ..services.movimentos_service import MovimentoService
from ..services.dados_basicos_service import DadosBasicosService


class JsonController:

    @staticmethod
    def json_to_database(path_list):
        count = 13
        for path in path_list[12:]:
            print(count, " - Carregando arquivo " + path)
            movimento_list = JsonService().get_movimento_list_from_json(path)
            MovimentoService.save_movimento_list(movimento_list)
            dados_basicos_list = JsonService().get_dados_basicos_from_json(path)
            DadosBasicosService.save_dados_basicos_list(dados_basicos_list)
            count += 1

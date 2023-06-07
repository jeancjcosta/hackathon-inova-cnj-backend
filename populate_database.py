from src.controllers.json_controller import JsonController
from src.helpers.helper import Helper

if __name__ == "__main__":
    print("Iniciando o carregamento dos dados do json")
    JsonController.json_to_database(Helper.get_leaf_paths())
    print("FIM")


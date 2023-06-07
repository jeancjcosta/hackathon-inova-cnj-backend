from ..services.movimentos_service import MovimentosService
from flask import jsonify


class MovimentosController:

    def __init__(self):
        pass

    @staticmethod
    def get_movimentos():
        return jsonify(MovimentosService().get_movimnetos())

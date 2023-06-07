from ..services.serventias_service import ServentiasService
from flask import jsonify


class ServentiasController:

    def __init__(self):
        pass

    @staticmethod
    def get_serventias():
        return jsonify(ServentiasService().get_serventias())

from flask import jsonify
from ..services.assuntos_service import AssuntosService


class AssuntosController:

    def __init__(self):
        pass

    @staticmethod
    def get_assuntos():
        return jsonify(AssuntosService().get_assuntos())

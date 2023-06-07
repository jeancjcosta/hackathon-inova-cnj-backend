from ..services.classes_service import ClassesService
from flask import jsonify


class ClassesController:

    def __init__(self):
        pass

    @staticmethod
    def get_classes_processuais():
        return jsonify(ClassesService().get_classes())

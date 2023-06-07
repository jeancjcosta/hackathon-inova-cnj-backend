from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

from ..controllers.test_controller import TestController
from ..controllers.assuntos_controller import AssuntosController
from ..controllers.classes_controller import ClassesController
from ..controllers.serventias_controller import ServentiasController
from ..controllers.report_controller import ReportController
from ..controllers.movimentos_controller import MovimentosController

app = Flask(__name__)
CORS(app)


@app.route("/teste-cors", methods=["GET"])
def hello_world():
    return "Hello, cross-origin-world!"


@app.route("/api/score", methods=["GET"])
def score():
    return TestController.get_score(request)


@app.route("/api/desempenho-unidade-judicial", methods=["GET"])
def performance_unidade_judicial():
    return ReportController.performance_statistics(request)


@app.route("/api/gargalos-serventia", methods=["GET"])
def gargalos_serventia():
    return ReportController.gargalos_serventia(request)


@app.route("/api/gargalos", methods=["GET"])
def gargalos():
    return ReportController.gargalos(request)


@app.route("/api/expectativa-tempo-tramitacao", methods=["GET"])
def expectativa_tempo_tramitacao():
    return ReportController.expected_process_duration(request)


@app.route("/api/assuntos/list", methods=["GET"])
def assuntos_list():
    return AssuntosController.get_assuntos()


@app.route("/api/classes/list", methods=["GET"])
def classes_list():
    return ClassesController.get_classes_processuais()


@app.route("/api/movimentos/list", methods=["GET"])
def movimentos_list():
    return MovimentosController.get_movimentos()


@app.route("/api/serventias/list", methods=["GET"])
def serventias_list():
    return ServentiasController.get_serventias()



def init():
    app.run(host="127.0.0.1", port=8000)

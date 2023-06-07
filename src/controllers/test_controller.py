
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from aiohttp import web
from sklearn.neural_network import MLPClassifier
from flask import jsonify


class TestController:

    @staticmethod
    def get_score(requst):
        # exemplo de como pegar dados do request usando o aiohttp
        # if 'data' in request.query.keys():
        #     data = request.query['data']

        # usando flask
        # request.args.get('data')

        digits = load_digits()
        X = digits.data
        Y = digits.target
        X = (X - np.min(X, 0)) / (np.max(X, 0) + 0.0001)  # 0-1 scaling

        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=0.2, random_state=0)

        mlp = MLPClassifier()
        mlp.fit(X_train, Y_train)
        return jsonify(mlp.score(X_test, Y_test))

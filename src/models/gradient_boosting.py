from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import pickle
import os

class GradientBoosting(object):
    """
    Classe que implementa o Gradient Boosting com sklearn.
    """

    def __init__(self, learning_rate=0.1, n_estimators=100, max_depth=7):
        """
        :param learning_rate: taxa de aprendizado
        :param n_estimators: número de estimadores (árvores)
        """
        self.learning_rate = learning_rate
        self.n_estimators = n_estimators
        self.model = GradientBoostingClassifier(n_estimators=self.n_estimators, learning_rate=self.learning_rate,
                                                verbose=1, loss='exponential', max_depth=max_depth)

    def fit(self, X, y):
        """
        Ajusta o modelo aos dados de treinamento
        :param X: Matriz multidimensional com os dados de treinamento
        :param y: abel unidimensional das entradas de X
        :return:
        """
        X = np.array(X)
        y = np.array(y)
        self.model.fit(X, y)

    def predict(self, X):
        """
        Método para predizes as classes
        :param X: Matriz multidimensional com os dados a serem classificados
        :return: vetor com as predições do modelo relativos aos dados de entrada
        """
        X = np.array(X)
        return self.model.predict(X)

    def predict_proba(self, X):
        """
        Método para predizes as classes
        :param X: Matriz multidimensional com os dados a serem classificados
        :return: vetor com as probabilidades de cada classe do modelo relativos aos dados de entrada
        """
        X = np.array(X)
        return self.model.predict_proba(X)

    def score(self, X, y):
        """
        Método para calcular a taxa de acerto
        :param X: Matriz multidimensional com os dados a serem classificados
        :param y: Classes reais da bae de dados
        :return: um score representando a taxa de acerto.
        """
        X = np.array(X)
        y = np.array(y)
        pred = self.model.predict(X)
        return sum([1 for a, b in zip(pred, y) if a == b])/y.shape[0]

    def salvar(self, nome_do_modelo):
        dirname = os.path.dirname(__file__)
        pickle.dump(self.model, open(dirname + '/models-treinados/' + nome_do_modelo + '_model.sav', 'wb'))
        del self.model


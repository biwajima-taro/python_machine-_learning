import numpy as np


class Perceptron:

    def __init__(self, eta: float = 0.01, n_iter: int = 50, random_state: int = 1):
        """perceptron class"""
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)

    def net_input(self, X: np.ndarray) -> tuple:
        return np.dot(X, self.w_[1:])+self.w_[0]

    def predict(self, X):
        return np.where(self.net_iput(X) >= 0.0, 1, -1)

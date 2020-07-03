from common.functions import sigmoid, soft_max, cross_entropy_error
import numpy as np
from typing import Dict
import attr
from common.gradient import numerical_gradient
import os
import sys
sys.path.append(os.pardir)


# @attr.s
class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 重みの初期化
        self.params = {}
        self.params['W1'] = weight_init_std * \
            np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * \
            np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    def predict(self, x):
        w1, w2 = self.params["W1"], self.params["W2"]
        b1, b2 = self.params["b1"], self.params["b2"]
        return self.__two_layer_prediction(x, w1, w2, b1, b2)

    def __two_layer_prediction(self, x, w1, w2, b1, b2):
        a1 = np.dot(x, w1)+b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, w2)+b2
        z2 = soft_max(a2)
        return z2

    def loss(self, x, training):
        predict = self.predict(x)
        return cross_entropy_error(predict, training)

    def accuracy(self, x: np.ndarray, training: np.ndarray):
        predict = self.predict(x)
        # axis=0:return the maximum of each column,axis=1 return the maximu of each raw
        predict = np.argmax(predict, axis=1)
        training = np.argmax(training, axis=1)
        # x.shape[0] returns the numboer of row
        accuracy = np.sum(predict == training)/float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x: np.ndarray, training: np.ndarray):
        def loss_W(W): return self.loss(x, training)

        def calc(param: str):
            grads[param] = numerical_gradient(loss_W, self.params["w1"])

        grads = {}
        for param in ["W1", "W2", "b1", "b2"]:
            calc(param)
        return grads


#if __name__ == "__main__":
   # tmp = TwoLayerNet()
    #tmp2 = TwoLayerNet()
    #print(tmp2)

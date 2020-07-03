from common.functions import sigmoid, soft_max, cross_entropy_error
import numpy as np
from typing import Dict
import attr
from common.gradient import numerical_gradient
import os
import sys
sys.path.append(os.pardir)


@attr.s
class TwoLayerNet:
    params: Dict = attr.ib(default={})
    input_size: int = attr.ib()
    hidden_size: int = attr.ib()
    output_size: int = attr.ib()
    weight_init_std: float = attr.ib(default=0.01)

    def __attrs_post_init__(self):
        self.params["hogehoge"] = "hogehoge"

    def predict(self, x):
        w1, w2 = self.params["w1"], self.params["w2"]
        b1, b2 = self.params["b1"], self.params["b2"]
        return self.__two_layer_prediction(x, w1, w2, b1, b2)

    def __two_layer_prediction(self, x, w1, w2, b1, b2):
        a1 = np.dot(x, w1)+b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, w2)+b2
        z2 = soft_max(a2)
        return z2

    def loss(self, x, traning):
        predict = self.predict(x)
        return cross_entropy_error(predict, training)


if __name__ == "__main__":
    tmp = TwoLayerNet()
    tmp2 = TwoLayerNet()
    print(tmp2)

from neural_network import soft_max, cross_entropy_error
import attr
from gradient import numerical_gradient
import numpy as np
import sys
import os
sys.path.append(os.pardir)


@attr.s
class SimpleNet:
    weight: np.ndarray = attr.ib(init=None)

    def __attrs_post_init__(self):
        self.weight = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.weight)

    def loss(self, x, train_data):
        z = self.predict(x)
        prediction = soft_max(z)
        loss = cross_entropy_error(prediction, train_data)
        return loss


if __name__ == "__main__":
    net=SimpleNet()
    print(net.weight)
    x=np.array([0.6,0.9])
    predict=net.predict(x)
    print(predict)
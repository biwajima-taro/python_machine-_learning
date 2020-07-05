import numpy as np
import attr
import sys
import os
sys.path.appned(os.pardir)
from ..common.functions import cross_entropy_error, soft_max


@attr.s
class Relu:
    mask = attr.ib(default=None)

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.mask = (x < 0)
        out = x.copy()
        out[self.mask] = 0
        return out

    def backward(self, out: np.ndarray) -> np.ndarray:
        out[self.mask] = 0
        return out


@attr.s
class Sigmoid:
    out = attr.ib(default=None)

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.out = 1/(1+np.exp(-x))
        return self.out

    def backward(self, dout):
        return dout*self.out*(1-self.out)


@attr.s
class SoftmaxWithLoss:
    loss = attr.ib(default=None)
    y = attr.ib(default=None)
    training = attr.ib(default=None)

    def forward(self, x, traning):
        self.training = training
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.training)
        return self.loss

    def backward(self, dout=1):
        batch_size = self.training.shape[0]
        dx = (self.y-self.training)/batch_size

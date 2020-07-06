import attr
import numpy as np
from abc import ABCMeta, abstractclassmethod
from typing import Dict, List
DELTA = 1e-7


class Optimizer(metaclass=ABCMeta):
    @abstractclassmethod
    def update(self):
        pass


@attr.s
class Momentum(Optimizer):
    learning_rate: float = attr.ib()
    momentum: float = attr.ib(default=0.9)
    velocity: float = attr.ib(default=None)

    def update(self, params: Dict, grads: Dict):
        """


        Parameters
        ----------
        params : Dict
            [description]
        grads : Dict
            [description]
        """
        if self.velocity is None:
            self.velocity = {}
            for key, item in params.items:
                self.velocity[key] = item

        for key in params.keys():
            self.velocity[key] = self.momentum*self.velocity[key] - \
                self.learning_rate*grad[key]
            params[key] += self.velocity[key]


@attr.s
class AdaGrad(Optimizer):
    learning_rate: float = attr.ib(default=0.01)
    h = attr.ib(default=None)

    def update(self, params: Dict, grads: Dict):
        if self.h is None:
            self.h = {}
            for key, value in params.items():
                self.h[key] = np.zeros_like(value)

        for key in params.keys():
            self.h[key] = grads[key]*grads[key]
            params[key] = self.learning_rate * \
                grads[key]/(np.sqrt(self.h[key]+DELTA))


class Adam(Optimizer):

    """Adam (http://arxiv.org/abs/1412.6980v8)"""

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None

    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)

        self.iter += 1
        # learning late is differento for each time
        lr_t = self.lr * np.sqrt(1.0 - self.beta2 **
                                 self.iter) / (1.0 - self.beta1**self.iter)

        for key in params.keys():
            #self.m[key] = self.beta1*self.m[key] + (1-self.beta1)*grads[key]
            #self.v[key] = self.beta2*self.v[key] + (1-self.beta2)*(grads[key]**2)
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])

            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)

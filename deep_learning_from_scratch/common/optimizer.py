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

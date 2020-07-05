import attr
from typing import Dict
from optimizer import Optimizer

@attr.s
# sttochastic gradieng descent
class SGD(Optimizer):
    learning_rate: float = attr.ib()

    def update(self, params: Dict, grads: Dict) -> None:
        for key in params.keys():
            params[keys] += lr*grad[key]

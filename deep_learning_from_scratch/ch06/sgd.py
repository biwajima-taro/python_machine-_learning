import attr
from typing import Dict


@attr.s
# sttochastic gradieng descent
class SGD:
    learning_rate: float = attr.ib()

    def update(self, params: Dict, grads: Dict) -> None:
        for key in params.keys():
            params[keys] += lr*grad[key]

from __future__ import annotations
import attr
from typing import List
import numpy as np


@attr.s
class Variable:
    data: np.ndarray = attr.ib()
    grad: np.ndarray = attr.ib(default=None)
    creator: Function = attr.ib(default=None)

    def set_creator(self, func) -> None:
        self.creator = func

    def backward(self):
        funcs: List[Function] = [self.creator]
        while funcs:
            f = funcs.pop()
            x, y = f.input, f.output
            x.grad = f.backward(y.grad)
            if x.creator:
                funcs.append(x.creator)
        return x.grad


@attr.s
class Function:
    input: Variable = attr.ib(init=None)
    output: Variable = attr.ib(init=None)

    def forward(self):
        raise NotImplemented

    def backward(self):
        raise NotImplemented

    def __call__(self, input: Variable) -> Variable:
        self.input = input
        y = self.forward(input.data)
        output = Variable(y)
        output.set_creator(self)
        self.output = output
        return output

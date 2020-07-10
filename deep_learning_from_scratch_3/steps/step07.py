import attr
from typing import List
import numpy as np


@attr.s
class Variable:
    data: np.ndarray = attr.ib()
    grad: np.ndarray = attr.ib()
    # how to write Function as a type hint?
    creator = attr.ib(default=None)

    def set_creator(self, func) -> None:
        self.creator = func

    def backward(self):
        f = self.creator
        if f:
            x = f.input
            x.grad = f.backward(self.grad)
            value=x.backward()
        return value

@attr.s
class Function:
    input: Varible = attr.ib(init=None)
    output: Variable = attr.ib(init=None)

    def forward(self):
        raise NotImplemented

    def backward(self):
        raise NotImplemented

    def __call__(self, input: Variable) -> Variable:
        self.input = input
        y = self.forward(input.data)
        output = Variable(y)
        ouput.set_creator(self)
        self.output = output
        return Variable(y)

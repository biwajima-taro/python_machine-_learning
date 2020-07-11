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
        f = self.creator
        if f:
            x = f.input
            x.grad = f.backward(self.grad)
            value = x.backward()
        else:
            value = self.grad
        return value


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


class Square(Function):
    def forward(self, x: np.ndarray) -> np.ndarray:
        y = x**2
        return y

    def backward(self, gy: np.ndarray) -> np.ndarray:
        x = self.input.data
        return 2*x*gy


class Exp(Function):
    def forward(self, x: np.ndarray) -> np.ndarray:
        return np.exp(x)

    def backward(self, gy: np.ndarray) -> np.ndarray:
        x = self.input.data
        return np.exp(x)*gy


if __name__ == "__main__":
    A = Square()
    B = Exp()
    C = Square()

    x = Variable(np.array(0.5))
    a = A(x)
    b = B(a)
    y = C(b)

    y.grad=np.array(1.0)
    print(y.backward())

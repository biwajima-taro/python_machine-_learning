from typing import List
import numpy as np
import attr
from abc import ABC, abstractclassmethod


@attr.s
class Variable:
    data: np.ndarray = attr.ib()
    grad: np.ndarray = attr.ib(default=None)


@attr.s
class Fuction(ABC):
    input: Variable = attr.ib(default=None)

    @abstractclassmethod
    def forward(self):
        pass

    @abstractclassmethod
    def backward(self):
        pass

    def __call__(self, input: Variable) -> Variable:
        self.input = input
        y = self.forward(input.data)
        return Variable(y)


class Square(Fuction):
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
        return exp(x)*gy



if __name__=="__main__":
    A=Square()
    B=Exp()
    C=Square()

    x=Variable(np.array(0.5))
    a=A(x)
    b=B(a)
    c=C(b)
    \ 
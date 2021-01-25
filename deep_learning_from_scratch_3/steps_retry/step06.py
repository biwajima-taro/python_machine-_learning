from dataclasses import dataclass
from typing import Any
import numpy as np


@dataclass
class Variable:
    data: Any
    grad: Any = None


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.input = input
        return output

    def forward(self, x):
        NotImplementedError()

    def backwward(self, gy):
        raise NotImplementedError()


class Square(Function):
    def forward(self, x):
        y = x**2
        return y

    def backward(self, gy):
        x = self.input.data
        gx = 2*x*gy
        return gx


class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y

    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x)*gy
        return gx


if __name__ == "__main__":
    A = Square()
    B = Exp()
    C = Square()
    x = Variable(np.array(0.6))
    a = A(x)
    b = B(a)
    y = C(b)
    print(y)


    y.grad=np.array(1.0)
    b.grad=C.backward(y.grad)
    a.grad=B.backward(b.grad)
    x.grad=A.backward(a.grad)
    print(x.grad)
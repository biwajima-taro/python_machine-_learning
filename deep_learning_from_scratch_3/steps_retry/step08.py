from dataclasses import dataclass
from typing import Any
import numpy as np
from typing import Callable


@dataclass
class Variable:
    data: Any
    grad: Any = None
    creator: Callable = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            x, y = f.input, f.output
            x.grad = f.backward(y.grad)
            if x.creator is not None:
                funcs.append(x.creator)


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        output.set_creator(self)
        self.input = input
        self.output = output
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
        print(gy)
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

    y.grad = np.array(1.9)
    y.backward()
    print(x.grad)

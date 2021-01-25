from step08 import Exp
import numpy as np
from typing import Callable, Any
from dataclasses import dataclass

def square(x):
    f = Square()
    return f(x)


def exp(x):
    f = Exp()
    return f(x)


@dataclass
class Variable:
    data: Any
    grad: Any = None
    creator: Callable = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            x, y = f.input, f.output
            x.grad = f.backward(y.grad)
            if x.creator is not None:
                funcs.append(x.creator)

    def __post_init__(self):
        if self.data is not None:
            if not isinstance(self.data, np.ndarray):
                raise TypeError(f"{self.data} is not supported")


def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(as_array(y))
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







if __name__ == "__main__":
    a = Variable(213)

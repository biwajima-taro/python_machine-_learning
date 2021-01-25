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
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(xs)
        outputs = [Variable(as_array(y)) for y in ys]
        for ouput in outputs:
            ouput.set_creator(self)
        self.inputs = inputs
        self.outputs = outputs
        return outputs if len(outputs) > 1 else outputs[0]

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


class Add(Function):
    def forward(self, xs):
        x0, x1 = xs
        y = x0+x1
        return (y,)



if __name__=="__main__":
    x=Variable(np.array(1))

    y=Variable(np.array(3))
    f=Add()
    y=f(x,y)
    print(y.data)
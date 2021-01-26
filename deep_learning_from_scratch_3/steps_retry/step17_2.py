import weakref
import numpy as np
from typing import Callable, Any
from dataclasses import dataclass


def exp(x):
    f = Exp()
    return f(x)


def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x


@dataclass
class Variable:
    data: Any
    grad: Any = None
    creator: Callable = None
    generation: int = 0

    def set_creator(self, func):
        self.creator = func
        self.generation = self.generation+1

    def backward(self):

        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = []
        seen_set = set()

        def add_func(f):
            if f not in seen_set:
                funcs.append(f)
                seen_set.add(f)
                funcs.sort(key=lambda x: x.generation)

        while funcs:
            f = funcs.pop()
            gys = [output().grad for output in f.ouputs]
            gxs = f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)
            for x, gx in zip(f.inputs, gxs):
                if x.grad is None:
                    x.grad = gx

    def __post_init__(self):
        if self.data is not None:
            if not isinstance(self.data, np.ndarray):
                raise TypeError(f"{self.data} is not supported")


class Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]
        self.generation = max([x.generation for x in inputs])
        for output in outputs:
            output.set_creator(self)
        self.inputs = inputs
        self.outputs = [weakref.ref(output) for output in outputs]
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, x):
        NotImplementedError()

    def backwward(self, gy):
        raise NotImplementedError()


class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y

    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x)*gy
        return gx


class Square(Function):
    def forward(self, x):
        y = x**2
        return y

    def backward(self, gy):
        x = self.input.data
        print(gy)
        gx = 2*x*gy
        return gx


def square(x):
    f = Square()
    return f(x)


if __name__ == "__main__":
    for i in range(10):
        x = Variable(np.random.randn(100))
        y = square(square(square(x)))

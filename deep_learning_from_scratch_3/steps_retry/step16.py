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
    generation: int = 0

    def set_creator(self, func):
        self.creator = func
        self.generation = self.generation+1



    def backward(self):

        if self.grad is None:
            self.grad=np.ones_like(self.data)
        funcs=[]
        seen_set=set()
        def add_func(f):
            if f not in seen_set:
                funcs.append(f
                seen_set.add(f)
                funcs.sort(key=lambdax:x.generation)

        while funcs:
            f=funcs.pop()
            gys=[output.grad for ouput in f.ouputs]
            gxs=f.backward(*gys)
            if not isinstance(gxs,tuple):
                gxs=(gxs,)
            for x ,gx in zip(f.inputs,gxs):
                if x.grad is None:
                    x.grad=gx

   def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            gys = [output.grad for output in f.outputs]
            gxs = f.backward(*gys)
            #x, y = f.input, f.output
            if not isinstance(gxs, tuple):
                gxs = (gxs,)
            for x, gx in zip(f.inputs, gxs):
                x.grad = gx
                if x.creator is not None:
                    funcs.append(x.creator)

    def __post_init__(self):
        if self.data is not None:
            if not isinstance(self.data, np.ndarray):
                raise TypeError(f"{self.data} is not supported")

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

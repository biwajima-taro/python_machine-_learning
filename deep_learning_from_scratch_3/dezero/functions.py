from .core_simple import Function, Variable
import attr
from typing import Tuple
from .core import as_variable
import numpy as np


@attr.s
class Transpose(Function):
    def forward(self,x:np.ndarray)->np.ndarray:
        np.transpose(x)

    def backward(self,dy):
        return transpose(dy)

def transpose(x):
    return Transpose()(x)

@attr.s
class Reshape(Function):
    shape: Tuple = attr.ib()

    def forward(self, x: Variable) -> Variable:
        # stored for backward
        self.prev_shape = x.shape
        return x.reshape(self.shape)

    def backward(self, gy: Variable):
        return reshape(gy, self.prev_shape)


def reshape(x: Variable, shape: Tuple) -> Variable:

    if x.shape == shape:
        return as_variable(x)
    return Reshape(shape)(x)

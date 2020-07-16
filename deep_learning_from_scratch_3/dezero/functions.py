from .core_simple import Function, Variable
import attr
from typing import Tuple
from .core import as_variable


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

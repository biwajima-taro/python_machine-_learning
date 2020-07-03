import attr
from typing import Tuple


@attr.s
class MulLayer:
    x = attr.ib(default=None)
    y = attr.ib(default=None)


def forward(self, x, y):
    self.x = x
    self.y = y
    return x*y


def backward(self, dout) -> Tuple:
    dx = dout*self.y
    dy = dout*self.x

    return dx, dy


@attr.s
class AddLayer:
    def forward(self, x, y):
        return x+y

    def backward(self, dout) -> Tuple:
        return dout, dout




import numpy as np
import attr

@attr.s
class Relu:
    mask = attr.ib(default=None)

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.mask = (x < 0)
        out = x.copy()
        out[self.mask] = 0
        return out

    def backward(self, out: np.ndarray) -> np.ndarray:
        out[self.mask] = 0
        return out


@attr.s
class Sigmoid:
    out = attr.ib(default=None)

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.out = 1/(1+np.exp(-x))
        return self.out

    def backward(self, dout):
        return dout*self.out*(1-self.out)

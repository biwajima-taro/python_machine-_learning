from .step08 import Variable, Square, Exp
import attr
import numpy as np
from typing import List


def as_array(x: np.ndarray) -> np.ndarray:
    """
     convert x into ndarray if necessary

    Parameters
    ----------
    x : np.ndarray
        [description]

    Returns
    -------
    np.ndarray
        [description]
    """
    if np.isscalar(x):
        return np.array(x)
    return x


@attr.s
class Function:
    input: List[Variable] = attr.ib(init=None)
    output: List[Variable] = attr.ib(init=None)

    def forward(self):
        raise NotImplemented

    def backward(self):
        raise NotImplemented

    def __call__(self, *inputs: Variable) -> List[Variable]:
        """
        [summary]

        Returns
        -------
        List[Variable]
            [description]
        """             
        xs = [input.data for input in inputs]
        self.input = input
        ys = self.forward(input.data)
        outputs = [Variable(as_array(y)) for y in ys]
        for output in outputs:
            output.set_creator(self)
        self.outputs = outputs
        return outputs if len(outputs) > 1 else output[0]

import numpy as np
from step01 import Variable
from abc import ABC, abstractclassmethod


class Function(ABC):
    @abstractclassmethod
    def forward(self):
        pass

    def __call__(self, input: Variable) -> Variable:
        """

        Parameters
        ----------
        input : Variable
            [description]

        Returns
        -------
        Variable
            [description]
        """
        x = input.data
        y = self.forward(x)
        return Variable(y)


class Square(Function):
    def forward(self, x: np.ndarray) -> np.ndarray:    
        return x**2


class Exp(Function):
    def forward(self, x: np.ndarray) -> np.ndarray:
        
        return np.exp(x)


def numerical_diff(f:Function,x:Variable,eps=1e-5):
    x0=Variable(x.data-eps)
    x1=Variable(x.data+eps)
    y0,y1=f(x0),f(x1)
    return (y1.data-y0.data)/(2*eps)



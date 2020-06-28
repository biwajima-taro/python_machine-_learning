import numpy as np
from typing import List


def AND_(x1: int, x2: int, w1: float = 0.5, w2: float = 0.5, theta: float = 0.7) -> int:
    """
    ANT gate implemented by perceptron

    Parameters
    ----------
    x1 : int
        [description]
    x2 : int
        [description]
    w1 : float, optional
        [description], by default 0.5
    w2 : float, optional
        [description], by default 0.5
    theta : float, optional
        [description], by default 0.7

    Returns
    -------
    int
        [description]
    """

    tmp = x1*w1+x2*w2
    if tmp > theta:
        return 1
    return 0


def AND(x1: int, x2: int, weight: List = [0.5, 0.5],
        threshold: float = 0.7) -> int:
    x = np.array([x1, x2])
    w = np.array(weight)

    tmp = np.sum(x*w)-threshold
    if tmp > 0:
        return 1
    return 0


def NAND():
    NotImplemented


def OR():
    NotImplemented


def XOR(x1: int, x2: int) -> int:
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

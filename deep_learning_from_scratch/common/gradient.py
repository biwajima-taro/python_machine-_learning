import numpy as np
from typing import Callable


def numerical_diff(func: Callable, x: float):
    """[summary]

    Parameters
    ----------
    func : [type]
        [description]
    x : [type]
        [description]
    """
    h = 1e-4
    return (func(x+h)-func(x-h))/2*h


def numerical_gradient(func: Callable, x: np.ndarray) -> np.ndarray:
    """[summary]

    Parameters
    ----------
    func : Callable
        [description]
    x : np.ndarray
        [description]

    Returns
    -------
    np.ndarray
        [description]
    """
    h = 1e-4
    grad = np.zeros_like(x)
    for i in range(x.size):
        grad[i] = numerical_partial_diff(func, x, i, h)
    return grad


def numerical_partial_diff(func: Callable,  x: np.ndarray, i: int, h: float = 1e-4):
    tmp = x[i]
    x[i] = tmp+h
    f1 = func(x)
    x[i] = tmp-h
    f2 = func(x)
    # set back value to its original
    x[i] = tmp
    return (f1-f2)/(2*h)


def gradient_decent(func: Callable, init_x: np.array, learning_rate: float = 0.01, step_num: int = 100) -> np.ndarray:
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(func, x)
        x -= learning_rate*grad
    return x


if __name__ == "__main__":
    def func2(x: np.ndarray):
        return np.sum(x**2)
    print(numerical_gradient(func2, np.array([3.0, 4.0])))

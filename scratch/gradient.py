from typing import Callable, TypeVar, List, Iterator
from scratch.lineaer_algebra import Vector, add, scalar_multiply
T = TypeVar("T")

def 


def difference_auotient(f: Callable[float, float],
                        x: float, h: float) -> float:
    """calc derivative of one-variable function """
    return (f(x+h)-f(x))/h


def partial_differnce_quotient(f: Callable[[Vector], float],
                               v: Vector, i: int, h: float) -> float:
    """partial derivative of multiple-variables function"""
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w)-f(v))/h


def gradient_step(v: Vector, gradient: Vector,
                  step_size: float) -> Vector:
    step = scalar_multiply(step_size, gradient)
    return add(v, step)


def minibatches(dataset: List[T], batch_size: int,
                shuffle: bool = True) -> Iterator[List[T]]:

    batch_starts = [start for start in range(0, len(dataset), batch_size)]
    if shuffle:
        random.shuffle(batch_starts)
    for start in batch_starts:
        end = start+batch_size
        yield[start:end]

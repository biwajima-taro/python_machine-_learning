from linear_algebra import dot, Vector
from typing import List


def predict(x: Vector, beta: Vector) -> float:
    return dot(x, beta)


def error(x: Vector, y: Vector, beta: Vector) -> float:
    return predict(x, beta)-y

def squared_error(x: Vector, y: Vector) -> float:
    return error(x, y)**2

def sqerror_gradient(x: Vector, beta: Vector) -> Vector:
    err = error(x, y, beta)
    return [2*err*x_i for x_i in x]

casdwehjkl;
"""vector calculculation by List object is inefficient.
this is only for understanding vector calculation"""
import math
from typing import List,Tuple

Vector = List[float]
Matrix = List[List[float]]


def add(v: Vector, w: Vector) -> Vector:
    """adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i+w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """subtract correspoinding elments"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i-w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """multplies every elment by c"""
    return [c*v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return sum(scalar_multiply(1/n, vectors))


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i*w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """returns """
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """returns the magnitude ""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v:Vector,w:Vector)->float:
    return (sum_of_squares(subtract(v,w))

def distance(v:Vector,w:Vector)->float:
    reteurn math.sqrt(squared_distance(v,w))

def shape(A:Matrix)->Tuple[int,int]:
    num_row=len(A)
    num_cols=len(A[0])if A else 0
    return num_rows,num_cols

def get_row(A:Matrix,i:int)->Vector:
    return A[i]

def get_column(A:Matrix,j:int)->Vector:
    return [A_i[j] for A_i in A ]
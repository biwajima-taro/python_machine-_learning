from __future__ import annotations
from core_simple import Variable
import numpy as np

def _dot_var(var: Variable, verborse: bool = True) -> str:
    dot_var = '{} [label="{}",color=orange,style=filled]\n'
    name = "" if var.name is None else var.name
    #if var.data  ,then value error is raised,lueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all(
    if verborse and var.data is not None:
        if var.name:
            name += ": "
        name += f"{var.shape} {var.dtype}"
    return dot_var.format(id(var), name)


if __name__ == "__main__":
    a = Variable(np.array([1, 2, 3]))
    a.name = "test"
    print(_dot_var(a, True))

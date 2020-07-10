from typing import List
import numpy as np
import attr

@attr.s
class Variable:
    data:np.ndarray=attr.ib()
    
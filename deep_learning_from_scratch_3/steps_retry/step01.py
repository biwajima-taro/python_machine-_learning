from dataclasses import dataclass
from typing import Any
import numpy as np


@dataclass
class Variable:
    data:Any


if __name__=="__main__":
    data=np.array(1.0)
    x=Variable(data)
    print(x.data)

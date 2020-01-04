# chapter10
from typing import List, Dict
from collections import Counter
import math
import matplotlib.pyplot as plt


def bucket_size(point: float, bucket_size: float) -> float:
    return bucket_size*math.floor(point/bucket_size)

def make_histogram(points:List[float],bucket_size:float)->Dict[float]
    return Couunter(bucket_size(point,bucket_sizef))
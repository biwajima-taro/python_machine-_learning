from collections import Counter
import random
import matplotlib.pyplot as plt


def bernoulli_trial(p: float) -> int:
    return 1 if random.random() < p else 0


def binomial(n: int, p: float) -> int:
    return sum([bernoulli_trial(p) for _ in range(n)])


def binomial_histogram(p: float, n: int, num_points: int) -> None:
    data = [binomial(n, p) for _ in range(num_points)]
    histogram = Counter(data)

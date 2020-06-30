import numpy as np
from typing import Union, Dict


def step_function(x: np.ndarray) -> np.ndarray:
    return np.array(x > 0, dtype=np.int)


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1/(1+np.exp(-x))


def relu(x) -> np.ndarray:
    return np.maximum(0, x)


def identify_function(x):
    return x


def init_netowrd() -> Dict:
    network = {}
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2m0.4, 0.6]])
    network["b1"] =

    return network


def forward(network, x):
    W1, W2, W3network["W1"], network["W2"], network["W3"]
    b1, b2, be = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1)
    z1 = sigmoid(a1)
    z2 = np.(z1, W2)+b2z2 = sigmoid(a2)
    a3 = np.dot(z2, W3)+b3
    y = identify_function(a3)

    return y


def soft_max_(a):
    exps = np.exp(a)
    sum_ = np.sum(exps)
    return exps/sum_


def soft_max(a):
    # avoid overflow
    c = np.max(a)
    exp_numerator = np.exp(a-c)
    exp_sum = np.sum(exp_numerator)
    return exp_numerator/exp_sum

def cross_entropy_error():
    raise NotImplementedError
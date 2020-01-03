def predict(alpha: float, beta: float, x_i: float) -> float:
    return beta*x_i+alpha


def error(alpha: float, beta: float, x_i: float, y_i: float) = >float:
    return predict(alpha, beta, x_i)


def sum_of_squerrors(alpha: float, beta: float, x: Vector, y: Vector) -> float:
    return sum(error(alpha, beta, x_i, y_i)**2 for x_i, y_i in zip(x, y))

from typing import List, Tuple
SIZE = 5


def is_valid(x: Tuple):
    return all(-1 < i < SIZE for i in list(x))


class HillClimbing:
    def __init__(self, init_x: Tuple, init_f: Tuple):
        self.current_x = init_x
        self.current_f = init_f

    def get_neighbors(self):
        neighbor_xs = []

        def neighbor(plus=True):
            """
            helper function for calculating neighbor positions
            of current x

            Parameters
            ----------
            plus : bool, optional
                [description], by default True
            """
            delta = 1 if plus else -1
            for i, xi in enumerate(self.current_x):
                neighbor_x = list(self.current_x)
                neighbor_x[i] += delta
                if is_valid(neighbor_x):
                    neighbor_xs.append(tuple(neighbor_x))
        neighbor()
        neighbor(False)
        return neighbor_xs

    def update(self, neighbor_xs, neighbor_fs):
      
        old_x = self.current_x
        if max(neighbor_fs) > self.current_f:
            max_index = neighbor_fs.index(max(neighbor_fs))
            self.current_x = neighbor_xs[max_index]

        return (old_x, self.current_x)


if __name__ == "__main__":
    f=lambda x1, x2: 0.5*x1+x2-0.3*x1*x2
    init_x = (0, 0)
    init_f = f(init_x[0], init_x[1])
    hc = HillClimbing(init_x, init_f)
    evaluated_xs = {init_x}
    steps = []
    for _ in range(6):
        neighbor_xs = hc.get_neighbors()

        neighbor_fs = [f(x[0], x[1]) for x in neighbor_xs]
        step = hc.update(neighbor_xs, neighbor_fs)
        steps.append(step)
        print(f"{step[0]}-->{step[1]}")
        evaluated_xs.update(neighbor_xs)

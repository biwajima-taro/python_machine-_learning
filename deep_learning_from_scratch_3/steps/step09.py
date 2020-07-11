from .step08 import Variable, Square, Exp
import attr


def square(x: Variable) -> Variable:
    f = Square()
    return f(x)


def exp(x: Variable) -> Variable:
    f = Exp()
    return f(x)


def as_array(x: np.ndarray) -> np.ndarray:
    """
     convert x into ndarray if necessary

    Parameters
    ----------
    x : np.ndarray
        [description]

    Returns
    -------
    np.ndarray
        [description]
    """
    if np.isscalar(x):
        return np.array(x)
    return x


@attr.s
class Function:
    input: Variable = attr.ib(init=None)
    output: Variable = attr.ib(init=None)

    def forward(self):
        raise NotImplemented

    def backward(self):
        raise NotImplemented

    def __call__(self, input: Variable) -> Variable:
        self.input = input
        y = self.forward(input.data)
        output = Variable(as_array(y))
        output.set_creator(self)
        self.output = output
        return output

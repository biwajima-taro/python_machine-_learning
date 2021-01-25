from step01 import Variable
import numpy as np

class Function:
    def __call__(self,input:Variable):

        x=input.data

        y=self.forward(x)
        output=Variable(y)
        return output

    def forward(self,x):
        #forward method is implemented at each child class
        raise NotImplementedError()


class Square(Function):
    def forward(self,x):
        return x**2


if __name__=="__main__":
    x=Variable(np.array(10))
    f=Function()
    y=f(x)
    print(type(y))
    print(y.data)

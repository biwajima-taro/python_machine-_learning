
import attr
import numpy as np


@attr.s
class Affine:
    W:np.ndarray=attr.ib()
    b:np.ndarray=attr.ib()
    x:np.ndarray=attr.ib(default=None)
    dw:np.ndarray=attr.ib(default=None)
    db:np.ndarray=attr.ib(default=None)
def forward(self,x:np.ndarary):
    self.x=x
    out=np.dot(x,self.w)+self.b

def backward(self,dout):
    dx=np.dot(dout,self.w.T)
    self.dw=np.dot(self.x.T,dout)
    self.db=np.sum(dout,axis=0)
    return dx
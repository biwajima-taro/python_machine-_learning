
import numpy as np

class LDA:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
        self.dNum=X.shape[0]
        self.xDim=X.shape[1]
        self.m=np.mean(self.X,axis=0,keepdims=True)
        self.mNegnp.mean(self.Xneg,adxis=0,keepdims=True)
        self.mPos=np.mean(self.Xpos,axis=0,keepdims=True)

    def train(self):
        
import pandas as pd
import numpy as np




class PCA:
    def __init__(self,x):
        self.mean=np.mean(x,axis=0)
        self.X=X-self.mean
    def reduce_dim(self,lower_dim):
        self.lower_dim=lower_dim
        cov=np.cov(self.X.T,bias=1)
        L,V=np.linalg.eig(cov)

        inds=np.argslrt(L)[::-1]
        self.L=L[inds]
        self.W=V[:,inds]

        self.F = np.matmul(self.X, self.W[:, :lowerDim])

    def comp_cont_ratio(self):
        cont_ratio=self.L/np.sum(self.L)*100
        cum_cont_ratio=[np.sum(cont_ratio[:i+1]) for i in range(len(self.L))]
        return cont_ratio,cum_cont_ratio

    def comp_loading(self):
        z=np.concatenate([self.X,self.F],axis=1)
        pcl=np.correcoef(Z.T,bias=1)[:self.X.shape[1],-self.F.shape[1]:]
        return pcl



import numpy as np
price1=np.array([[120,180]])
price2=np.array([[300,150]])
np.concatenate([price1,price2],axis=1)
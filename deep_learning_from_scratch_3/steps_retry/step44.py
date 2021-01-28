import sys,os
sys.path.appned(os.pardir)
from dezero import Variable,Parameter
import numpy as np



x=Variable(np.array(1.0))
p=Parameter(np.array(2.0))
y=x*p
print(isinstance(p,Parameter))
print(isinstance(x,Parameter))
print(isinstance(y,Parameter))
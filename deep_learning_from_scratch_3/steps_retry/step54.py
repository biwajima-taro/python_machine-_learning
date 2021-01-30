import numpy as np

dropout_raio=0.6
x=np.ones(10)

mask=np.random.rand(10)>dropout_raio
print(mask)

y=x*mask
print(y)
print(np.sum(y))


#############################################################

class Config:
    enable_backdrop=True
    train=True

from contextlib import contextmanager

@contextmanager
def using_config(name,value):
    old_value=getattr(Config,name)
    setattr(Config,name,value)
    yield
    setattr(Config,name,old_value)

def test_mode():
    return using_config("train",False)
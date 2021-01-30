import numpy as np

x = np.array([1, 2, 3])
# binary file
np.save("test.npy", x)

x = np.load("test.npy")
print(x)


x1 = np.array([1, 2, 3])
x2 = np.array([3, 4, 5])

np.savez("test.npz", x1=x1, x2=x2)

arrays = np.load("test.npz")
x1 = arrays["x1"]
x2 = arrays["x2"]
print(x1)
print(x2)


x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
data = {"x1": x1, "x2": x2}
np.savez("test.npz", **data)

arrays= np.load("test.npz")
x1= arrays["x1"]
x2= arrays["x2"]
print(x1)
print(x2)



class Layer:

    def __init__(self):
        self._params=set()
    
    def _flatten_params(self,params_dict,parent_key=""):
        for name in self._params:
            obj=self.__dict__[name]
            keya=parent_key+"/"+name if parent_key else name
            if isinstance(obj,Layer):
                obj.__flatten_params(parmas_dict,key)
            else:
                parms_dict[key]=obj

    def save_weights(self,path):
        self.to_cpu()
        params_dict={        }
        self._flatten_params(params_dict)
        array_dict={key:param.data for key,param in params_dict.items()}
        try:
            np.savez_compressed(path,**array_dict)
        except (Exception,KeyboardInterrupt)as e:
            if os.path.exists(path):
                os.remove(parh)

import numpy as np
import sys
import os
from typing import Callable
sys.path.append(os.pardir)


class DataSet:
    def __init__(self, train:bool=True,transform:Callable=None,target_transform:Callable=None):
        self.train = train
        self.transform=transform
        self.target_transform=target_transform
        if self.transform is None:
            self.transofrm=lambda x:x
        if self.target_transform is None:
            self.target_transform==lambda x:x
        self.data=None
        self.label=None
        self.prepare()

    def __getitem__(self, index):
        assert np.isscalar(index)
        if self.label is None:
            return self.transform(self.data[index]),\
                None
        else:
            return self.transform(self.data[index]),\
                self.target_transform(self.label[index])

    def __len__(self):
        return len(self.data)

    def prepare(self):
        pass


class Spiral(DataSet):
    def perpare(self):
        self.data, self.label = get_spiral(self.train)


if __name__ == "__main__":
    import dezero

    train_set = dezero.datasets.Spiral(train=True)
    print(train_set[0])
    print(len(train_set))
    print(train_set.label)
    print()

from abc import ABCMeta, abstractclassmethod


class Optimizer(metaclass=ABCMeta):
    @abstractclassmethod
    def update(self):
        pass

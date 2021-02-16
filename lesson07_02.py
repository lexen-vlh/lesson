from abc import ABC, abstractmethod
from typing import Any


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def material(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def _calc(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, size: Any):
        self._size = size
        self._material = None
        self._clothes.append(self)

    @property
    def material(self) -> float:
        if not self._material:
            self._calc()
        return self._material

    @property
    def size(self) -> Any:
        return self._size

    @size.setter
    def size(self, size: Any):
        self._size = size
        self._material = None

    def _calc(self):
        raise NotImplemented

    @property
    def all(self):
        return sum([i.material for i in self._clothes])


class Coat(Clothes):
    @property
    def V(self) -> Any:
        return self.size

    @V.setter
    def V(self, size: Any):
        self.size = size

    def _calc(self):
        self._material = round((self.size/6.5 + 0.5), 1)

    def __str__(self):
        return 'Для пошива пальто ' + str(self.size) + ' размера требуется ' + str(self.material) + \
               ' условных едениц площади ткани'


class Costume(Clothes):
    @property
    def H(self) -> Any:
        return self.size

    @H.setter
    def H(self, size: Any):
        self.size = size

    def _calc(self):
        self._material = round((self.size*2 + 0.3), 1)

    def __str__(self):
        return 'Для пошива костюма под рост ' + str(self.size) + ' требуется ' + str(self.material) + \
               ' условных едениц площади ткани'


coat = Coat(54)
print(coat)

coat.V = 34
print(coat)

сostume = Costume(44)
print(сostume)

сostume.H = 24
print(сostume)

print(coat.all)
print(сostume.all)

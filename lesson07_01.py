from typing import List


class Matrix:
    _result = []

    def __init__(self, l: List[List]):
        self.__matrix = l
        self.__size = frozenset([(len(self.__matrix), len(i)) for i in self.__matrix])
        if len(self.__size) != 1:
            raise ValueError('Неверный размер матрицы!')

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, i)) for i in self.__matrix])

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(other.__class__.__name__ + ' - несовместимый тип!')
        if self.__size != other.__size:
            raise ValueError('Размеры матриц не совпадают!')
        for i in zip(self.__matrix, other.__matrix):
            self._result.append([sum([j, k]) for j, k in zip(*i)])
        return Matrix(self._result)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(m1, '\n')
print(m2, '\n')
print(m1 + m2)

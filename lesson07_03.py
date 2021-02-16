class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count <= other._count:
            print(self._count, '-', other._count, '<- разность количества ячеек двух клеток меньше либо равна нулю')
        else:
            return Cell(self._count - other._count)

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, cells: int) -> str:
        rows = self._count // cells
        remainder = self._count % cells
        return '\n'.join(['*' * cells] * rows + (['*' * remainder] if remainder else []))

    def __str__(self) -> str:
        return 'Клетка состоит из ' + str(self._count) + ' ячеек'


c1 = Cell(5)
c2 = Cell(7)
print(c1)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)
print((c1 + c2).make_order(10))

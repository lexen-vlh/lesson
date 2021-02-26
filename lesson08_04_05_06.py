class WarehouseError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return self.error


class AddWarehouseError(WarehouseError):
    def __init__(self, error):
        self.error = f"Ошибка добавления {error}"


class MoveWarehouseError(WarehouseError):
    def __init__(self, error):
        self.error = f"Ошибка перемещения {error}"


class Warehouse:
    def __init__(self):
        self.__warehouse = []

    def add(self, lots):
        if not all([isinstance(lots, OfficeEquipment) for lots in lots]):
            raise AddWarehouseError(f"Это не оргтехника")
        self.__warehouse.extend(lots)

    def move(self, ind: int, dept: str):
        if not isinstance(ind, int):
            raise MoveWarehouseError(f"{ind} недопустимый номер")
        if ind > len(self.__warehouse):
            raise MoveWarehouseError(f"{ind} номер больше чем есть на складе")

        lot: OfficeEquipment = self.__warehouse[ind]
        if lot.dept:
            raise MoveWarehouseError(f"{lot} уже перемещено в отдел {lot.dept}")
        lot.dept = dept

    def __getitem__(self, ind):
        if not isinstance(ind, int):
            raise MoveWarehouseError(f"{ind} недопустимый номер")
        if ind > len(self.__warehouse):
            raise MoveWarehouseError(f"{ind} номер больше чем есть на складе")

        return self.__warehouse[ind]

    def __delitem__(self, ind):
        if not isinstance(ind, int):
            raise MoveWarehouseError(f"{ind} недопустимый номер")
        if ind > len(self.__warehouse):
            raise MoveWarehouseError(f"{ind} номер больше чем есть на складе")

        del self.__warehouse[ind]

    def __iter__(self):
        return self.__warehouse.__iter__()

    def filter(self, **kwargs):
        for i, j in enumerate(self):
            obj: OfficeEquipment = j
            if all([obj.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield i, j

    def count(self):
        return len(self.__warehouse)

    def __str__(self):
        return f"Сейчас на складе {len(self.__warehouse)} едениц техники"


class OfficeEquipment:
    __required = ("device", "vendor", "model")

    def __init__(self, device: str = None, vendor: str = "", model: str = "", price: float = 0):
        self.device = device
        self.vendor = vendor
        self.model = model
        self.price = price
        self.dept = None

    def __setattr__(self, key, value):
        if key in self.__required and not value:
            raise AttributeError(f"'{key}' не должно быть False")
        object.__setattr__(self, key, value)

    @staticmethod
    def valid(cnt):
        if not isinstance(cnt, int):
            AddWarehouseError(f"{type(cnt)} - количество должно быть типа int")

    @classmethod
    def create(cls, cnt, **properties):
        cls.valid(cnt)
        return [cls(**properties) for _ in range(cnt)]

    def __str__(self):
        return f"тип: {self.device}, производитель: {self.vendor}, модель: {self.model}, цена: {self.price}"


class Printer(OfficeEquipment):
    func = [True, False]

    def __init__(self, **kwargs):
        super().__init__(device='printer', **kwargs)


class Scanner(OfficeEquipment):
    func = [False, True]

    def __init__(self, **kwargs):
        super().__init__(device='scanner', **kwargs)


class Xerox(OfficeEquipment):
    func = [True, True]

    def __init__(self, **kwargs):
        super().__init__(device='xerox', **kwargs)


warehouse = Warehouse()
warehouse.add(Printer.create(2, vendor='hp', model='1102', price=400))
warehouse.add(Scanner.create(3, vendor='epson', model='400', price=200))
warehouse.add(Xerox.create(4, vendor='canon', model='mfp-200', price=600))
warehouse.move(warehouse.count()-1, 'ОИТ')
del warehouse[0]

print('Техника не переданная в отделы:')
for ind, lot in warehouse.filter(dept=None):
    print(ind, lot)

print('Техника находящаяся в ОИТ:')
for ind, lot in warehouse.filter(dept='ОИТ'):
    print(ind, lot)

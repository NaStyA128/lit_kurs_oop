import types


class Properties:

    material = None
    length = None
    width = None
    coordinate = {'top_left': None,
                  'bottom_right': None}

    def __init__(self, **kwargs):
        self.material = kwargs.pop('material')
        self.coordinate = kwargs.pop('coordinate')
        x = self.coordinate['bottom_right'][0] - self.coordinate['top_left'][0]
        y = self.coordinate['bottom_right'][1] - self.coordinate['top_left'][1]
        self.length = float(x)
        self.width = float(y)


class Furniture(Properties):

    weight = None

    def __init__(self, **kwargs):
        self.weight = float(kwargs.pop('weight'))
        super().__init__(**kwargs)


class Bed(Furniture):

    linen = None    # белье
    mattress = None    # матрац

    def __init__(self, **kwargs):
        self.linen = bool(kwargs.pop('linen'))
        self.mattress = bool(kwargs.pop('mattress'))
        super().__init__(**kwargs)


class Table(Furniture):

    number_of_legs = None    # количество ножек
    coating = None    # покрытие

    def __init__(self, *kwargs):
        self.number_of_legs = int(kwargs.pop('number_of_legs'))
        self.coating = kwargs.pop('coating')
        super().__init__(**kwargs)


class Cupboard(Furniture):

    number_of_shelves = None    # количество полок
    coating = None    # покрытие

    def __init__(self, **kwargs):
        self.number_of_shelves = int(kwargs.pop('number_of_shelves'))
        self.coating = kwargs.pop('coating')
        super().__init__(**kwargs)


class Chair(Furniture):

    upholstery = None    # обивка
    number_of_legs = None    # количество ножек

    def __init__(self, **kwargs):
        self.upholstery = kwargs.pop('upholstery')
        self.number_of_legs = int(kwargs.pop('number_of_legs'))
        super().__init__(**kwargs)


class Nightstand(Furniture):

    coating = None    # покрытие
    number_of_boxes = None    # количество ящиков

    def __init__(self, **kwargs):
        self.coating = kwargs.pop('coating')
        self.number_of_boxes = int(kwargs.pop('number_of_boxes'))
        super().__init__(**kwargs)


class Bath(Furniture):

    volume = None
    shower = None    # душ

    def __init__(self, **kwargs):
        self.volume = float(kwargs.pop('volume'))
        self.shower = bool(kwargs.pop('shower'))
        super().__init__(**kwargs)


class Sink(Furniture):

    mixer = None    # смеситель
    mirror = None    # зеркало

    def __init__(self, **kwargs):
        self.mixer = bool(kwargs.pop('mixer'))
        self.mirror = bool(kwargs.pop('mirror'))
        super().__init__(**kwargs)


class Toilet(Furniture):

    cover = None    # крышка

    def __init__(self, **kwargs):
        self.cover = bool(kwargs.pop('cover'))
        super().__init__(**kwargs)


class Appliances(Properties):

    category = None    # категория
    provider = None    # производитель
    power = None    # мощность (W or Вт)
    mean_time = None    # среднее время работы (hours/day)
    weight = None
    energy = None

    def __init__(self, **kwargs):
        self.power = float(kwargs.pop('power'))
        self.weight = float(kwargs.pop('weight'))
        self.category = kwargs.pop('category')
        self.provider = kwargs.pop('provider')
        super().__init__(**kwargs)

    def energy_consumption(self):
        a = self.power * self.mean_time
        a /= 1000
        a *= 30    # kWh / month
        self.energy = a


class Refrigerator(Appliances):

    type = None    # двухкамерный, морозилка
    max_temp = None
    min_temp = None
    capacity = None    # вместимость

    def __init__(self, **kwargs):
        self.type = kwargs.pop('type')
        self.max_temp = float(kwargs.pop('max_temp'))
        self.min_temp = float(kwargs.pop('min_temp'))
        self.capacity = float(kwargs.pop('capacity'))
        super().__init__(**kwargs)


class Microwave(Appliances):

    clock = None

    def __init__(self, **kwargs):
        self.clock = bool(kwargs.pop('clock'))
        super().__init__(**kwargs)


class Stove(Appliances):

    type = None    # электронная, газовая
    number_of_burners = None    # количество конфорок
    oven = None    # духовка

    def __init__(self, **kwargs):
        self.type = kwargs.pop('type')
        self.number_of_burners = int(kwargs.pop('number_of_burners'))
        self.oven = bool(kwargs.pop('oven'))
        super().__init__(**kwargs)


class Windows(Properties):

    type = None    # окно / дверь
    weight = None

    def __init__(self, **kwargs):
        self.type = kwargs.pop('type')
        self.weight = float(kwargs.pop('weight'))
        super().__init__(**kwargs)


class Room(Properties):

    furniture = None
    windows = None
    height = None

    def __init__(self, **kwargs):
        self.furniture = kwargs.pop('furniture')
        self.windows = kwargs.pop('windows')
        self.height = float(kwargs.pop('height'))
        super().__init__(**kwargs)

    @property
    def volume(self):
        return self.length * self.width * self.height

    @property
    def weight(self):
        s = sum([f.weight for f in self.furniture])
        s += sum(w.weight for w in self.windows)
        return s

    @property
    def energy(self):
        pass


class Kitchen(Room):
    pass


class Bathroom(Room):
    pass


class Restroom(Room):
    pass


class Bedroom(Room):
    pass


class House(Properties):

    rooms = None

    def __init__(self, **kwargs):
        self.rooms = kwargs['rooms']

    @property
    def total_volume(self):
        return sum([room.volume for room in self.rooms])

    @property
    def total_weight(self):
        return sum([room.weight for room in self.rooms])


house = House(rooms=[
    Kitchen(furniture=[
        Refrigerator(type='cool',
                     max_temp=5,
                     min_temp=-5,
                     capacity=100,
                     material='metal',
                     coordinate={'top_left': (0, 0),
                                 'bottom_right': (100, 80)},
                     category='Kitchen',
                     provider='Beko',
                     weight=10,
                     power=250,
                     mean_time=5)
        ],
        windows=[
            Windows(type='window',
                    material='glass',
                    coordinate={'top_left': (0, 0),
                                'bottom_right': (100, 80)},
                    weight=10)
        ],
        height=300,
        material='brick',
        coordinate={'top_left': (0, 0),
                    'bottom_right': (600, 600)}
    )
])

# print(type(house) == types)
print('Volume of house:', house.total_volume)
print('Weight of house:', house.total_weight)

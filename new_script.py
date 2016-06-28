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
        self.length = x
        self.width = y


class Furniture(Properties):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Bed(Furniture):

    linen = None    # белье
    mattress = None    # матрац

    def __init__(self, **kwargs):
        self.linen = kwargs.pop('linen')
        self.mattress = kwargs.pop('mattress')
        super().__init__(**kwargs)


class Table(Furniture):

    number_of_legs = None    # количество ножек
    coating = None    # покрытие

    def __init__(self, *kwargs):
        self.number_of_legs = kwargs.pop('number_of_legs')
        self.coating = kwargs.pop('coating')
        super().__init__(**kwargs)


class Cupboard(Furniture):

    number_of_shelves = None    # количество полок
    coating = None    # покрытие

    def __init__(self, **kwargs):
        self.number_of_shelves = kwargs.pop('number_of_shelves')
        self.coating = kwargs.pop('coating')
        super().__init__(**kwargs)


class Chair(Furniture):

    upholstery = None    # обивка
    number_of_legs = None    # количество ножек

    def __init__(self, **kwargs):
        self.upholstery = kwargs.pop('upholstery')
        self.number_of_legs = kwargs.pop('number_of_legs')
        super().__init__(**kwargs)


class Nightstand(Furniture):

    coating = None    # покрытие
    number_of_boxes = None    # количество ящиков

    def __init__(self, **kwargs):
        self.coating = kwargs.pop('coating')
        self.number_of_boxes = kwargs.pop('number_of_boxes')
        super().__init__(**kwargs)


class Appliances(Properties):

    category = None    # категория
    provider = None    # производитель

    def __init__(self, **kwargs):
        self.category = kwargs.pop('category')
        self.provider = kwargs.pop('provider')
        super().__init__(**kwargs)


class Refrigerator(Appliances):

    type = None    # двухкамерный, морозилка
    max_temp = None
    min_temp = None
    capacity = None    # вместимость

    def __init__(self, **kwargs):
        self.type = kwargs.pop('type')
        self.max_temp = kwargs.pop('max_temp')
        self.min_temp = kwargs.pop('min_temp')
        self.capacity = kwargs.pop('capacity')
        super().__init__(**kwargs)


class Microwave(Appliances):

    power = None    # мощность

    def __init__(self, **kwargs):
        self.power = kwargs.pop('power')
        self.clock = kwargs.pop('clock')
        super().__init__(**kwargs)


class Stove(Appliances):

    type = None    # электронная, газовая
    number_of_burners = None    # количество конфорок
    oven = None    # духовка

    def __init__(self, **kwargs):
        self.type = kwargs.pop('type')
        self.number_of_burners = kwargs.pop('number_of_burners')
        self.oven = kwargs.pop('oven')
        super().__init__(**kwargs)


class Bath(Appliances):

    volume = None
    shower = None    # душ

    def __init__(self, **kwargs):
        self.volume = kwargs.pop('volume')
        self.shower = kwargs.pop('shower')
        super().__init__(**kwargs)


class Sink(Appliances):

    mixer = None    # смеситель
    mirror = None    # зеркало

    def __init__(self, **kwargs):
        self.mirror = kwargs.pop('mirror')
        self.mixer = kwargs.pop('mixer')
        super().__init__(**kwargs)


class Toilet(Appliances):

    cover = None    # крышка

    def __init__(self, **kwargs):
        self.cover = kwargs.pop('cover')
        super().__init__(**kwargs)


class Windows(Properties):

    type = None    # окно / дверь

    def __init__(self, **kwargs):
        self.type = kwargs.pop('type')
        super().__init__(**kwargs)


class Room(Properties):

    furniture = None
    windows = None
    height = None

    def __init__(self, **kwargs):
        self.furniture = kwargs.pop('furniture')
        self.windows = kwargs.pop('windows')
        self.height = kwargs.pop('height')
        super().__init__(**kwargs)

    @property
    def volume(self):
        return self.length * self.width * self.height


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
                     provider='Beko')
        ],
        windows=[
            Windows(type='window',
                    material='glass',
                    coordinate={'top_left': (0, 0),
                                'bottom_right': (100, 80)})
        ],
        height=300,
        material='brick',
        coordinate={'top_left': (0, 0),
                    'bottom_right': (600, 600)}
    )
])

print(house.total_volume)

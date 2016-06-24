class Properties:

    material = None
    length = None
    width = None
    coordinate = {'top_left': None,
                  'bottom_right': None}

    def __init__(self, **kwargs):
        self.material = kwargs['material']
        self.coordinate = kwargs['coordinate']
        x = kwargs['coordinate']['bottom_right'][0] - kwargs['coordinate']['top_left'][0]
        y = kwargs['coordinate']['bottom_right'][1] - kwargs['coordinate']['top_left'][1]
        self.length = x
        self.width = y


class Furniture(Properties, object):

    def __init__(self, **kwargs):
        Properties.__init__(self, **kwargs)


class Bed(Furniture):

    linen = None    # белье
    mattress = None    # матрац

    def __init__(self, **kwargs):
        Furniture.__init__(self, **kwargs)
        self.linen = kwargs['linen']
        self.mattress = kwargs['mattress']


class Table(Furniture):

    number_of_legs = None    # количество ножек
    coating = None    # покрытие

    def __init__(self, *kwargs):
        Furniture.__init__(self, **kwargs)
        self.number_of_legs = kwargs['number_of_legs']
        self.coating = kwargs['coating']


class Cupboard(Furniture):

    number_of_shelves = None    # количество полок
    coating = None    # покрытие

    def __init__(self, **kwargs):
        Furniture.__init__(self, **kwargs)
        self.number_of_shelves = kwargs['number_of_shelves']
        self.coating = kwargs['coating']


class Chair(Furniture):

    upholstery = None    # обивка
    number_of_legs = None    # количество ножек

    def __init__(self, **kwargs):
        Furniture.__init__(self, **kwargs)
        self.upholstery = kwargs['upholstery']
        self.number_of_legs = kwargs['number_of_legs']


class Nightstand(Furniture):

    coating = None    # покрытие
    number_of_boxes = None    # количество ящиков

    def __init__(self, **kwargs):
        Furniture.__init__(self, **kwargs)
        self.coating = kwargs['coating']
        self.number_of_boxes = kwargs['number_of_boxes']


class Appliances(Properties, object):

    category = None    # категория
    provider = None    # производитель

    def __init__(self, **kwargs):
        self.category = kwargs['category']
        self.provider = kwargs['provider']


class Refrigerator(Appliances):

    type = None    # двухкамерный, морозилка
    max_temp = None
    min_temp = None
    capacity = None    # вместимость

    def __init__(self, **kwargs):
        Appliances.__init__(self, **kwargs)
        self.type = kwargs['type']
        self.max_temp = kwargs['max_temp']
        self.min_temp = kwargs['min_temp']
        self.capacity = kwargs['capacity']


class Microwave(Appliances):

    power = None    # мощность

    def __init__(self, **kwargs):
        Appliances.__init__(self, **kwargs)
        self.power = kwargs['power']
        self.clock = kwargs['clock']


class Stove(Appliances):

    type = None    # электронная, газовая
    number_of_burners = None    # количество конфорок
    oven = None    # духовка

    def __init__(self, **kwargs):
        Appliances.__init__(self, **kwargs)
        self.type = kwargs['type']
        self.number_of_burners = kwargs['number_of_burners']
        self.oven = kwargs['oven']


class Bath(Appliances):

    volume = None
    shower = None    # душ

    def __init__(self, **kwargs):
        Appliances.__init__(self, **kwargs)
        self.volume = kwargs['volume']
        self.shower = kwargs['shower']


class Sink(Appliances):

    mixer = None    # смеситель
    mirror = None    # зеркало

    def __init__(self, **kwargs):
        Appliances.__init__(self, **kwargs)
        self.mirror = kwargs['mirror']
        self.mixer = kwargs['mixer']


class Toilet(Appliances):

    cover = None    # крышка

    def __init__(self, **kwargs):
        Appliances.__init__(self, **kwargs)
        self.cover = kwargs['cover']


class Windows(Properties, object):

    type = None    # окно / дверь

    def __init__(self, **kwargs):
        Properties.__init__(self, **kwargs)
        self.type = kwargs['type']


class Room(Properties, object):

    furniture = None
    windows = None
    height = None

    def __init__(self, **kwargs):
        Properties.__init__(self, **kwargs)
        self.furniture = kwargs['furniture']
        self.windows = kwargs['windows']
        self.height = kwargs['height']

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


class House(object):

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

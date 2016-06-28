class Properties(object):

    material = None
    length = None
    width = None
    coordinate = {'top_left': None,
                  'bottom_right': None}

    def __init__(self):
        self.material = input('Enter material: ')
        for i in self.coordinate:
            print(i)
            x = float(input('Enter x: '))
            y = float(input('Enter y: '))
            self.coordinate[i] = (x, y)
        x = self.coordinate['bottom_right'][0] - self.coordinate['top_left'][0]
        y = self.coordinate['bottom_right'][1] - self.coordinate['top_left'][1]
        self.length = x
        self.width = y


class Furniture(Properties):

    def __init__(self):
        Properties.__init__(self)


class Bed(Furniture):

    linen = None    # белье
    mattress = None    # матрац

    def __init__(self):
        print('\n\033[1m' + 'Bed' + '\033[0m')
        Furniture.__init__(self)
        self.linen = bool(input('Enter linen (True or False): '))
        self.mattress = bool(input('Enter mattress (True or False): '))


class Table(Furniture):

    number_of_legs = None    # количество ножек
    coating = None    # покрытие

    def __init__(self):
        print('\n\033[1m' + 'Table' + '\033[0m')
        Furniture.__init__(self)
        self.number_of_legs = int(input('Enter the number of legs: '))
        self.coating = input('Enter coating: ')


class Cupboard(Furniture):

    number_of_shelves = None    # количество полок
    coating = None    # покрытие

    def __init__(self):
        print('\n\033[1m' + 'Cupboard' + '\033[0m')
        Furniture.__init__(self)
        self.number_of_shelves = int(input('Enter the number of shelves: '))
        self.coating = input('Enter coating: ')


class Chair(Furniture):

    upholstery = None    # обивка
    number_of_legs = None    # количество ножек

    def __init__(self):
        print('\n\033[1m' + 'Chair' + '\033[0m')
        Furniture.__init__(self)
        self.upholstery = input('Enter upholstery: ')
        self.number_of_legs = int(input('Enter the number of legs: '))


class Nightstand(Furniture):

    coating = None    # покрытие
    number_of_boxes = None    # количество ящиков

    def __init__(self):
        print('\n\033[1m' + 'Nightstand' + '\033[0m')
        Furniture.__init__(self)
        self.coating = input('Enter coating: ')
        self.number_of_boxes = int(input('Enter the number of boxes: '))


class Appliances(Properties):

    category = None    # категория
    provider = None    # производитель

    def __init__(self):
        Properties.__init__(self)
        self.category = input('Enter category: ')
        self.provider = input('Enter provider: ')


class Refrigerator(Appliances):

    type = None    # двухкамерный, морозилка
    max_temp = None
    min_temp = None
    capacity = None    # вместимость

    def __init__(self):
        print('\n\033[1m' + 'Refrigerator' + '\033[0m')
        Appliances.__init__(self)
        self.type = input('Enter type: ')
        self.max_temp = float(input('Enter max temperature: '))
        self.min_temp = float(input('Enter min temperature: '))
        self.capacity = float(input('Enter capacity: '))


class Microwave(Appliances):

    power = None    # мощность

    def __init__(self):
        print('\n\033[1m' + 'Microwave' + '\033[0m')
        Appliances.__init__(self)
        self.power = int(input('Enter power: '))
        self.clock = bool(input('Enter clock (True or False): '))


class Stove(Appliances):

    type = None    # электронная, газовая
    number_of_burners = None    # количество конфорок
    oven = None    # духовка

    def __init__(self):
        print('\n\033[1m' + 'Stove' + '\033[0m')
        Appliances.__init__(self)
        self.type = input('Enter type: ')
        self.number_of_burners = int(input('Enter the number of burners: '))
        self.oven = bool(input('Enter oven (True or False): '))


class Bath(Appliances):

    volume = None
    shower = None    # душ

    def __init__(self):
        print('\n\033[1m' + 'Bath' + '\033[0m')
        Appliances.__init__(self)
        self.volume = float(input('Enter volume: '))
        self.shower = bool(input('Enter shower (True or False): '))


class Sink(Appliances):

    mixer = None    # смеситель
    mirror = None    # зеркало

    def __init__(self):
        print('\n\033[1m' + 'Sink' + '\033[0m')
        Appliances.__init__(self)
        self.mirror = bool(input('Enter mirror (True or False): '))
        self.mixer = bool(input('Enter mixer (True or False): '))


class Toilet(Appliances):

    cover = None    # крышка

    def __init__(self):
        print('\n\033[1m' + 'Toilet' + '\033[0m')
        Appliances.__init__(self)
        self.cover = bool(input('Enter cover (True or False): '))


class Windows(Properties):

    type = None    # окно / дверь

    def __init__(self):
        print('\n\033[1m' + 'Window or door' + '\033[0m')
        Properties.__init__(self)
        self.type = input('Enter type (window or door): ')


class Room(Properties):

    furniture = None
    windows = None
    height = None

    def __init__(self, **kwargs):
        print('\n\033[1m' + 'Room' + '\033[0m')
        Properties.__init__(self)
        self.furniture = kwargs.pop('furniture')
        self.windows = kwargs.pop('windows')
        self.height = float(input('Enter height: '))

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
        self.rooms = kwargs.pop('rooms')

    @property
    def total_volume(self):
        return sum([room.volume for room in self.rooms])


house = House(
    rooms=[
        Kitchen(furniture=[
                    Refrigerator()],
                windows=[
                    Windows()]
                )
    ]
)

print(house.total_volume)

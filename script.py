class Furniture(object):

    material = None
    length = None
    width = None

    def __init__(self, material, length, width):
        self.material = material
        self.length = length
        self.width = width


class Bed(Furniture):

    linen = None

    def __init__(self, linen):
        self.linen = linen


class Table(Furniture):

    number_of_legs = None

    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs


class Cupboard(Furniture):
    pass


class Chair(Furniture):
    pass


class Nightstand(Furniture):
    pass


class Appliances(object):

    category = None
    length = None
    width = None

    def __init__(self, category, length, width):
        self.category = category
        self.length = length
        self.width = width


class Refrigerator(Appliances):
    pass


class Microwave(Appliances):
    pass


class Bath(Appliances):
    pass


class Sink(Appliances):
    pass


class Toilet(Appliances):
    pass


class Room(object):

    furniture = None
    windows = []
    doors = []
    size = []

    def __init__(self, furniture, windows, doors, size=[0, 0, 0]):
        self.furniture = furniture
        self.windows = windows
        self.doors = doors
        self.size = size

    def volume(self):
        return self.size[0]*self.size[1]*self.size[2]


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




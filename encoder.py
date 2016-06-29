import pickle
import json
from abc import ABCMeta, abstractmethod
import building as b


class Encoder(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def load(self, data):
        pass

    @abstractmethod
    def dump(self, obj):
        pass


class PickleEncoder(Encoder):

    def load(self, data):
        with open(data, 'rb') as f:
            return pickle.load(f)

    def dump(self, obj):
        with open('house.pickle', 'wb') as f:
            pickle.dump(obj, f)


class JSONEncoder(Encoder):

    my_classes = []
    my_classes_name = []
    r = None

    def __init__(self):
        for classes in b.__dict__:
            if isinstance(b.__dict__[classes], type):
                if classes != 'Properties' and classes != 'Appliances' and \
                                classes != 'Furniture' and classes != 'Room':
                    self.my_classes_name.append(classes)
                    self.my_classes.append(b.__dict__[classes])

    def load(self, data):
        f = open(data, 'r')
        text = f.read()
        f.close()
        a = self.loading(json.loads(text))
        return eval(a)

    def loading(self, data):
        for d in data:
            return 'b.' + d + '(' + self.func(data[d]) + ')'

    def func(self, data):
        text = ''
        for d in data:
            for i in d:
                text += i
                if i == 'furniture' or i == 'rooms' or i == 'windows':
                    if isinstance(d[i], dict):
                        text += '=['
                        text += self.loading(d[i])
                        text += '], '
                else:
                    text += '='
                    if isinstance(d[i], str):
                        text += "'"
                        text += str(d[i])
                        text += "'"
                    else:
                        text += str(d[i])
                    text += ', '
        return text

    def dump(self, obj):
        # таким образом мы получаем иерархический словарь из объектов и их свойств
        a = self.dumping(obj)
        f = open('house.txt', 'w')
        f.write(json.dumps(a, indent=4))
        f.close()

    def dumping(self, obj):
        a = []
        for i in self.my_classes:
            # проверяем, является ли наш объект
            # объектом одного из классов в building.py
            if isinstance(obj, i):
                # перебираем свойства даного объекта
                for j in obj.__dict__:
                    # если значение этого свойства является списком
                    # (др. объекты этих классов хранятся только в списке в значении!)
                    # furniture=[ b.Refrigerator(...) ]
                    if isinstance(obj.__dict__[j], list):
                        # вызываем эту же функцию для этого объекта
                        # и записываем в список словарь с ключом в виде
                        # свойства объекта, а значение -
                        # это рузультат этой же функции
                        for z in obj.__dict__[j]:
                            a.append({j: self.dumping(z)})
                    # иначе
                    else:
                        # просто записываем в список словарь с ключом в виде
                        # свойства объекта и само значение этого свойства
                        a.append({j: obj.__dict__[j]})
        # записываем в результат список с ключом в виде имени класса объекта
        # и его свойства
        # print(self.r)
        self.r = {type(obj).__name__: a}
        return self.r

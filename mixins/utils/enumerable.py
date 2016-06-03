
class Enumerable:
    def take(self, num_taken):
        new_collect = []
        for number in self:
            if num_taken > 0:
                new_collect.append(number)
                num_taken -= 1
            else:
                return self.__class__(*new_collect)

    def drop(self, n):
        new_collect = []
        for number in self:
            if n > 0:
                n -= 1
            else:
                new_collect.append(number)
        return self.__class__(*new_collect)

    def take_while(self, operation):
        new_collect = []
        for number in self:
            if operation(number):
                new_collect.append(number)
        return self.__class__(*new_collect)

    def drop_while(self, operation):
        new_collect = []
        for number in self:
            if not operation(number):
                new_collect.append(number)
        return self.__class__(*new_collect)

    def map(self, callable):
        map_list = []
        for number in self:
            map_list.append(callable(number))
        return self.__class__(*map_list)

    def filter(self, predicate):
        filter_list = []
        for number in self:
            if predicate(number):
                filter_list.append(number)
        return self.__class__(*filter_list)

    def reduce(self, start_value, operator):
        suma = -start_value
        for number in self:
            suma = operator(number, suma)
        return self.__class__(*[suma])

    # Returns True, if value is in self
    def search(self, value):
        return value in self


class Exensible:
    pass


class Collection(Enumerable, Exensible):
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        return iter(self.args)

    def __eq__(self, other):
        return list(self) == list(other)

    def __add__(self, another):
        return list(self) + another
# collect = Collection(1)
# collect2 = Collection(1, 2)

# print(collect == collect2)
# c = Collection(1, 2, 3)
# print(c == c.map(lambda x: x))
# print(Collection(2) == c.filter(lambda x: x % 2 == 0))
# print(Collection(5) == c.reduce(1, lambda x, y: x + y))
# print(Collection(1, 2) == c.take(2))
# print(Collection(3) == c.drop(2))
# print(Collection(0, 0, 0) == Collection(0, 0, 0, 1).take_while(lambda x: x == 0))
# print(Collection(1) == Collection(0, 0, 0, 1).drop_while(lambda x: x == 0))
# print(Collection(1, 2).search(3))

# c = Collection(1, 2, 3)
# c1 = c + [1, 2, 3]

# print(c1 == Collection(1, 2, 3, 1, 2, 3))

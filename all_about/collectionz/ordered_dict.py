# OrderedDict: OrderedDict - это словарь, который сохраняет порядок добавления элементов.
# В отличие от обычного словаря, где порядок элементов не гарантирован, OrderedDict запоминает порядок,
# в котором элементы были добавлены. При итерации по OrderedDict элементы будут возвращаться в
# том же порядке, в котором они были добавлены. Например:

from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

for key, value in d.items():
    print(key, value)  # Выводит: a 1, b 2, c 3

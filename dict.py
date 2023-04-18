#  Все о типах данных словарь в Python.

# способы создания словарей:
my_new_dict = dict()
...
# ToDo: дописать потом сюда все способы и кейсы


# Все не магические методы для словарей:
"""
dir(dict)

clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values
"""


# clear(): Удаляет все элементы словаря.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()  # Output: {}

# copy(): Создает копию словаря.
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = my_dict.copy()  # Output: {'a': 1, 'b': 2, 'c': 3}

# fromkeys(seq, value): Создает новый словарь с ключами из seq и значением value.
keys = ['a', 'b', 'c']
values = 0
my_dict = dict.fromkeys(keys, values)
print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# get(key[, default]): Возвращает значение ключа key. Если ключ не найден, возвращает default (по умолчанию None).
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('d', 0)
print(value)  # Output: 0

# items(): Возвращает список кортежей (key, value) для всех элементов словаря.
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# keys(): Возвращает список ключей словаря
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])

# pop(key[, default]): Удаляет ключ key и возвращает соответствующее ему значение. Если ключ не найден, возвращает
# default (по умолчанию возникает ошибка).
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')
print(my_dict)  # Output: {'a': 1, 'c': 3}
print(value)  # Output: 2

# popitem(): Удаляет и возвращает произвольный элемент (key, value) из словаря. Если словарь пуст, возникает ошибка.
my_dict = {'a': 1, 'b': 2, 'c': 3}
item = my_dict.popitem()
print(my_dict)  # Output: {'a': 1, 'b': 2}
print(item)  # Output: ('c', 3)

# setdefault(): этот метод позволяет получить значение ключа, если ключ есть в словаре, или установить значение ключа
# и вернуть его, если ключа нет в словаре.
# Создаем пустой словарь
d = {}
# устанавливаем значение ключа 'a' равным 1
d.setdefault('a', 1)
# выводим словарь
print(d)  # {'a': 1}
# устанавливаем значение ключа 'b' равным 2
d.setdefault('b', 2)
# выводим словарь
print(d)  # {'a': 1, 'b': 2}
# получаем значение ключа 'a'
print(d.setdefault('a'))  # 1

# update(): этот метод объединяет два словаря. Если ключи второго словаря уже есть в первом, то их значения будут
# заменены на значения из второго словаря. Если ключи второго словаря не найдены в первом, то они будут добавлены
# в первый словарь.
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
# объединяем словари
d1.update(d2)
# выводим результат
print(d1)  # {'a': 1, 'b': 3, 'c': 4}

# values() возвращает список значений в словаре. Вот несколько примеров использования этого метода:
# Пример 1:
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values) # выводит dict_values([1, 2, 3])
# Пример 2:
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value) # выводит 1, затем 2, затем 3

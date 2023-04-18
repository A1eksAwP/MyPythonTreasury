#  Все о списковых типах данных в Python.

# способы создания списков:
my_new_list = []
my_list2 = list()
list('8, 7, 6')  # ['8', ',', ' ', '7', ',', ' ', '6']
list((7, 6, 5))  # [7, 6, 5]
list({7: 'семь', 6: 'шесть', 5: 'пять'})  # [7, 6, 5]


# Все не магические методы спискового типа:
"""
dir(list)

append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
"""


# *.append(x): метод добавляет элемент x в конец списка:
l = [1, 2, 3]
l.append(4)  # Output: [1, 2, 3, 4]

# *.clear(): метод удаляет все элементы из списка:
l.clear()  # Output: []

# *.copy(): метод создает и возвращает копию списка:
lst1 = [1, 2, 3]
lst2 = lst1.copy()  # Output: [1, 2, 3]

# *.count(x): метод возвращает количество вхождений элемента x в список:
lst = [1, 2, 3, 2]
print(lst.count(2))  # Output: 2

# *.extend(iterable): метод добавляет элементы из итерируемого объекта iterable в конец списка:
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)  # Output: [1, 2, 3, 4, 5, 6]

# *.index(x[, start[, end]]): метод возвращает индекс первого вхождения элемента x в список.
# Метод принимает необязательные параметры start и end, которые определяют границы поиска:
lst = [1, 2, 3, 2]
print(lst.index(2))  # Output: 1

# *.insert(i, x): метод добавляет элемент x в список на позицию i:
lst = [1, 2, 3]
lst.insert(1, 4)  # Output: [1, 4, 2, 3]

# *.pop([i]): метод удаляет и возвращает элемент с индексом i, если i не указан, удаляется последний элемент списка:
lst = [1, 2, 3]
x = lst.pop()
print(x)  # Output: 3
print(lst)  # Output: [1, 2]

# *.remove(x): метод удаляет первое вхождение элемента x из списка:
lst = [1, 2, 3, 2]
lst.remove(2)  # Output: [1, 3, 2]

# *.reverse(): метод изменяет порядок элементов в списке на обратный:
lst = [1, 2, 3]
lst.reverse()  # Output: [3, 2, 1]

# *.sort(*, key=None, reverse=False): сортирует элементы списка. Можно задать функцию-ключ для сортировки и указать
# порядок сортировки (по убыванию или возрастанию).
my_list = [3, 2, 1]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

my_list = ["cat", "Dog", "apple"]
my_list.sort(key=str.lower)
print(my_list)  # Output: ["apple", "cat", "Dog"]

my_list = ["cat", "Dog", "apple"]
my_list.sort(key=str.lower, reverse=True)
print(my_list)  # Output: ["Dog", "cat", "apple"]

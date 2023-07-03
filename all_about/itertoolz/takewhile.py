import itertools


# itertools.takewhile() - создает итератор, который возвращает элементы из
# итерируемого объекта, пока условие истинно, а затем прекращает возвращать элементы:


numbers = [1, 2, 3, 4, 5]

taken_iter = itertools.takewhile(lambda x: x < 3, numbers)

for item in taken_iter:
    print(item)

# В этом примере функция itertools.takewhile() создает итератор taken_iter, который
# возвращает элементы списка numbers, пока они меньше 3, а затем прекращает возвращать
# элементы. Результатом будут элементы [1, 2].

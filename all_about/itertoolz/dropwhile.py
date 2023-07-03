import itertools


# itertools.dropwhile() - создает итератор, который пропускает элементы из
# итерируемого объекта до тех пор, пока условие истинно, а затем возвращает оставшиеся элементы:


numbers = [1, 2, 3, 4, 5]

dropped_iter = itertools.dropwhile(lambda x: x < 3, numbers)

for item in dropped_iter:
    print(item)

# В этом примере функция itertools.dropwhile() создает итератор dropped_iter, который пропускает
# элементы списка numbers, пока они меньше 3, а затем возвращает оставшиеся элементы.
# Результатом будут элементы [3, 4, 5].

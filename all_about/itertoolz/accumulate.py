import itertools


# itertools.accumulate() - создает итератор, который возвращает накопленные
# значения итерируемого объекта, используя указанную функцию для накопления:


numbers = [1, 2, 3, 4, 5]

accumulated_iter = itertools.accumulate(numbers)

for item in accumulated_iter:
    print(item)

# В этом примере функция itertools.accumulate() создает итератор accumulated_iter, который
# возвращает накопленные значения списка numbers. По умолчанию, используется операция сложения
# для накопления. Результатом будет [1, 3, 6, 10, 15], где каждый элемент -
# сумма предыдущих элементов и текущего.

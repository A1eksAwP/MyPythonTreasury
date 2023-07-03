import itertools


# itertools.islice() - создает итератор, который возвращает выбранные элементы из итерируемого объекта:


numbers = [1, 2, 3, 4, 5]

sliced_iter = itertools.islice(numbers, 2, 4)

for item in sliced_iter:
    print(item)

# В этом примере функция itertools.islice() создает итератор sliced_iter, который
# возвращает элементы списка numbers, начиная с индекса 2 и до индекса 4 (не включая).
# Результатом будут элементы [3, 4].

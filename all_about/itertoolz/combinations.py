import itertools

# itertools.combinations() - создает итератор, который возвращает все
# возможные комбинации элементов итерируемого объекта заданной длины:


letters = ['a', 'b', 'c']

combinations_iter = itertools.combinations(letters, 2)

for item in combinations_iter:
    print(item)

# В этом примере функция itertools.combinations() создает итератор combinations_iter,
# который возвращает все возможные комбинации элементов списка letters длиной 2.
# Результатом будут все возможные комбинации из двух элементов.

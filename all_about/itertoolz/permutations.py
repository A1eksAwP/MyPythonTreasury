import itertools

# itertools.permutations() - создает итератор, который возвращает
# все возможные перестановки элементов итерируемого объекта:

letters = ['a', 'b', 'c']

permutations_iter = itertools.permutations(letters)

for item in permutations_iter:
    print(item)


# В этом примере функция itertools.permutations() создает итератор permutations_iter,
# который возвращает все возможные перестановки элементов из списка letters.
# Результатом будут все возможные комбинации перестановок элементов.

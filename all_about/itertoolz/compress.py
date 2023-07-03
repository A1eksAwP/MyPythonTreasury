import itertools


# itertools.compress() - создает итератор, который возвращает элементы из итерируемого объекта,
# соответствующие булевым значениям из сопоставленного итерируемого объекта:


letters = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, True, False, True]

compressed_iter = itertools.compress(letters, selectors)

for item in compressed_iter:
    print(item)

# В этом примере функция itertools.compress() создает итератор compressed_iter, который возвращает
# элементы списка letters, соответствующие булевым значениям из списка selectors. Результатом будут
# элементы ['a', 'c', 'e'], так как они соответствуют соответствующим True значениям в списке selectors.

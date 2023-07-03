import itertools


# itertools.zip_longest() - создает итератор, который комбинирует элементы из нескольких итерируемых
# объектов в кортежи, заполняя пропущенные значения значением fillvalue:


numbers = [1, 2, 3]
letters = ['a', 'b']

zipped_iter = itertools.zip_longest(numbers, letters, fillvalue='')

for item in zipped_iter:
    print(item)

# В этом примере функция itertools.zip_longest() создает итератор zipped_iter, который комбинирует
# элементы списков numbers и letters в кортежи. Если один список заканчивается раньше другого,
# то fillvalue будет использован для заполнения отсутствующих значений. Результатом будут кортежи
# [(1, 'a'), (2, 'b'), (3, '')].

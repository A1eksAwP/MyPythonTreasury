import itertools

# itertools.chain() - объединение нескольких итерируемых объектов в один последовательный итератор:

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

combined_iter = itertools.chain(numbers, letters)

for item in combined_iter:
    print(item)

# В этом примере функция itertools.chain() объединяет элементы списка numbers и списка letters
# в один последовательный итератор combined_iter, который выводит все элементы последовательно.

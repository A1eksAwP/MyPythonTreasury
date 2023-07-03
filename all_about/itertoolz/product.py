import itertools

# itertools.product() - создает итератор, который возвращает
# декартово произведение элементов нескольких итерируемых объектов:

numbers = [1, 2]
letters = ['a', 'b']

product_iter = itertools.product(numbers, letters)

for item in product_iter:
    print(item)

# В этом примере функция itertools.product() создает итератор product_iter,
# который возвращает все возможные комбинации элементов из списков numbers и letters.
# Результатом будет декартово произведение двух списков, и все комбинации будут выведены.

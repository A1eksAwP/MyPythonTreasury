import itertools

# itertools.groupby() - создает итератор, который группирует элементы итерируемого объекта на основе ключей:


data = [
    ('apple', 'fruit'),
    ('banana', 'fruit'),
    ('carrot', 'vegetable'),
    ('celery', 'vegetable')
]

grouped_iter = itertools.groupby(data, key=lambda x: x[1])

for key, group in grouped_iter:
    print(key, list(group))

# В этом примере функция itertools.groupby() создает итератор grouped_iter,
# который группирует элементы списка data на основе второго элемента каждого кортежа.
# Результатом будет группировка элементов по ключам 'fruit' и 'vegetable'.
# Каждая группа будет представлена ключом и итератором, содержащим элементы этой группы.

import itertools


# itertools.tee() - создает несколько независимых итераторов,
# которые могут проходить по одному и тому же итерируемому объекту:


numbers = [1, 2, 3, 4, 5]

iter1, iter2 = itertools.tee(numbers, 2)

print(list(iter1))  # [1, 2, 3, 4, 5]
print(list(iter2))  # [1, 2, 3, 4, 5]

# В этом примере функция itertools.tee() создает два независимых итератора iter1 и iter2,
# которые могут проходить по элементам списка numbers. Оба итератора будут иметь доступ ко всем элементам списка.

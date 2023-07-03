import itertools

# itertools.cycle() - бесконечный итератор, который постоянно повторяет элементы заданной последовательности:

colors = ['red', 'green', 'blue']

for color in itertools.cycle(colors):
    if color == 'green':
        break
    print(color)

# В этом примере итератор itertools.cycle() будет бесконечно повторять элементы списка colors.
# Цикл будет выполняться до тех пор, пока не будет найден элемент 'green', после чего он выйдет из цикла.

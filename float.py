#  Все о вещественных типах данных в Python.


# способы создания целых чисел:
my_float = 1.2  # на прямую из числа
my_int_to_float = float(2)  # из приведения целого числа к вещественному
my_str_to_float = float('1.2')  # из приведения строкового числа к целому
my_int_str_to_float = float(int('2'))  # из приведения строкового целого числа к вещественному

# математические операции:
x = 1.4
y = 4.4
z = 5.4

my_sum = x + y  # 5.800000000000001
my_sub = x - y  # -3.0000000000000004
my_mul = y * z  # 23.760000000000005
my_div = y / z  # 0.8148148148148149
my_true_div = y // z  # 0.0
my_remains = z % y  # 1.0
my_pow = z ** y  # 1669.2928885428548

abs(-3.5)  # 3.5


# Все не магические методы вещественных чисел:
"""
dir(float):

as_integer_ratio, conjugate, fromhex, hex, imag, is_integer, real
"""


# *.as_integer_ratio(): возвращает кортеж, содержащий числитель и знаменатель, которое представляет вещественное число:
x = 2.75
numerator, denominator = x.as_integer_ratio()
print(numerator, denominator)  # Output: 11 4

# *.conjugate(): метод возвращает комплексно-сопряженное число:
x = 3.0 + 4.0j
print(x.conjugate())  # Output: (3-4j)

# *.fromhex(s): метод принимает строку с шестнадцатеричным представлением числа и возвращает float:
x = float.fromhex('0x1.ffffp+1023')
print(x)  # Output: inf

# *.hex(): метод возвращает шестнадцатеричное представление числа в виде строки:
x = 3.5
print(x.hex())  # Output: '0x1.c000000000000p+1'

# *.imag: метод возвращает мнимую часть числа:
x = 2.5 + 3j
print(x.imag)  # Output: 3.0

# *.is_integer(): метод проверяет, является ли число целым:
x = 3.0
print(x.is_integer())  # Output: True
y = 3.5
print(y.is_integer())  # Output: False

# *.real: метод возвращает действительную часть числа:
x = 2.5 + 3j
print(x.real)  # Output: 2.5

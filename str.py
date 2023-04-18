#  Все о строковых типах данных в Python.
import sys
import string
import pickle
from collections import UserString

# способы создания строки:
my_str = ''  # Пустая строка
next_str = 'new'  # Новая строка
add_str = my_str + next_str  # -> 'new' это конкатенация строк
my_str += next_str  # -> 'new' это конкатенация строк через переопределение переменной
best_str = my_str.join(next_str)  # -> 'new' конкатенация строк через метод *.join(). Работает быстрее чем через "+"
f_str = f'{my_str}{next_str}'  # -> 'new' конкатенация строк через f-строки. Работает быстрее чем через "+"
r_str = r'сырая строка\n\t\r'  # -> 'сырая строка\n\t\r' на ней не будут применяться функциональные символы
b_str = b'123'  # -> b'123' строка для записи в битовый формат

# любую переменную можно ПОПЫТАТЬСЯ привести к строке с помощью функции str()
my_num = 123
# str(my_num) -> '123'
my_list = ['Okay', 'Go']
# str(my_list) -> "['Okay', 'Go']"
my_set = {1, '5', 10.7}
# str(my_set) -> "{1, 10.7, '5'}"
my_dict = {1: 'One', 2: 'Two'}
# str(my_dict) -> "{1: 'One', 2: 'Two'}"
my_tuple = (1, 2, '6', 9, 'Wow')
# str(my_tuple) -> "(1, 2, '6', 9, 'Wow')"
my_bool = True
# str(my_bool) -> 'True'
my_none = None
# str(my_none) -> 'None'


# рассмотрим все основные методы строк:
example = 'TestiNg string 12345 _ %^& OKAY'

# *.split('char') - разбиение строки по символу
example.split()  # -> ['TestiNg', 'string', '12345', '_', '%^&', 'OKAY']
# работает слева направо, принимает в себя аргументы sep=символу, по умолчанию это пробел
# можно ограничить с помощью аргумента maxsplit=число, по умолчанию -1
# возвращает list['str']

# *.replace('это', 'на это') - замена символа, если он встретится в последовательности
example.replace('_', 'нижн.подч.')  # -> 'TestiNg string 12345 нижн.подч. %^& OKAY'
# есть необязательный аргумент третий аргумент count:
example.replace('g', 'GG', 1)  # -> 'TestiNGG string 12345 _ %^& OKAY'

# *.find('что угодно') - вернет индекс ПЕРВОГО СОВПАДЕНИЯ символа в последовательности, если нет то -1
example.find('1')  # -> 15
example.find('10')  # -> -1
# есть похожий метод *.index(), но при отсутствии символа в последовательности возникнет ошибка ValueError

# *.strip('символ') - заменяет найденные в начале и конце последовательности символы (по умолчанию пробелы) на ''
'___UltraMagic___'.strip('_')  # -> 'UltraMagic'

# *.endswith('символ') - логическая проверка, что последние индексы [-len(c):] последовательности совпадают с символами
example.endswith('Y')  # -> True
example.endswith('OKAN')  # -> False
# *.startswith('символ') - логическая проверка, что первые индексы [0:len(c)] последовательности совпадают с символами
example.startswith('Te')  # -> True
example.startswith('te')  # -> False
# у обоих методов есть не обязательные аргументы start= и end=, куда можно вписать индексы

# Все не магические методы строкового типа:
"""
dir(str):

"Стили" = ['capitalize', 'casefold', 'swapcase', 'title', 'upper', 'lower']

"Расположения" = ['center', 'ljust', 'rjust']

"Индексы" = ['find', 'index', 'rfind', 'rindex']

"Логические" = ['startswith', 'endswith', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper']

"Заменяющие" = ['expandtabs', 'format', 'format_map', 'maketrans', 'removeprefix', 'removesuffix', 'replace', 'rstrip',
'strip',  'translate',  'zfill']

"Остальные" = ['count', 'encode', 'join', 'lstrip', 'partition', 'rpartition', 'rsplit', , 'split', 'splitlines']
"""


# ---СТИЛИ---

# *.capitalize(): делает первую букву строки заглавной
"hello world".capitalize()  # -> "Hello world"

# *.casefold(): приводит строку к нижнему регистру и удаляет некоторые особенности букв: акценты и диакритические знаки.
"Héllo Wôrld".casefold()  # -> "hello world"

# *.swapcase(): возвращает новую строку, где все заглавные буквы приведены к строчным, а все строчные буквы - заглавным
'Hello WorlD'.swapcase()  # -> "hELLO wORLd"

# *.title(): возвращает новую строку, в которой каждое слово начинается с заглавной буквы.
"hello world".title()  # -> "Hello World"

# *.upper(): возвращает новую строку, в которой все символы приведены к верхнему регистру.
"hello world".upper()  # -> "HELLO WORLD"

# *.lower(): возвращает строку, все символы которой приведены к нижнему регистру.
"HELLO".lower()  # -> "hello"


# ---РАСПОЛОЖЕНИЯ---

# *.center(width, fillchar): центрирует строку в строке заданной ширины (width), дополняя пустые пространства символами
# fillchar (по умолчанию - пробелами).
"hello".center(10, "-")  # -> "--hello---"

# *.ljust(width, fillchar): выравнивает строку по левому краю, заполняя ее символом fillchar до заданной длины width.
"Hello".ljust(10, "-")  # -> "Hello-----"

# *.rjust(width, fillchar): выравнивает строку по правому краю, заполняя ее символом fillchar до заданной длины width.
"Hello".rjust(10, "-")  # -> "-----Hello"


# ---ИНДЕКСЫ---

# *.find(substring, start, end): находит первое вхождение подстроки substring в строке в диапазоне (start, end) и
# возвращает его индекс. Если подстрока не найдена, возвращает -1.
"hello world".find("world")  # -> 6

# *.index(sub, start, end): находит первое вхождение подстроки sub в строке в заданном диапазоне (start, end)
# и возвращает его индекс. Если подстрока не найдена, вызывает ValueError.
"hello world".index("world")  # -> 6

# *.rfind(substring, start, end): находит последнее вхождение подстроки substring в строке в заданном диапазоне
# (start, end) и возвращает его индекс. Если подстрока не найдена, возвращает -1.
"hello world".rfind("o")  # -> 7

# *.rindex(substring, start, end): находит последнее вхождение подстроки substring в строке в заданном диапазоне
# (start, end) и возвращает его индекс. Если подстрока не найдена, вызывает ValueError.
"hello world".rindex("o")  # -> 7


# ---ЛОГИЧЕСКИЕ---

# *.isalnum(): возвращает True, если все символы в строке являются буквами или цифрами.
"hello123".isalnum()  # -> True

# *.isalpha(): возвращает True, если все символы в строке являются буквами.
"hello".isalpha()  # -> True

# *.isascii(): возвращает True, если все символы в строке являются ASCII-символами.
"hello".isascii()  # -> True

# *.isdecimal(): возвращает True, если все символы в строке являются десятичными цифрами.
"123".isdecimal()  # -> True

# *.isdigit(): возвращает True, если все символы в строке являются цифрами.
"123".isdigit()  # -> True

# *.isidentifier(): возвращает True, если строка является допустимым идентификатором в Python.
"hello_world".isidentifier()  # -> True

# *.islower(): возвращает True, если все буквы в строке являются строчными.
"hello".islower()  # -> True

# *.isnumeric(): возвращает True, если все символы в строке являются числами.
"123".isnumeric()  # -> True

# *.isprintable(): возвращает True, если все символы в строке являются печатаемыми.
"hello".isprintable()  # -> True

# *.isspace(): возвращает True, если все символы в строке являются пробельными.
"   ".isspace()  # -> True

# *.istitle(): возвращает True, если строка начинается с заглавной буквы и все остальные буквы являются строчными.
"Hello World".istitle()  # -> True

# *.isupper(): возвращает True, если все буквы в строке являются заглавными.
"HELLO".isupper()  # -> True

# *.endswith(suffix, start, end): возвращает True, если строка заканчивается подстрокой suffix в заданном (start, end).
"hello world".endswith("world")  # -> True

# *.startswith(prefix[, start[, end]]): возвращает True, если строка начинается с указанного префикса prefix.
# Можно указать необязательные аргументы start и end, которые определяют диапазон поиска.
"hello world".startswith("hello")  # -> True


# ---ЗАМЕНЯЮЩИЕ---

# *.expandtabs(tabsize): заменяет табуляции в строке на заданное количество пробелов (tabsize).
"hello\tworld".expandtabs(4)  # -> "hello   world"

# *.format(*args, **kwargs): форматирует строку, заменяя в ней заполнители {} на значения из переданных аргументов.
name = "Alice"
age = 25
formatted_string = "My name is {0} and I'm {1} years old".format(name, age)
# -> "My name is Alice and I'm 25 years old"

# *.format_map(mapping): аналогичен методу format(), но в качестве аргумента принимает словарь.
values = {"name": "Alice", "age": 25}
"My name is {values['name']} and I'm {values['age']} years old".format_map(values)
# -> "My name is Alice and I'm 25 years old"

# *.maketrans(x[, y[, z]]): возвращает таблицу перевода символов для использования с методами translate().
table = str.maketrans("aeiou", "12345")
"hello".translate(table)  # -> "h2ll4"

# *.strip(): удаляет все пробельные символы в начале и конце строки.
"    Hello    ".strip()  # -> "Hello"

# *.translate(table): возвращает новую строку, в которой все символы заменены в соответствии с таблицей перевода table.
translation_table = str.maketrans("o", "0")
"hello world".translate(translation_table)  # -> "hell0 w0rld"

# *.zfill(width): возвращает новую строку, в которой исходная дополнена слева символами '0' до указанной длины width.
"123".zfill(5)  # -> "00123"

# *.lstrip(): удаляет все пробельные символы в начале строки.
" Hello".lstrip()  # -> "Hello"

# *.rstrip(): удаляет все пробельные символы в конце строки.
"Hello    ".rstrip()  # -> "Hello"

# *.removeprefix(prefix): удаляет указанный префикс prefix из начала строки, если он присутствует.
"Hello World".removeprefix("Hello ")  # -> "World"

# *.removesuffix(suffix): удаляет указанный суффикс suffix из конца строки, если он присутствует.
"Hello World".removesuffix(" World")  # -> "Hello"

# *.replace(old, new[, count]): заменяет все вхождения подстроки old в строке на подстроку new.
# Можно указать необязательный аргумент count, который указывает максимальное количество замен.
"Hello World".replace("o", "X", 1)  # -> "HellX World"


# ---ОСТАЛЬНЫЕ---

# *.count(substring, start, end): возвращает количество вхождений подстроки substring в строке в диапазоне (start, end).
"hello world".count("l")  # -> 3

# *.encode(encoding, errors): кодирует строку в байтовый объект, используя заданную кодировку.
"hello world".encode("utf-8")  # -> b'hello world'

# *.join(iterable): возвращает строку, которая является объединением строк в итерируемом объекте iterable.
' '.join(["Hello", "World"])  # -> "Hello World"

# *.partition(separator): разбивает строку на три части: все, что находится до первого вхождения разделителя separator,
# сам разделитель и все, что находится после него.
"hello world".partition(" ")  # -> ("hello", " ", "world")

# *.rpartition(separator): разбивает строку на три части: все, что находится до последнего вхождения разделителя
# separator, сам разделитель и все, что находится после него.
"hello world".rpartition(" ")  # -> ("hello", " ", "world")

# *.rsplit(sep=None, maxsplit=-1): разбивает строку на список, используя sep как разделитель. Если не указан,
# используется пробел. Можно указать необязательный аргумент maxsplit, который ограничивает количество разбиений.
"hello world".rsplit()  # -> ["hello", "world"]

# *.split(sep=None, maxsplit=-1): разбивает строку на список, используя sep как разделитель (по умолчанию пробел).
# Можно указать необязательный аргумент maxsplit, который ограничивает количество разбиений.
"hello world".split()  # -> ["hello", "world"]

# *.splitlines(keepends=False): разбивает строку на список, используя символы перевода строки.
# Если keepends=True, включает символы перевода строки в результирующие строки.
"hello\nworld".splitlines()  # -> ["hello", "world"]


"""
Далее вещи более сложные, связанные с магическими методами строк из dir(str).
Магические методы - это предопределенные методы класса в языке программирования. В данном случае для type(str).

'__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'
"""


# add(self, other): позволяет складывать две строки с помощью оператора "+".
ex_add = "Hello" + " World"  # "Hello World"


# class(self): возвращает класс объекта.
ex_class = "Hello".__class__  # <class 'str'>


# contains(self, substring): возвращает True, если подстрока substring содержится в строке.
ex_contains = "Hello World"
print("World" in ex_contains)  # True


# delattr(self, name): удаляет атрибут name у объекта.
class MyDelClass:
    my_attribute = "Hello"


obj = MyDelClass()
delattr(obj, "my_attribute")
print(hasattr(obj, "my_attribute"))  # False


# dir(self): возвращает список имен атрибутов и методов объекта.
ex_dir = "Hello World"
dir(ex_dir)  # [..., __magic_methods__, methods, ...]


# doc(self): возвращает строку документации для объекта.
def my_function():
    """This is a docstring"""
    ...


print(my_function.__doc__)  # "This is a docstring"


# eq(self, other): возвращает True, если два объекта равны.
string1 = "Hello"
string2 = "Hello"
print(string1 == string2)  # True


# format(self, format_spec): форматирует строку в соответствии с заданным форматом.
format("Hello", "<10")  # "Hello     "


# ge(self, other): возвращает True, если объект больше или равен другому объекту.
string1 = "Hello"
string2 = "World"
print(string1 >= string2)  # False


# getattribute(self, name): возвращает значение атрибута name объекта.
class MyGetAttributeClass:
    my_attribute = "Hello"


obj = MyGetAttributeClass()
print(obj.my_attribute)  # "Hello"


# getitem(self, key): возвращает значение элемента строки, находящегося по индексу key.
print("Hello World"[6])  # "W"


# getnewargs(self): возвращает кортеж аргументов, передаваемых в конструктор объекта.
class MyGetNewArgsClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getnewargs__(self):
        return self.x, self.y


obj = MyGetNewArgsClass(1, 2)
new_obj = obj.__new__(MyGetNewArgsClass, *obj.__getnewargs__())
print(new_obj.x, new_obj.y)  # 1 2


# getstate(self): возвращает состояние объекта в виде словаря.
class MyGetStateClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getstate__(self):
        return {"x": self.x, "y": self.y}

    def __setstate__(self, state):
        self.x = state["x"]
        self.y = state["y"]


obj = MyGetStateClass(1, 2)
data = pickle.dumps(obj)
new_obj = pickle.loads(data)
print(new_obj.x, new_obj.y)  # 1 2


# gt(self, other): возвращает True, если объект больше другого объекта.
string1 = "Hello"
string2 = "World"
print(string1 > string2)  # False


# hash(self): возвращает хеш-значение объекта.
hash("Hello")  # 6985918441885721357


# init(self): конструктор класса.
class MyInitClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = MyInitClass(1, 2)
print(obj.x, obj.y)  # 1 2


# init_subclass(cls): вызывается при создании подкласса.
class MyParentClass:
    def __init_subclass__(cls):
        print("Subclass created")


class MyChildClass(MyParentClass):
    ...
# Output: "Subclass created"


# iter(self): возвращает итератор для строки.
iterator = iter("OK")
print(next(iterator))  # "O"
print(next(iterator))  # "K"
print(next(iterator))  # StopIteration


# le(self, other): возвращает True, если объект меньше или равен другому объекту.
print("Hello" <= "World")  # True


# len(self): возвращает длину строки.
print(len("Hello World"))  # 11


# lt(self, other): возвращает True, если объект меньше другого объекта.
print("Hello" < "World")  # True


# mod(self, other): возвращает строку, отформатированную с помощью оператора %.
print("Hello, %s" % "World")  # "Hello, World"


# mul(self, other): возвращает строку, повторенную определенное количество раз.
print("Hello" * 3)  # "HelloHelloHello"


# ne(self, other): возвращает True, если объекты не равны.
print("Hello" != "World")  # True


# new(cls, *args, **kwargs): создает новый экземпляр класса.
class MyNewClass:
    def __new__(cls, *args, **kwargs):
        print("Creating new instance")
        return super().__new__(cls)


obj = MyNewClass()
# Output: "Creating new instance"


# reduce(self): используется при сериализации объекта.
class MyReduceClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __reduce__(self):
        return MyReduceClass, (self.x, self.y)


obj_2 = MyReduceClass(1, 2)
data = pickle.dumps(obj)
new_obj = pickle.loads(data)
print(new_obj.x, new_obj.y)  # 1 2


# reduce_ex(self): используется при сериализации объекта.
class MyReduceExClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __reduce_ex__(self, protocol):
        return MyReduceExClass, (self.x, self.y), None, None, None


obj = MyReduceExClass(1, 2)
data = pickle.dumps(obj)
new_obj = pickle.loads(data)
print(new_obj.x, new_obj.y)  # 1 2


# repr(self): возвращает строковое представление объекта.
print(repr("Hello"))  # "'Hello'"


# rmod(self, other): используется при форматировании строк с помощью оператора %.
class MyNumber:
    def __init__(self, num):
        self.num = num

    def __rmod__(self, other):
        return other % self.num


n = MyNumber(5)
print("17 %s n = %s" % ('%', 17 % n))  # "17 % n = 2"
# В этом примере метод __rmod__ вызывается, когда мы используем оператор % для вычисления остатка от деления числа 17
# на объект MyNumber. Мы используем символ % в строке формата для обозначения операции взятия остатка от деления и
# передаем объект MyNumber в качестве второго аргумента в оператор %.
# Когда мы запускаем программу, Python вызывает метод __rmod__ для объекта n и передает ему число 17 в качестве первого
# аргумента other. Метод __rmod__ возвращает остаток от деления числа 17 на 5, который равен 2. Затем оператор %
# заменяет подстроку %s в строке на этот остаток, и мы получаем строку "17 % n = 2".


# rmul(self, other): возвращает строку, повторенную определенное количество раз.
print(3 * "Hello")  # "HelloHelloHello"


# setattr(self, name, value): используется при установке значения атрибута объекта.
class MySetAttrClass:
    def __setattr__(self, name, value):
        print("Setting attribute")
        super().__setattr__(name, value)


obj = MySetAttrClass()
obj.x = 1  # Output: "Setting attribute"


# sizeof(self): возвращает размер объекта в байтах.
print("Hello".__sizeof__())  # 54


# str(self): возвращает строковое представление объекта.
print(str(1))  # "1"


# subclasshook(self, subclass): используется при определении, является ли класс подклассом данного класса.
class MyNextParentClass:
    pass


class MyNewChildClass(MyNextParentClass):
    pass


print(issubclass(MyNewChildClass, MyNextParentClass))  # True



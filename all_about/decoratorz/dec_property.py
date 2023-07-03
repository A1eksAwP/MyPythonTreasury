# @property - превращает метод класса в свойство, которое можно обращаться как атрибут, без вызова метода.

class MyClass:
    def __init__(self):
        self._my_attribute = 10

    @property
    def my_attribute(self):
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        self._my_attribute = value


# Использование свойства
obj = MyClass()
print(obj.my_attribute)  # Выводит значение атрибута
obj.my_attribute = 20     # Изменяет значение атрибута

# @abstractmethod - определяет абстрактный метод в абстрактном базовом классе.
# Класс, наследующийся от этого абстрактного класса, должен реализовать этот абстрактный метод.

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass


class MyClass(MyAbstractClass):
    def my_abstract_method(self):
        print("Implementing abstract method")


# Создание экземпляра класса
obj = MyClass()
obj.my_abstract_method()

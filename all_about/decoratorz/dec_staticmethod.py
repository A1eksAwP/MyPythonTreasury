# @staticmethod - превращает метод класса в статический метод,
# который может быть вызван независимо от экземпляра класса.

class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method")


# Вызов статического метода без создания экземпляра класса
MyClass.my_static_method()

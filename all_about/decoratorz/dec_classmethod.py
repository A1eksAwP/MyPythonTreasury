# @classmethod - превращает метод класса в метод, который принимает первым аргументом ссылку на класс (cls),
# а не на экземпляр класса. Этот декоратор позволяет работать с атрибутами класса, а не только с атрибутами экземпляра.

class MyClass:
    class_attribute = 10

    @classmethod
    def my_class_method(cls):
        print("This is a class method")
        print("Class attribute:", cls.class_attribute)


# Вызов классового метода
MyClass.my_class_method()

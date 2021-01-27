# Определить порядок исполнения print() и что будет выведено на экран.

# Согласно синтаксису python любой метод объявленый внутри класса должен иметь параметр SELF!!!

class my_metaclass(type):                                                              # Это класс
    def __new__(cls, class_name, parents, attributes):                                 # Это метод
        print('- my_metaclass. __new__ - Creating class instance of type', cls)
        return super().__new__(cls, class_name, parents, attributes)

    def __init__(self, class_name, parents, attributes):
        print('- my_metaclass. __init__ - Initializing the class instance', self)
        super().__init__(class_name, parents, attributes)

    def __call__(self, *args, **kwargs):
        print('- my_metaclass. __call__ - Creating object of type', self)
        return super().__call__(*args, **kwargs)

def my_class_decorator(cls):
    print('- my_class_decorator - Chance to modify the class', cls)
    return cls

@my_class_decorator
class C(metaclass=my_metaclass):

    def __new__(cls):
        print('- C.__new__ - Creating object')
        return super(C, cls).__new__(cls)

    def __init__(self):
        print('- C.__init__ - Initializing object')

c = C()
print('Object c =', c)
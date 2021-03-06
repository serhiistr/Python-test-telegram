# Class
# Название класса пишутся с большой буквы

class Dog():

# __init__ специальный метод, который автоматически выполняется при создании
# каждого нового экземпляра класса. Т.е. отвечает за базовый функционал,
# который будет отрабатываться каждый раз при создании нашего обьекта (собака :))

# self - указывает, что мы работаем конкретно с экземпляром класса Dog
# self нужен только внутри класса, а при создании обьекта мы его не указываем

    def __init__(self, name, age):
        #Инициализируем аттрибуты имя и возраст
        self.name = name
        self.age = age
        print("Собака",  name, "создана")

    def sit(self):
        print(self.name.title() + " села на место")

    def jump(self):
        print(self.name.title() + " подпрыгнула")

# Теперь создаем обьект по инструкции нашей (class Dog()). Этот обьект называется экземпляр класса

my_dog_1 = Dog('archi', 5)           # это создали экземпляр класса Dog
my_dog_2 = Dog('ben', 2)

my_dog_1.sit() # обращаемся напрямую к методу, через точку
my_dog_2.jump()

# print(my_dog.age)

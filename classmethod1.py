class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def description_name(self):
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        print('Пробег этого авто ' + str(self.odometer_reading) + ' км')

    def update_odometer(self, km):
        self.odometer_reading = km

my_car = Car('Audi', 'A4', 2017)
my_car.update_odometer(33)

my_car.read_odometer()
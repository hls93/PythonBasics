#Public => memberName
#Protected => _memberName
#Private => __memberName

class Car:
    numberOfWheels = 4
    _color ="Black"
    __yearOfManufacture = 2017 #_Car__yearOfManufacture

class BMW(Car):
    def __init__(self):
        print("protected attribute color: ", self._color)

car = Car()
print("Public attribute NumberOfWheels: ", car.numberOfWheels)
bmw = BMW()
print("private att year of manufacture ", car._Car.__yearOfManufacture)

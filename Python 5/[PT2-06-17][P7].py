class Car():
    ids = 0

    def __init__(self, color='Black', wheels=5):
        self.color = color
        self.wheels = wheels
        if color.lower() == 'red':
            self.wheels = 4
        Car.ids += 1

    def diag(self):
        print ("This car has {} wheels and has {} color".format(self.wheels, self.color))


if __name__ == '__main__':
    car1 = Car()
    car1.diag()
    car2 = Car('Red')
    car2.diag()
    car3 = Car('Yellow', 3)
    car3.diag()
    print "Quantity of created cars {}".format(Car.ids)

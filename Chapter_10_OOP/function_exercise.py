class Thing:
    pass
print(Thing)
example = Thing()
print(example)

class Thing2:
    letters = 'abc'

print(Thing2.letters)

class Thing3:
    letters = 'xyz'

print(Thing3.letters)

class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f' name: {self.__name}, symbol: {self.__symbol}, number {self.__number}'

hydrogen_1 = Element('Hydrogen', 'H', 1)

hydrogen_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen_2 = Element(**hydrogen_dict)
#hydrogen_2.dump()
print(hydrogen_2)
print(hydrogen_2.name)


class Bear:
    def eats(self):
        return 'beries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octot = Octothorpe()
print(bear.eats())
print(rabbit.eats())
print(octot.eats())

class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self, laser, claw, smart):
        self.laser = laser
        self.claw = claw
        self.smart = smart

    def does(self):
        return self.laser.does(), self.claw.does(), self.smart.does()


laser = Laser()
claw = Claw()
smart = SmartPhone()
robot = Robot(laser, claw, smart)
print(robot.does())

print('==' * 20)
print('Простые объекты')


class Cat:
    pass


a_cat = Cat()
neibhour_cat = Cat()

print(a_cat, neibhour_cat)

print('-' * 10)
print('Атрибуты')
a_cat.name = 'Kefir'
a_cat.color = 'orange'
a_cat.friend = neibhour_cat
a_cat.friend.name = 'Bochok'
print(a_cat.name, a_cat.color, a_cat.friend.name)

print('-' * 10)
print('Инициализация')


class Cat:
    def __init__(self, name):
        self.name = name


sisters_cat = Cat('Givi')

print('Our latet addition: ', sisters_cat.name)

print('==' * 20)
print('Наследование')


class Car:
    pass


class Toyota(Car):
    pass


print(issubclass(Toyota, Car))

give_me_a_car = Car()
give_me_a_toyota = Toyota()


class Car:
    def say_my_name(self):
        print("I`m a Car!")


class Toyota(Car):
    pass


give_me_a_car = Car()
give_me_a_toyota = Toyota()
give_me_a_car.say_my_name()
give_me_a_toyota.say_my_name()

"""У такого приема, как наследование, есть определенные преимущества,
но иногда им пользуются слишком часто. Многолетний опыт работы в объектно-ориентированном
программировании показал, что чрезмерное увлечение наследованием может затруднить управление
программами. Вместо этого рекомендуется сделать акцент на использовании других приемов,
таких как агрегирование и композиция."""

print('==' * 20)
print('Переопределение методов')


class Car:
    def say_my_name(self):
        print("I`m a Car!")


class Toyota(Car):
    def say_my_name(self):
        print("I`m Toyota. Rule your dreams")


give_me_a_car = Car()
give_me_a_toyota = Toyota()
give_me_a_car.say_my_name()
give_me_a_toyota.say_my_name()


class Person:
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Важный тип"


person_0 = Person('Fred')
person_1 = JDPerson('Givi')
person_2 = MDPerson('House')
print(person_0.name)
print(person_1.name)
print(person_2.name)

print('==' * 20)
print('Добавление метода')


class Car:
    def say_my_name(self):
        print('I`m a car')


class Toyota(Car):
    def say_my_name(self):
        print('I`m Toyota rule your dreams')

    def need_help(self):
        print('Bite me!! (*3*)')


give_me_a_car = Car()
give_me_a_toyota = Toyota()
give_me_a_toyota.need_help()

print('==' * 20)
print('Поулчаем помощь от super()')


class Person:
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


"""Когда вы определяете метод __init__() для своего класса,
вы заменяете метод __init__() родительского класса, который больше
не вызывается автоматически. В результате вам нужно вызывать его явно."""

givy = EmailPerson('Givy', 'giv4ik@gmail.com')
print(givy.name)
print(givy.email)

print('==' * 20)
print('Множественное наследование')


class Animal:
    def says(self):
        print("I`m an animal")


class Horse(Animal):
    def says(self):
        print("I`m a horse")


class Donkey(Animal):
    def says(self):
        print('DOOOONkeeeeey')


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()
mule.says()
hinny.says()

print('==' * 20)
print('Примеси')
"""Вы можете включить дополнительный родительский класс в определение вашего класса,
но только в качестве вспомогательного. Таким образом, он не будет иметь общих методов
с другими родительскими классами, что позволит избежать неоднозначности при разрешении методов
Такой родительский класс называют классом-примесью или миксином. Примеси можно использовать для
выполнения «сторонних» задач, таких, например, как ведение журнала."""


class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.name = 'Gibson'
t.age = 18
t.race = 'Asian'
t.dump()

print('==' * 20)
print('В защиту self')
a_car = Car()
a_car.say_my_name()
"""Вот что происходит за кулисами Python.
1. Выполняется поиск класса (Car) объекта a_car.
2. Объект a_car передается методу exclaim() класса Car как параметр self."""
Car.say_my_name(a_car)  # оба метода работают нормально, но смысла так делать нет


def header_1(name):
    print('==' * 20)
    print(name)


def header_2(name):
    print('--' * 10)
    print(name)


header_1('Доступ к атрибутам')
header_2('Прямой доступ')


class Duck:
    def __init__(self, input_name):
        self.name = input_name


daffy = Duck('Daffy')
print(daffy.name)
print('Кто то решил поменять этот атрибут')
daffy.name = 'Abvralg'
print(daffy.name)

header_2('Геттеры и сеттеры')


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name  # Чтобы не было доступа используют обфускацию

    def get_name(self):
        print('Inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


don = Duck('Donald')
print(don.get_name())
don.set_name('Daffy')
print(don.get_name())

header_2('Свойства для доступа к атрибутам')


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name  # Чтобы не было доступа используют обфускацию

    def get_name(self):
        print('Inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


don = Duck('Donald')
print(don.get_name())
don.set_name('Scruj')
print(don.get_name())
"""Но благодаря propert теперь можно использовать name
для доступа к атрибутам"""
print('Новый подход')
don = Duck('Donald')
print(don.name)
don.name = 'Scruj'
print(don.name)
header_2('Подход через декораторы')
"""@property размещается перед геттером
name.setter размещается перед сеттером
имена методов get_name и set_name заменяются на name"""


class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name  # Чтобы не было доступа используют обфускацию

    @property
    def name(self):
        print('Inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


don = Duck('Baggy')  # доступ к name осуществляется как к атрибуту
print(don.name)
don.name = 'Donald'
print(don.name)
"""Если кто-то и догадается, что мы назвали наш атрибут hidden_name,
считать и записать его он все равно может непосредственно как fowl.hidden_name.
В подразделе «Искажение имен для безопасности» далее в этой главе вы увидите
особый способ Python, позволяющий скрыть имена атрибутов."""

header_2('Свойства вычисляемых значений')

class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.diameter)
"""Если вы не укажете сеттер для атрибута, 
то не сможете устанавливать его значение извне. 
Это удобно для атрибутов, которые должны быть 
доступны только для чтения:"""
#c.diameter = 20

header_2('Искажение имен для безопасности')
"""В рассмотренном ранее примере с классом Duck 
мы назвали наш (не полностью) скрытый атрибут hidden_name. 
Python предлагает соглашения по именованию для атрибутов, 
которые не должны быть видимы за пределами определения их классов: 
имена начинаются с двух нижних подчеркиваний (__)."""
class Duck:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside setter')
        self.__name = input_name

big_duck = Duck('Bobby')
print(big_duck.name)
big_duck.name = 'Daffy'
print(big_duck.name)
#big_duck.name не доступно для изменения атрибута
"""Однако эта защита не идеальна и доступ выглядит так"""
print(big_duck._Duck__name)

header_2('Атрибуты классов и объектов')
class Fruit:
    color = 'red'

blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)
blueberry.color = 'blue'
print(blueberry.color)
print(Fruit.color)
"""Если позже измените атрибут класса, 
на существующих объектах-потомках это не отразится:"""
Fruit.color = 'orange'
print(blueberry.color)
print(Fruit.color)
"""Но это отразится на новых экземплярах классов"""
new_fruit = Fruit()
print(new_fruit.color)

header_2('Типы методов')
"""Методы объектов стандартные и при их вызове Python
передает объект методу, когда мы его вызываем(через self)"""
header_2('Методы классов')
"""В противоположность ему метод класса влияет на весь класс целиком. 
Любое изменение, которое происходит с классом, влияет на все его объекты. 
Внутри определения класса декоратор @classmethod показывает, что следующая 
функция является методом класса. Первым параметром метода также является сам класс. 
По традиции этот параметр называется cls, поскольку слово class зарезервировано 
и не может быть использовано в данной ситуации. Определим метод класса для А, который 
будет подсчитывать количество созданных объектов:"""

class A:
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print('I`m an A!')

    @classmethod
    def kids(cls):
        print('A has', cls.count, "little objects")  # можно использовать и A.count

easy_a = A()
brezy_a = A()
weezy_a = A()
A.kids()

header_2('Статические методы')
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print("This CoyoteWeapon has been brought to you by Any")

CoyoteWeapon.commercial()

"""Третий тип методов не влияет ни на классы, ни на объекты: он находится 
внутри класса только для удобства, чтобы не располагаться где-то отдельно. 
Это статический метод, которому предшествует декоратор @staticmethod, 
не имеющий в качестве начального параметра ни self, ни класс class.
Обратите внимание на то, что нам не нужно создавать объект класса CoyoteWeapon, 
чтобы получить доступ к этому методу. И это замечательно."""

header_1("Утиная типизация")
#213

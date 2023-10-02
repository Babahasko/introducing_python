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
"""В Python имеется также реализация полиморфизма — это значит, 
что одна операция может быть произведена над разными объектами, 
основываясь на имени метода и его аргументах, независимо от их класса."""


class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('ElemFudd', 'I`m hunting rabbits')
print(hunter.who(), 'says: ', hunter.says())

hunter_1 = QuestionQuote('Bug Bunny', 'Hey, wasssap')
print(hunter_1.who(), 'says: ', hunter_1.says())

hunter_2 = Quote('Alen Ford', 'I like cars')
print(hunter_2.who(), 'says: ', hunter_2.says())

"""Это был типичный пример полиморфизма - один
и тот же метод в разных классах. Но Python пошел дальше и позволяет
вызывать методы who() и says() для любых объектов, в том числе
и для этих методов."""

print('--'*10)
print('Зайдем немного глубже')
class BagglinBrook:
    def who(self):
        return 'Gruut'
    def says(self):
        return 'I`m GRUUUT'


brook = BagglinBrook()


def who_says(obj):
    print(obj.who(), 'says:', obj.says())


who_says(hunter)
who_says(hunter_1)
who_says(hunter_2)
who_says(brook)

header_2('Магические методы')


class Word:
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('HA')
second = Word('ha')
third = Word('eh')
print(first.equals(second))
print(first.equals(third))


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return f'Word {self.text}'

    def __repr__(self):
        return self.text


first = Word('HA')
second = Word('ha')
third = Word('eh')
print(first == second)
print(first == third)
print(first)


header_2('Агрегирование и композиция')

"""Наследование может сослужить хорошую службу, 
когда вы хотите, чтобы класс-потомок бо'льшую часть 
времени вел себя как родительский класс (потомок является родителем). 
Возможность создавать иерархии наследования довольно заманчива, но 
иногда композиция или агрегирование имеет больше смысла. В чем разница? 
При композиции один объект является частью другого. Утка является птицей (наследование), 
но имеет хвост (композиция)."""


class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')


a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()

"""Агрегирование выражает более свободные отношения между объектами: 
один из них использует другой, но оба они существуют независимо друг 
от друга. Утка использует озеро, но не является его частью."""

header_2("Когда использовать объекты,а когда — что-то другое")
"""Рассмотрим несколько рекомендаций, которые помогут вам понять, 
где лучше разместить свой код и данные — в классе, в модуле или в
чем-то совершенно ином."""
print("Объекты наиболее полезны, когда вам нужно иметь несколько "
      "отдельных экземпляров с одинаковым поведением (методы), но"
      "разным внутренним состоянием (атрибуты).")
print('Классы, в отличие от модулей, поддерживают наследование')
print('Если вам нужен только один объект, модуль может быть лучшим'
      'выбором. Независимо от того, сколько обращений к модулю имеется в'
      'программе, загрузится только одна копия.')
print("""Если у вас есть несколько переменных, которые содержат разные 
      значения и могут быть переданы в качестве аргументов в несколько 
      функций, лучше всего определить их как классы. Например, вы можете 
      использовать словарь с ключами size и color, чтобы представить цветное 
      изображение. Вы можете создать разные словари для каждого изображения 
      в программе и передавать их в качестве аргументов в функции scale() и 
      transform(). Правда, по мере добавления новых ключей и функций разбираться 
      со всем этим станет трудно. Поэтому более предпочтительно определить класс 
      Image с атрибутами size или color и методами scale() и transform(). Тогда 
      все данные и методы для работы с цветными изображениями будут определены в одном месте.""")
print("""Используйте самые простые решения. Словарь, список или кортеж проще, компактнее и быстрее, 
чем модуль, который, в свою очередь, проще, чем класс. Совет от Гвидо ван Россума: «Избегайте усложнения 
структур данных. Кортежи лучше объектов (можно воспользоваться именованными кортежами). 
Предпочитайте простые поля функциям, геттерам и сеттерам. (Встроенные типы данных — ваши друзья.) 
Используйте больше чисел, строк, кортежей, списков, множеств, словарей. Взгляните также на библиотеку 
collections, особенно на класс deque».""")
print("""Более новой альтернативой является класс данных""")

header_2("Именованные кортежи")

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {'bill' : 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

duck_dict = {'bill':'wide orange', 'tail': 'long'}
print(duck_dict)
duck_dict['color'] = 'green'  #  Можно добавить поле в словарь
print(duck_dict)
#duck.color = 'green' # Но нельзя добавить в именованный кортеж
print('Плюсы именованных кортежей:')
print("""1.Они выглядят и действуют как неизменяемый объект.
2.Они более эффективны, чем объекты, с точки зрения времени и занимаемого места.
3.Вы можете получить доступ к атрибутам, используя точки, а не квадратные скобки, характерные для словарей.
4.Вы можете использовать их как ключ словаря.""")

header_2('Классы данных')
print("""Многие люди создают объекты для хранения данных (с помощью атрибутов объектов), а 
не для задания определенного поведения (с помощью методов). Вы уже видели, как именованные 
кортежи могут стать альтернативным хранилищем данных.""")
class TeenyClass:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name

teeny = TeenyClass('itsy')
print(teeny.name)
print('Реализация с помощью классов данных')
from dataclasses import dataclass
@dataclass
class TeenyClass:
    name: str


teeny = TeenyClass('bitsy')
print(teeny.name)
print("""Помимо декоратора @dataclass, вам нужно определить атрибуты 
класса с помощью аннотаций переменных (https://www.python.org/dev/peps/pep-0526/). 
Это выглядит как имя: тип или имя: тип = значение, например color: str или color: str = "red". 
Типом может быть любой тип объектов в Python, включая созданные вами классы, а не только 
встроенные, такие как str или int.""")
print("""Когда вы создаете объект класса данных, вы предоставляете аргументы в том порядке, 
в котором они указаны в классе, или используете именованные аргументы, передавая их в любом порядке:""")
@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
print(snowman)
print(duck)
print('Вы можете обращаться к атрибутам этого объекта точно так же, как и к атрибутам других объектов:')
print(duck.habitat)
print(snowman.teeth)
print("""О классах данных можно говорить еще долго. Обратитесь к этому руководству 
(https://realpython.com/python-data-classes/) или прочтите официальную (довольно объемную) 
документацию (https://www.python.org/dev/peps/pep-0557/).""")

header_2('attrs')
print("""Именованные кортежи и классы данных предлагают альтернативное решение, которое можно встретить в стандартной библиотеке, — если вам нужно создать простую коллекцию данных, проще всего воспользоваться этими вариантами.
В статье The One Python Library Everyone Needs (https://glyph.twistedmatrix.com/
2016/08/attrs.html) сравниваются простые классы, именованные кортежи и классы данных. 
В ней по множеству причин рекомендуется использовать сторонний пакет attrs (https://oreil.ly/Rdwlx), 
который позволяет меньше набирать, меньше проверять данные и т. д. Взгляните сами и решите для себя, 
что вам больше нравится — эта библиотека или встроенные решения.""")


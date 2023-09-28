print('None is usefully')
def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


whatis(None)
whatis(True)
whatis(False)
print('='*10)
whatis(0)
whatis(0.0)
whatis('')
whatis('''''')
whatis(())
whatis([])
whatis({})
whatis(set())
print('='*10)
whatis(0.00001)
whatis([0])
whatis([''])
whatis(' ')

print('==' * 20)
print('Строки документации')


def echo(anything):
    """ Returns its input argument """
    return anything


def print_if_true(thing, check):
    """
    Prints th first argument if a second argument is true.
    The operation is:
        1. Check whether the second is true.
        2. If it is, print the *first argument.
    :param thing:
    :param check:
    :return:
    """
    if check:
        print(thing)


help(print_if_true)
print(echo.__doc__)
abc = echo  # присвоил функцию переменной
print(abc('что-то'))  # вызвал эту функцию


def func_return(function):
    return function


abcd = func_return(print_if_true)
abcd('c чем-то', 'что-то')


def answer():
    print(43)


answer()


def run_something(func):
    func()


run_something(answer)
print(type(run_something))


def add_args(arg1, arg2):
    print(arg1 + arg2)


print(type(add_args))


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_something_with_args(add_args, 1, 10)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1, 2, 3, 4))


def knights(saying):
    def inner(quote):
        return "We are the knight who say: '%s' " % quote

    return inner(saying)


print(knights('Ni'))


def knights2(saying):
    def inner2():
        return "We are the knight`s who saying '%s' " % saying

    return inner2


a = knights2('Duck')
b = knights2('Mommy')

res_1 = a()
res_2 = b()
print(res_1)
print(res_2)

print('==' * 20)
print('Анонимные лямбда выражения')


def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['meow', 'tuhd', 'hiss', 'tuhd']


def enliven(word):
    return word.capitalize() + '!'


edit_story(stairs, enliven)
print('--' * 10)
edit_story(stairs, lambda slovo: slovo.capitalize() + '!')

print('==' * 20)
print('Generation Functions')
print(sum(range(1, 101)))


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number  # Возвращает значение с помощью yield а не return
        number += step

print(type(my_range))
ranger = my_range(1, 5)  #  Эта обычная функция возвращает объект генератора
print(ranger)

for x in ranger:
    print(x)

"""Генератор можно запустить лишь однажды. Списки, множества,
строки и словари существуют в памяти, а генераторы создают свои
значения на лету и выдают их по одному с помощью итератора.
Генератор не запоминает значения, поэтому вы не можете перезапустить
его или создать резервную копию."""

for try_again in ranger:
    print(try_again)

print('==' * 20)
print('Включение генераторов')

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(type(genobj))
for thing in genobj:
    print(thing)

print('=='*20)  #  это функция, которая принимает одну функцию
print('Декораторы')  # в качестве аргумента и возвращает другую функцию.

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Postional arguments:', args)
        print('Keword arguments', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_function


def add_ints(a, b, **kwargs):
    for key, val in kwargs.items():
        print(key, val)
    return a + b


print(add_ints(3, 4, **{'melik' : 'huge'}, **{'gender' : 'female'}, **{'hair' : 'brown'}))
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5, **{'melik' : 'huge'}, **{'gender' : 'female'}, **{'hair' : 'brown'})

print('=='*20)
print('Используем декоратор')

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@square_it
@document_it
def add_ints(a, b, **kwargs):
    for k, v in kwargs.items():
        print(k, v)
    return a + b
ma_dict = {'melik' : 'huge','gender' : 'female','hair' : 'brown'}
print(add_ints(2, 11, **ma_dict))

print('--'*10)
print('Изменим порядок декораторов')

@document_it  #  Выполняется первым декоратор, который ближе всего к функции
@square_it
def add_ints(a, b, **kwargs):
    for k, v in kwargs.items():
        print(k, v)
    return a + b
ma_dict = {'melik' : 'huge','gender' : 'female','hair' : 'brown'}
print(add_ints(2, 11, **ma_dict))

animal = 'fruitbat'


def print_global():
    print('inside print global: ', animal)

print('At the top level: ', animal)
print_global()

""" Заведомо ошибочный пример 
пытаемся изменить глобальную переменную внутри функции"""

# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print('after the change: ', animal)
#  change_and_print_global()

def change_local():
    animal = 'wombat'
    print('Inside change local: ', animal, id(animal))


change_local()
print('Outside change local: ', animal, id(animal))

"""Глобальная пременная не поменялась, т.к. мы создали
и имзенили локальную перменную внутри функции change_local()"""

def change_and_print_global():
    global animal
    animal = 'wombat'
    print('Inside change_and_print_global: ', animal, id(animal))

change_and_print_global()
print("Outside change_and_print_global: ", animal, id(animal))

"""Насколько помню использования глобальных перменных следует избегать, а то это
не 'Pythonic way'. лучше, чтобы функции возвращали значения и затем их уже использовать
в других функциях"""

print('=='*20)
print('Использование словрая локального и глобального пространства имён')
animal = 'fruitbat'
def show_locals():
    animal = 'wombat'
    print('locals: ', locals())

print(animal)
show_locals()
print('globals: ', globals())
print(animal)
"""Локальное пространство имен внутри функции change_local()
содержало только локальную переменную animal.
Глобальное пространство имен содержало отдельную глобальную
переменную animal и многое другое."""

print('=='*20)
print('Использование символов _ и __ в именах')
"""Имена __xxxx___ зарезервированы для использования внутри Python.
Их не применяем. Например, имя функции находится в системной переменной
function.__name__, а имя ее строки документации — в function.__doc__:"""

def amazing():
    """ This is the amazing function.
     Want to see it again? """
    print('This function is named: ', amazing.__name__)
    print('And its docstring is: ', amazing.__doc__)

amazing()


print('=='*20)
print('Рекурсия')

"""Заведомо ошибочный пример, функция вызывает сама себя бесконечно и генерирует ошибку"""

# def dive():
#     return dive()
# dive()

"""щих списки, которые содержат списки.
Предположим, вы хотите «уплотнить» все подсписки
независимо от того, насколько глубоко они вложены.
Для этого отлично подойдет функция-генератор:"""

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item

lol = [2, 4, 6,[ 'lol', 'hi', 'everyone',[2,3,4,[1,2,3,[11,12]]]]]
print(flatten(lol))
print(list(flatten(lol)))

"""выражение yield from позволяет генератору передавать часть работы
другому генератору. Мы можем использовать его для того, чтобы упростить 
функцию flatten():"""

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

lol = [1, 1, 3,[ 'lol', 'kek'], 'cheburek',[2,3,4,[1,2,3,[11,12]]]]
print(list(flatten(lol)))

"""Это еще один популярный вопрос на собеседованиях. Давайте соберем всю коллекцию!"""

print('==' * 20)
print('Исключения')

short_list = [2, 4, 7]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and ', len(short_list) - 1, 'but got ', position)

print('--'*10)
print('Получаем больше информации об исключениях')

short_list = [2, 5, 9]
#Закоментил, чтобы вечно 'q' не вводить

# while True:
#     value = input('Position [q to quiet]?')
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad index', position)
#     except Exception as other:
#         print('Smothing else broken: ', other)  #  Выводится только последняя ошибка, без Traceback

print('==' * 20)
print('Создаём собственные типы исключений')

class UpperCaseException(Exception):
    pass

"""Очередной код с задуманной ошибкой"""

# words = ['enieee', 'menie', 'mini', 'AVADACEDAVRA']
# for word in words:
#     if word.isupper():
#         raise UpperCaseException(word)
#
"""Мы даже не определяли какое-то поведение для UppercaseException
(обратите внимание — мы просто использовали pass),
позволив его родительскому классу Exception самостоятельно разобраться,
что именно выводить на экран при генерации исключения."""

class OopsException(Exception):
    pass
try:
    raise OopsException('Generating of exception: oops')
except OopsException as exc:
    print(exc)

# raise OopsException() # Вывело просто название исключения

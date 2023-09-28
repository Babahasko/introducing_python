print("--"*10)
print('Exercise 1')


def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

print("--"*10)
print('Exercise 2')


def get_ods():
    for i in range(10):
        if i % 2 != 0:
            yield i

print(list(get_ods())[2])
#тоже самое черех цикл for
k=0
for i in get_ods():
    if k == 2:
        print(i)
    k += 1

print("--"*10)
print('Exercise 3')


def test_decor(func):
    def new_func():
        print('start')
        func()
        print('end')
    return new_func

@test_decor
def some_func():
    for i in range(1, 3):
        print(i)

some_func()

print("--"*10)
print('Exercise 4')


class OopsException(Exception):
    pass


#raise OopsException()

try:
    raise OopsException()
except OopsException:
    print('Cought an Oops')
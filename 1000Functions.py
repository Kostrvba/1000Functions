
import random
from math import sqrt



def printer():
    print("1000 functions!")


printer()


def adder(x, y):
    return x + y


print(adder(1, 5))


def remover(x):
    return 5 - x


print(remover(5))


def multiper(y):
    return y * 2


print(multiper(5))


def division(x, y):
    return x / y


print(division(6, 2))


def exponentiation(x):
    return x ** 2


print(exponentiation(5))


def rest(x, y):
    return x % y


print(rest(10, 3))


def sqrter(x):
    return sqrt(x)


print(sqrter(4))


def multistring(x):
    return x * 3


print(multistring("Hello"))


def table():
    x = [1, 2, 3]
    return x


print(table())


# 10!

def sum_table():
    x = [1, 2]
    y = [3, 4]
    return x + y


print(sum_table())


def is_true(x):
    if x == True:
        return "true"
    else:
        return "false"


print(is_true(True))


def list_arguments_printer():
    x = [1, 2, 3]
    return x[1], x[2]


print(list_arguments_printer())


def list_length():
    x = [5, 7]
    return len(x)


print(list_length())


def list_appender():
    x = [5, 7]
    x.append(6)
    return x


print(list_appender())


def list_inserter():
    x = [5, 6, 8]
    x.insert(2, 7)
    return x


print(list_inserter())


def is_same(x, y):
    if x == y:
        return "is same"
    else:
        return "Nope"


print(is_same(5, 5))


def bigger(x, y):
    if x > y:
        return "bigger"


print(bigger(5, 3))


def lower(x, y):
    if x < y:
        return "lower"


print(lower(3, 5))


def rounder(x):
    return round(x, 2)


print(rounder(3.4546765))


# 20!!

def is_same_name(x, y):
    if x > y:
        return "same"
    else:
        return "not same"


print(is_same_name("Alicja", "alicja"))


def incramentation(i):
    i += 1
    return i


print(incramentation(1))


def decramentacion(i):
    i -= 1
    return i


print(decramentacion(3))


def if_two_true(x, y):
    if x and y == True:
        return "TwoTrue"


print(if_two_true(True, True))


def if_one_true(x, y):
    if x or y == True:
        return "OneTrue"


print(if_one_true(True, False))


def not_true(x):
    if not x == False:
        return "False"


print(not_true(True))


def converter(x):
    return int(x)


print(converter("5"))


def string_converter(x):
    return str(x)


print(string_converter(234))


def string_to_list(x):
    return list(x)


print(string_to_list("Letters"))


def list_to_letters(x):
    return ' '.join(x)


print(list_to_letters(['L', 'E', 't', 'T', 'E', 'r', 'S']))


# 30!!!

def list_to_one_word(x):
    return ''.join(x)


print(list_to_one_word(['H', 'I']))


def is_0_True():
    x = 0
    y = (x == True)
    return y


print(is_0_True())


def inputer():
    x = input("give me x")
    return x


# print(inputer())

def absolute(x):
    return abs(x)


print(absolute(-50))


def biggest_from_list(x):
    return max(x)


print(biggest_from_list([1, 2, 3]))


def smallest_from_list(x):
    return min(x)


print(smallest_from_list([1, 2, 3]))


def sum_list(x):
    return sum(x)


print(sum_list([1, 2, 3]))


def sort_list(x):
    return sorted(x)


print(sort_list([5, 1, 9, 3]))


def what_type(x):
    return type(x)


print(what_type("a"))


def f_string(x):
    return f"your x is {x}"


print(f_string(5))


# 40!!!!


def for_how_many_elem(x):
    y = 0
    for elements in x:
        y += 1
    return f"{y} elements"


print(for_how_many_elem([1, 2, 3]))


def in_ranger(x):
    y = 0
    for elems in range(x):
        y += 1
    return f"{y} in range!"


print(in_ranger(5))


def in_range_list_adder(x):
    my_list = []
    for x in range(4):
        my_list.append(x)
    return my_list


print(in_range_list_adder(3))


def in_range_list_same_numb_adder(x):
    my_list = []
    for i in range(4):
        my_list.append(x)
    return my_list


print(in_range_list_same_numb_adder(3))


def easy_list():
    return list(range(5))


print(easy_list())


def while_incramentation(x):
    while x < 6:
        x += 1
    return x


print(while_incramentation(3))


def random_numb():
    return random.randint(1, 10)


print(random_numb())


def while_random_my_numb(x):
    y = 0
    while y != x:
        y = random.randint(1, 10)
    return "random number is my number"


print(while_random_my_numb(5))


def how_many_guess(x):
    y = 0
    z = 0
    while y != x:
        y = random.randint(1, 10)
        z += 1
    return f"{z} try"


print(how_many_guess(5))


def breaker():
    x = 0
    while x < 10:
        x += 1
        if x == 5:
            break
            return x
    return x


print(breaker())

#50!!!!!
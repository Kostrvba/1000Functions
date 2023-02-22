import random
import string
from math import sqrt
from datetime import datetime


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


# 50!!!!!

def if_elif_else(x):
    if x > 1:
        return "lower"
    elif x == 1:
        return "1!"
    else:
        return "bigger"


print(if_elif_else(0))


def for_else(table):
    for i in table:
        if i == 3:
            return "there is 3"
            break
        else:
            return "no 3"


print(for_else([1, 2, 4, 5]))


def even_or_odd(number):
    if (number % 2) == 0:
        return "Even"
    elif (number % 2) == 1:
        return "Odd"


print(even_or_odd(3))


def str_count(strng, letter):
    i = 0
    z = 0
    for letters in strng:
        if letter == strng[z]:
            i += 1
        z += 1
    return i


print(str_count("Tato", "a"))


def mean(x, y):
    return (x + y) / 2


print(mean(2, 4))


def mean_from_list(my_list):
    numbers = len(my_list)
    z = 0
    for i in range(numbers):
        z = z + my_list[i]
    return z / numbers


print(mean_from_list([4, 6, 8]))


def volume(x, y, z):
    vol = x * y * z
    return vol


print(volume(5, 8, 10))


def five_random_letters():
    letters_list = []
    for i in range(5):
        x = random.choice(string.ascii_letters)
        letters_list.append(x)
    return letters_list


print(five_random_letters())


def small_letters(x):
    return x.lower()


print(small_letters('YrUT'))


def big_letters(x):
    return x.upper()


print(big_letters('yRut'))


# 60!!!!!!

def change_letters(x):
    x_list = list(x)
    length = len(x_list)
    for i in range(length):
        if x_list[i].isupper():
            x_list[i] = x_list[i].lower()
        elif x_list[i].islower():
            x_list[i] = x_list[i].upper()
    return ''.join(x_list)


print(change_letters("rTrY"))


def describe_age(age):
    x = "kid" if age <= 12 else "teen" if age <= 17 else "adult" if age <= 64 else "elder"
    return f"You're {x}"


print(describe_age(18))


def sort_by_last_letter(s):
    def last_letter(word):
        return word[-1]

    return sorted(s.split(), key=last_letter)


print(sort_by_last_letter("Hello men i need a taxi"))


def format_duration(seconds):
    result_message = []
    year_result = seconds // 31536000
    day_result = (seconds % 31536000) // 86400
    hour_result = (seconds % 86400) // 3600
    rest = seconds % 3600
    minutes_result = rest // 60
    end_seconds = rest % 60

    if year_result > 0:
        result_message.append(f"{year_result} year" + ("s" if year_result > 1 else ""))

    if day_result > 0:
        result_message.append(f"{day_result} day" + ("s" if day_result > 1 else ""))

    if hour_result > 0:
        result_message.append(f"{hour_result} hour" + ("s" if hour_result > 1 else ""))

    if minutes_result > 0:
        result_message.append(f"{minutes_result} minute" + ("s" if minutes_result > 1 else ""))

    if end_seconds > 0:
        result_message.append(f"{end_seconds} second" + ("s" if end_seconds > 1 else ""))

    if len(result_message) == 0:
        return "now"
    elif len(result_message) == 1:
        return result_message[0]
    else:
        return ", ".join(result_message[:-1]) + " and " + result_message[-1]


print(format_duration(73826478))


def what_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


print(what_time())


def dice(many_numbers, throws):
    result = 0
    for throw in range(throws):
        numb = random.randint(1, many_numbers)
        result = result + numb
    return result


print(dice(6, 2))


def binary(x):
    binar = bin(x)
    return binar


print(binary(34))


def count_bits(n):
    binary = bin(n)
    length = len(binary)
    count = 0
    for i in range(length):
        if binary[i] == '1':
            count += 1
    return count


print(count_bits(34))


def is_isogram(word):
    return len(word) == len(set(word.lower()))


print(is_isogram("Kapelusz"))

#70!!!!!!!



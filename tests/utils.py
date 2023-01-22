import math


def is_prime(n):
    '''
    n: a non-negativ number
    return: True if the input number is prime else False
    '''
    if n < 0:
        return 'Negative numbers are not allowed'

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def cubic(a):
    '''
    a: a number
    return: return the cubic number
    '''
    return a * a * a


def say_hello(name):
    '''
    name: the name of a person or a thing
    return: Say Hello to a person or a thing
    '''
    return "Hello " + name
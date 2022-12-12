# def div(a, b):
#     return a / b

from exceptions import MyZeroDivisionError

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise MyZeroDivisionError(a)   #raise - это выброс exceptions (исключения), это return для except

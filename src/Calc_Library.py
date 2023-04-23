import decimal
from decimal import Decimal
import sys
sys.setrecursionlimit(3207)  # Increase recursion depth limit to 10000

def Factorial(n):
    if Decimal(n) > 3200:
        return "Overflow!"
    if not isinstance(n, int):
        return "Undefined!"
    if n == 0:
        return 1
    if n < 0:
        return "Undefined!"

    try:
        result = Decimal(n) * Factorial(n - 1)
        return result
    except RecursionError:
        return "Overflow!"

def SquareRoot(n):
    if n < 0:
        return "Undefined!"
    x = Decimal(str(n)) ** Decimal('0.5')
    return x

def Power(n, p):
    # number = decimal.Decimal(n) ** p
    # number_str = format(number, '0.10E').replace('E', 'e')
    #
    n = Decimal(str(n))
    p = Decimal(str(p))
    if n == decimal.Decimal('0') and decimal.Decimal('0') == p:
        return decimal.Decimal('1')
    number = n ** p
    # number_str = str(number)
    # number_digits = len(number_str)
    # if number_digits > 8 and '+' not in number_str:
    #     number = round(number, 8)
    return number

def Plus(n, p):

    n = Decimal(str(n))
    p = Decimal(str(p))
    x = n + p
    # x = float(n) + float(p)
    # x = "{:.7e}".format(x)
    # num_str = str(x)
    # num_str = str(x)
    # num_digits = len(num_str)
    # if num_digits > 8 and '+' not in num_str and ('-' not in num_str or num_str[0] == '-'):
    #     x = round(x, 3)
    return x

def Minus(n, p):
    n = Decimal(str(n))
    p = Decimal(str(p))
    x = n - p
    # num_str = str(x)
    # num_digits = len(num_str)
    # if num_digits > 8 and '+' not in num_str:
    #     x = round(x, 3)
    return x

def Multiply(n, p):
    n = Decimal(str(n))
    p = Decimal(str(p))
    # x = float(n) * float(p)
    # num_str = str(x)
    # num_digits = len(num_str)
    # if num_digits > 16 and '+' not in num_str:
    #     x = round(x, 30)
    x = n * p
    return x

def Divide(n, p):
    # x = decimal.Decimal(n) / decimal.Decimal(p)
    x = float(n) / float(p)
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8 and '+' not in num_str:
        x = round(x, 8)
    return x

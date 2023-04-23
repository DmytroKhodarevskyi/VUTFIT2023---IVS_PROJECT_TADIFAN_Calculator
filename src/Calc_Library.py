import decimal
import sys
sys.setrecursionlimit(3207)  # Increase recursion depth limit to 10000

def Factorial(n):
    if decimal.Decimal(n) > 3200:
        return "Overflow!"
    if not isinstance(n, int):
        return "Undefined!"
    if n == 0:
        return 1
    if n < 0:
        return "Undefined!"

    try:
        result = decimal.Decimal(n) * Factorial(n - 1)
        return result
    except RecursionError:
        return "Overflow!"

def SquareRoot(n):
    if n < 0:
        return "Undefined!"
    result = float(n) ** 0.5
    # change . to , for decimal
    if result.is_integer():
        result = int(result)
        return result
    result = str(result).replace('.', ',')
    return result
    # return float(n) ** 0.5

def Power(n, p):
    # number = decimal.Decimal(n) ** p
    # number_str = format(number, '0.10E').replace('E', 'e')
    number = float(n) ** float(p)
    number_str = str(number)
    number_digits = len(number_str)
    # if number_digits > 8 and '+' not in number_str:
    #     number = round(number, 8)
    return number

def Plus(n, p):
    x = decimal.Decimal(n) + decimal.Decimal(p)
    # x = float(n) + float(p)
    # x = "{:.7e}".format(x)
    num_str = str(x)
    # num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8 and '+' not in num_str:
        x = round(x, 5)
    return x

def Minus(n, p):
    x = decimal.Decimal(n) - decimal.Decimal(p)
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8 and '+' not in num_str:
        x = round(x, 5)
    return x

def Multiply(n, p):
    x = decimal.Decimal(n) * decimal.Decimal(p)
    # x = float(n) * float(p)
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8 and '+' not in num_str:
        x = round(x, 3)
    return x

def Divide(n, p):
    # x = decimal.Decimal(n) / decimal.Decimal(p)
    x = float(n) / float(p)
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8 and '+' not in num_str:
        x = round(x, 8)
    return x

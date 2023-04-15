
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)

def SquareRoot(n):
    return n ** 0.5

def Power(n, p):
    return n ** p

def Plus(n, p):
    x = n + p
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8:
        x = round(x, 3)
    return x

def Minus(n, p):
    x = n - p
    # if not x.is_integer():
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8:
        x = round(x, 3)
    return x

def Multiply(n, p):
    x = n * p
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8:
        x = round(x, 3)
    return x

def Divide(n, p):
    x = n / p
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8:
        x = round(x, 16)
    return x



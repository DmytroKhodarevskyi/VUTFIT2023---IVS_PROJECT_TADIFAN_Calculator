def Factorial(n):
    if not isinstance(n, int):
        return "error"
    if n == 0:
        return 1
    if n < 0:
        return "error"
    else:
        return n * Factorial(n - 1)

def SquareRoot(n):
    if n < 0:
        return "error"
    return n ** 0.5

def Power(n, p):
    number = n ** p
    number = f"{number:.10e}"
    return number

def Plus(n, p):
    x = n + p
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8:
        x = round(x, 5)
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
    x = f"{x:.10e}"
    return x

def Divide(n, p):
    if p == 0:
        return "error"
    x = n / p
    num_str = str(x)
    num_digits = len(num_str)
    if num_digits > 8:
        x = round(x, 8)
    return x


def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)



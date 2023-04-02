import Calc_Library
import sys
import os

def samplemean(numbers):
    return summs(numbers) / len(numbers)

def summs(numbers):
    summ = 0
    for n in numbers:
        summ = Calc_Library.Plus(summ, n)
    return summ

def stddev(numbers):
        x_sample = samplemean(numbers)
        minus = [Calc_Library.Minus(x, x_sample) for x in numbers]
        sqrt = [Calc_Library.Power(d, 2) for d in minus]
        sum_squares = summs(sqrt)
        N = len(numbers)
        befsq = Calc_Library.Divide(sum_squares, N)
        s = Calc_Library.SquareRoot(befsq)
        return s


cwd = os.getcwd()
file_path = os.path.join(cwd, 'prof')
numbers = []
for line in sys.stdin:
     numbers.extend(map(float, line.strip().split()))
     with open(file_path, 'w') as f:
         f.write("Input :\n" + str(numbers) + "\n" + "s(Standard deviation) =\t" + str(stddev(numbers)))

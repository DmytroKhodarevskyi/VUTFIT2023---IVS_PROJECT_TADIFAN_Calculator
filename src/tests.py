import sys
import unittest
from PySide6.QtWidgets import QApplication, QMainWindow
import main
import Calc_Library

class TestGUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not QApplication.instance():
            cls.app = QApplication(sys.argv)
        else:
            cls.app = QApplication.instance()

    @classmethod
    def tearDownClass(cls):
        del cls.app

    def setUp(self):
        self.calculator = main.Calculator()

    def tearDown(self):
        self.calculator.close()

    def test_write_numbers(self):
        # Checking that all numbers is working
        self.calculator.add_number("0")
        self.calculator.add_number("1")
        self.calculator.add_number("2")
        self.calculator.add_number("3")
        self.calculator.add_number("4")
        self.calculator.add_number("5")
        self.calculator.add_number("6")
        self.calculator.add_number("7")
        self.calculator.add_number("8")
        self.calculator.add_number("9")
        self.calculator.add_number("0")
        self.assertEqual(self.calculator.ui.entry.text(), "1234567890")
        self.calculator.clear_all()

        # Checking 2 digit numbers
        self.calculator.add_number("2")
        self.calculator.add_number("5")
        self.assertEqual(self.calculator.ui.entry.text(), "25")
        self.calculator.clear_all()

        # Checking that , calculator not writing a lot of zeros
        self.assertEqual(self.calculator.ui.entry.text(), "0")
        self.calculator.add_number("0")
        self.calculator.add_number("0")
        self.assertEqual(self.calculator.ui.entry.text(), "0")

        # Checking that, calculator replacing 0 with a number
        self.calculator.add_number("8")
        self.assertEqual(self.calculator.ui.entry.text(), "8")
        self.calculator.clear_all()

        # Checking 3 digit number
        self.calculator.add_number("1")
        self.calculator.add_number("5")
        self.calculator.add_number("9")
        self.assertEqual(self.calculator.ui.entry.text(), "159")
        self.calculator.clear_all()

    def test_for_clear_functions(self):
        # Checking clear_all function
        self.calculator.add_number("1")
        self.calculator.add_number("5")
        self.calculator.add_number("9")
        self.calculator.clear_all()
        self.assertEqual(self.calculator.ui.entry.text(), "0")

        # Checking clear_entry function
        self.calculator.add_number("2")
        self.calculator.add_number("5")
        self.assertEqual(self.calculator.ui.entry.text(), "25")
        self.calculator.clear_entry()
        self.assertEqual(self.calculator.ui.entry.text(), "0")

        # Checking clear_all with operators
        self.calculator.add_number("5")
        self.calculator.add_number("5")
        self.calculator.add_history(" + ")
        self.assertEqual(self.calculator.ui.history.text(), "55 + ")
        self.calculator.clear_all()
        self.assertEqual(self.calculator.ui.history.text(), "")

    def test_writing_point(self):
        # Checking the point , with starting zero
        self.calculator.add_point()
        self.assertEqual(self.calculator.ui.entry.text(), "0,")

        # Add number after point
        self.calculator.add_number("5")
        self.assertEqual(self.calculator.ui.entry.text(), "0,5")

        # Trying to add the second point in the number
        self.calculator.add_point()
        self.assertEqual(self.calculator.ui.entry.text(), "0,5")

        # Add some other numbers to a number
        self.calculator.add_number("5")
        self.calculator.add_number("8")
        self.assertEqual(self.calculator.ui.entry.text(), "0,558")

        # Again try to add another point
        self.calculator.add_point()
        self.assertEqual(self.calculator.ui.entry.text(), "0,558")
        self.calculator.clear_all()

    def test_with_points_in_history(self):
        # Add number with point to history and check if it is correct
        self.calculator.add_number("1")
        self.calculator.add_point()
        self.calculator.add_number("5")
        self.calculator.add_history(" + ")
        self.assertEqual(self.calculator.ui.history.text(), "1,5 + ")

        # Check if the point is not deleted and number in the entry text is correct
        self.calculator.add_number("2")
        self.calculator.add_point()
        self.calculator.add_number("5")
        self.assertEqual(self.calculator.ui.entry.text(), "2,5")
        self.calculator.calculate()
        self.assertEqual(self.calculator.ui.entry.text(), "4")

        # Check if the expression in the history is correct
        self.assertEqual(self.calculator.ui.history.text(), "1,5 + 2,5 =")
        self.calculator.clear_all()

    def test_calculations_with_points(self):

        # Checking for two digit with point and one digit without point
        self.calculator.add_number("44")
        self.calculator.add_point()
        self.calculator.add_number("99")
        self.calculator.add_history(" + ")
        self.calculator.add_number("6")
        self.calculator.add_point()
        self.calculator.add_number("99")
        self.calculator.calculate()
        self.assertEqual(self.calculator.ui.entry.text(), "51,98")
        self.calculator.clear_all()

        # Checking for one digit with point and two digit with point
        self.calculator.add_number("5")
        self.calculator.add_point()
        self.calculator.add_number("99")
        self.calculator.add_history(" + ")
        self.calculator.add_number("53")
        self.calculator.add_point()
        self.calculator.add_number("99")
        self.calculator.calculate()
        self.assertEqual(self.calculator.ui.entry.text(), "59,98")


class TestMathLib(unittest.TestCase):

        def test_add_simple_numbers(self):
            # Checking if the add function is working correctly (simple numbers)
            self.assertEqual(Calc_Library.Plus(3, 5), 8)
            self.assertEqual(Calc_Library.Plus(3, -5), -2)
            self.assertEqual(Calc_Library.Plus(-3, 5), 2)
            self.assertEqual(Calc_Library.Plus(-3, -5), -8)
            self.assertEqual(Calc_Library.Plus(0, 1), 1)
            self.assertEqual(Calc_Library.Plus(0, -1), -1)
            self.assertEqual(Calc_Library.Plus(0, 0), 0)

        def test_add_huge_numbers(self):
            # Checking if the add function is working correctly (huge numbers)
            self.assertEqual(Calc_Library.Plus(1000000, 1000000), 2000000)
            self.assertEqual(Calc_Library.Plus(1000000, -1000000), 0)
            self.assertEqual(Calc_Library.Plus(-1000000, 1000000), 0)
            self.assertEqual(Calc_Library.Plus(999999999999999999999999999, 1), 1000000000000000000000000000)
            self.assertEqual(Calc_Library.Plus(-999999999999999999999999999, 1), -999999999999999999999999998)
            self.assertEqual(Calc_Library.Plus(9876543210123456789, 9876543210123456789), 19753086420246913578)
            self.assertEqual(Calc_Library.Plus(-9876543210123456789, 9876543210123456789), 0)

        def test_add_float_numbers(self):
            # Checking if the add function is working correctly (float numbers)
            self.assertEqual(Calc_Library.Plus(0.5, 0.5), 1)
            self.assertEqual(Calc_Library.Plus(0.5, -0.5), 0)
            self.assertEqual(Calc_Library.Plus(0.5, 0.6), 1.1)
            self.assertEqual(Calc_Library.Plus(0.5, -0.6), -0.1)
            self.assertEqual(Calc_Library.Plus(0.8, 2.3), 3.1)
            self.assertEqual(Calc_Library.Plus(0.8, -2.3), -1.5)

        def test_sub_simple_numbers(self):
            # Checking if the sub function is working correctly (simple numbers)
            self.assertEqual(Calc_Library.Minus(3, 5), -2)
            self.assertEqual(Calc_Library.Minus(3, -5), 8)
            self.assertEqual(Calc_Library.Minus(-3, 5), -8)
            self.assertEqual(Calc_Library.Minus(-3, -5), 2)
            self.assertEqual(Calc_Library.Minus(0, 1), -1)
            self.assertEqual(Calc_Library.Minus(0, -1), 1)
            self.assertEqual(Calc_Library.Minus(0, 0), 0)

        def test_sub_huge_numbers(self):
            # Checking if the sub function is working correctly (huge numbers)
            self.assertEqual(Calc_Library.Minus(999999999, 888888888), 111111111)
            self.assertEqual(Calc_Library.Minus(123456789, 987654321), -864197532)
            self.assertEqual(Calc_Library.Minus(-123456789, 987654321), -1111111110)
            self.assertEqual(Calc_Library.Minus(-123456789, -987654321), 864197532)
            self.assertEqual(Calc_Library.Minus(9876543210123456789, 9876543210123456789), 0)
            self.assertEqual(Calc_Library.Minus(-9876543210123456789, 9876543210123456789), -19753086420246913578)

        def test_sub_float_numbers(self):
            # Checking if the sub function is working correctly (float numbers)
            self.assertEqual(Calc_Library.Minus(0.5, 0.5), 0)
            self.assertEqual(Calc_Library.Minus(0.5, -0.5), 1)
            self.assertEqual(Calc_Library.Minus(0.5, 0.6), -0.1)
            self.assertEqual(Calc_Library.Minus(0.5, -0.6), 1.1)
            self.assertEqual(Calc_Library.Minus(0.8, 2.3), -1.5)
            self.assertEqual(Calc_Library.Minus(0.8, -2.3), 3.1)

        def test_mul(self):
            # Checking if the mul function is working correctly (simple numbers)
            self.assertEqual(Calc_Library.Multiply(3, 5), 15)
            self.assertEqual(Calc_Library.Multiply(4, -6), -24)
            self.assertEqual(Calc_Library.Multiply(-1, 10), -10)
            self.assertEqual(Calc_Library.Multiply(-2, -6), 12)
            self.assertEqual(Calc_Library.Multiply(0, 0), 0)

        def test_mul_by_one(self):
            self.assertEqual(Calc_Library.Multiply(12049120421, 1), 12049120421)
            self.assertEqual(Calc_Library.Multiply(14012401, -1), -14012401)
            self.assertEqual(Calc_Library.Multiply(-43194910, -1), 43194910)

        def test_mul_huge(self):
            # Checking if the mul function is working correctly (huge numbers)
            self.assertEqual(Calc_Library.Multiply(999999999, 888888888), 888888887111111112)
            self.assertEqual(Calc_Library.Multiply(123456789, 987654321), 121932631112635269)
            self.assertEqual(Calc_Library.Multiply(-123456789, 987654321), -121932631112635269)
            self.assertEqual(Calc_Library.Multiply(-123456789, -987654321), 121932631112635269)
            self.assertEqual(Calc_Library.Multiply(123456789, 0), 0)

        def test_mul_float_numbers(self):
            # Checking if the mul function is working correctly (float numbers)
            self.assertEqual(Calc_Library.Multiply(0.5, 0.5), 0.25)
            self.assertEqual(Calc_Library.Multiply(0.5, -0.5), -0.25)
            self.assertEqual(Calc_Library.Multiply(0.5, 0.6), 0.3)
            self.assertEqual(Calc_Library.Multiply(0.5, -0.6), -0.3)
            self.assertEqual(Calc_Library.Multiply(0.8, 2.3), 1.84)
            self.assertEqual(Calc_Library.Multiply(0.8, -2.3), -1.84)

        def test_divide_simple_numbers(self):

            # Checking if the divide function is working correctly (simple numbers)
            self.assertEqual(Calc_Library.Divide(10, 2), 5)
            self.assertEqual(Calc_Library.Divide(20, -2), -10)
            self.assertEqual(Calc_Library.Divide(-15, 3), -5)
            self.assertEqual(Calc_Library.Divide(-30, -3), 10)
            self.assertEqual(Calc_Library.Divide(0, 1), 0)
            self.assertEqual(Calc_Library.Divide(0, -1), 0)

        def test_divide_by_one(self):
            self.assertEqual(Calc_Library.Divide(500, 1), 500)
            self.assertEqual(Calc_Library.Divide(1, 1), 1)
            self.assertEqual(Calc_Library.Divide(0, 1), 0)

        def test_divide_huge_numbers(self):
            # Checking if the divide function is working correctly (huge numbers)
            self.assertEqual(Calc_Library.Divide(999999999, 888888888), 1.125)
            self.assertEqual(Calc_Library.Divide(123456789, 987654321), 0.1249999988609375)
            self.assertEqual(Calc_Library.Divide(-123456789, 987654321), -0.1249999988609375)
            self.assertEqual(Calc_Library.Divide(-123456789, -987654321), 0.1249999988609375)

        def test_divide_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                Calc_Library.Divide(0, 0)
                Calc_Library.Divide(1, 0)
                Calc_Library.Divide(-1, 0)

        def test_divide_float_numbers(self):
            # Checking if the divide function is working correctly (float numbers)
            self.assertEqual(Calc_Library.Divide(0.5, 0.5), 1)
            self.assertEqual(Calc_Library.Divide(3, 5), 0.6)
            self.assertEqual(Calc_Library.Divide(0.5, -0.5), -1)

        def test_power_simple_numbers(self):
            # Checking if the power function is working correctly (simple numbers)
            self.assertEqual(Calc_Library.Power(2, 3), 8)
            self.assertEqual(Calc_Library.Power(2, -3), 0.125)
            self.assertEqual(Calc_Library.Power(-2, 3), -8)
            self.assertEqual(Calc_Library.Power(-2, -3), -0.125)
            self.assertEqual(Calc_Library.Power(0, 1), 0)
            self.assertEqual(Calc_Library.Power(0, 0), 1)

        def test_power_huge_numbers(self):
            self.assertEqual(Calc_Library.Power(154, 0), 1)
            self.assertEqual(Calc_Library.Power(157, 2), 24649)
            self.assertEqual(Calc_Library.Power(157, 3), 3869893)
            self.assertEqual(Calc_Library.Power(157, 4), 607573201)

        def test_power_float_numbers(self):
            self.assertEqual(Calc_Library.Power(0.5, 0.5), 0.7071067811865476)
            self.assertEqual(Calc_Library.Power(0.5, -0.5), 1.4142135623730951)
            self.assertEqual(Calc_Library.Power(0.5, 0.6),  0.6597539553864471)
            self.assertEqual(Calc_Library.Power(0.5, -0.6), 1.515716566510398)
            self.assertEqual(Calc_Library.Power(0.8, 2.3),  0.5985590066064778)
            self.assertEqual(Calc_Library.Power(0.8, -2.3), 1.670679062486231)

        def test_square_root_simple_numbers(self):
            # Checking if the square root function is working correctly (simple numbers)
            self.assertEqual(Calc_Library.SquareRoot(4), 2)
            self.assertEqual(Calc_Library.SquareRoot(9), 3)
            self.assertEqual(Calc_Library.SquareRoot(16), 4)
            self.assertEqual(Calc_Library.SquareRoot(25), 5)
            self.assertEqual(Calc_Library.SquareRoot(36), 6)
            self.assertEqual(Calc_Library.SquareRoot(49), 7)

        def test_square_root_huge_numbers(self):
            self.assertEqual(Calc_Library.SquareRoot(100000000), 10000)
            self.assertEqual(Calc_Library.SquareRoot(16000000000), 126491.10640673517)
            self.assertEqual(Calc_Library.SquareRoot(256000000000), 505964.4256269407)

        def test_square_root_float_numbers(self):
            self.assertEqual(Calc_Library.SquareRoot(0.25), 0.5)
            self.assertEqual(Calc_Library.SquareRoot(0.125), 0.3535533905932738)
            self.assertEqual(Calc_Library.SquareRoot(0.0625), 0.25)
            self.assertEqual(Calc_Library.SquareRoot(0.36), 0.6)
            self.assertEqual(Calc_Library.SquareRoot(0.49), 0.7)
            self.assertEqual(Calc_Library.SquareRoot(0.64), 0.8)
            self.assertEqual(Calc_Library.SquareRoot(0.810000000000000000), 0.9)
            self.assertEqual(Calc_Library.SquareRoot(1.0000000000000000000000000), 1.0)

        def test_factorial_simple_numbers(self):

            # Checking if the factorial function is working correctly (simple numbers)
            self.assertEqual(Calc_Library.Factorial(1), 1)
            self.assertEqual(Calc_Library.Factorial(2), 2)
            self.assertEqual(Calc_Library.Factorial(3), 6)
            self.assertEqual(Calc_Library.Factorial(4), 24)
            self.assertEqual(Calc_Library.Factorial(5), 120)
            self.assertEqual(Calc_Library.Factorial(6), 720)
            self.assertEqual(Calc_Library.Factorial(7), 5040)
            self.assertEqual(Calc_Library.Factorial(8), 40320)
            self.assertEqual(Calc_Library.Factorial(9), 362880)
            self.assertEqual(Calc_Library.Factorial(10), 3628800)

        def test_factorial_float_numbers(self):
            with self.assertRaises(TypeError):
                Calc_Library.Factorial(5.5)
                Calc_Library.Factorial(55.5)
                Calc_Library.Factorial(4.5)

        def test_factorial_negative_numbers(self):
            with self.assertRaises(ValueError):
                Calc_Library.Factorial(-1)
                Calc_Library.Factorial(-2)
                Calc_Library.Factorial(-3)
                Calc_Library.Factorial(-4)
                Calc_Library.Factorial(-5)
                Calc_Library.Factorial(-6)
                Calc_Library.Factorial(-7)
                Calc_Library.Factorial(-8)
                Calc_Library.Factorial(-9)
                Calc_Library.Factorial(-10)

        def test_factorial_zero(self):
            self.assertEqual(Calc_Library.Factorial(0), 1)





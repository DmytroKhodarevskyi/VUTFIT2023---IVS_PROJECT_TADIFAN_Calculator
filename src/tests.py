import sys
import unittest
from PySide6.QtWidgets import QApplication, QMainWindow
import main

class MyTestGUI(unittest.TestCase):
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
        self.calculator.add_number("1")
        self.calculator.add_number("5")
        self.calculator.add_number("9")
        self.calculator.clear_all()
        self.assertEqual(self.calculator.ui.entry.text(), "0")
        self.calculator.add_number("2")
        self.calculator.add_number("5")
        self.calculator.calculate()
        self.assertEqual(self.calculator.ui.entry.text(), "25")








    def test_writing_point(self):

        # Checking the point , with starting zero
        self.calculator.add_point()
        self.assertEqual(self.calculator.ui.entry.text(), "0.")

        # Add number after point
        self.calculator.add_number("5")
        self.assertEqual(self.calculator.ui.entry.text(), "0.5")

        # Trying to add the second point in the number
        self.calculator.add_point()
        self.assertEqual(self.calculator.ui.entry.text(), "0.5")

        # Add some other numbers to a number
        self.calculator.add_number("5")
        self.calculator.add_number("8")
        self.assertEqual(self.calculator.ui.entry.text(), "0.558")

        # Again try to add another point
        self.calculator.add_point()
        self.assertEqual(self.calculator.ui.entry.text(), "0.558")
        self.calculator.clear_all()


    def test_with_points_in_history(self):

        # Add number with point to history and check if it is correct
        self.calculator.add_number("1")
        self.calculator.add_point()
        self.calculator.add_number("5")
        self.calculator.add_history(" + ")
        self.assertEqual(self.calculator.ui.history.text(), "1.5 + ")

        # Check if the point is not deleted and number in the entry text is correct
        self.calculator.add_number("2")
        self.calculator.add_point()
        self.calculator.add_number("5")
        self.assertEqual(self.calculator.ui.entry.text(), "2.5")
        self.calculator.calculate()
        self.assertEqual(self.calculator.ui.entry.text(), "4")

        # Check if the expression in the history is correct
        self.assertEqual(self.calculator.ui.history.text(), "1.5 + 2.5 =")
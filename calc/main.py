import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox, QCheckBox, QFileDialog, QProgressBar, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QMenu, QAction, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QCoreApplication
from PyQt5.QtGui import QCursor
from typing import Union, Optional
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from Newdesign import Ui_MainWindow
from operator import add, sub, mul, truediv

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv
}

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("Rubik\static\Rubik-Bold.ttf")

        self.ui.Button_0.clicked.connect(lambda: self.add_number("0"))
        self.ui.Button_1.clicked.connect(lambda: self.add_number("1"))
        self.ui.Button_2.clicked.connect(lambda: self.add_number("2"))
        self.ui.Button_3.clicked.connect(lambda: self.add_number("3"))
        self.ui.Button_4.clicked.connect(lambda: self.add_number("4"))
        self.ui.Button_5.clicked.connect(lambda: self.add_number("5"))
        self.ui.Button_6.clicked.connect(lambda: self.add_number("6"))
        self.ui.Button_7.clicked.connect(lambda: self.add_number("7"))
        self.ui.Button_8.clicked.connect(lambda: self.add_number("8"))
        self.ui.Button_9.clicked.connect(lambda: self.add_number("9"))

        #clears
        self.ui.Button_c.clicked.connect(self.clear_all)
        self.ui.Button_ce.clicked.connect(self.clear_entry)

        #actions
        self.ui.Button_Comma.clicked.connect(self.add_point)

        #math
        self.ui.Button_Equal.clicked.connect(self.calculate)
        self.ui.Button_Plus.clicked.connect(lambda: self.add_history(" + "))

    def add_number(self, Button_text: str) -> None:
        if self.ui.entry.text() == "0":
            self.ui.entry.setText(Button_text)
        else:
            self.ui.entry.setText(self.ui.entry.text() + Button_text)

    def add_point(self) -> None:
        if ',' not in self.ui.entry.text():
            self.ui.entry.setText(self.ui.entry.text() + ',')

    def clear_all(self) -> None:
        self.ui.entry.setText("0")
        self.ui.history.clear()

    def clear_entry(self) -> None:
        self.ui.entry.setText("0")

    def add_history(self, math_sign: str) -> None:
       if not self.ui.history.text():
           history = self.remove_trailing_zeroes(self.ui.entry.text()) + f'{math_sign}'
           history = history.replace(".", ",")
           self.ui.history.setText(history)
           self.ui.entry.setText("0")

    @staticmethod
    def remove_trailing_zeroes(number: str) -> str:

        n = str(number)
        n = n.replace(",", ".")
        n = str(float(n))

        return n[:-2] if n.endswith('.0') else n

    def get_entry_number(self) -> Union[int, float]:
        entry = self.ui.entry.text().strip(',')
        entry = entry.replace(",", ".")
        print(entry)
        return float(entry) if '.' in entry else int(entry)

    def get_history_number(self) -> Union[int, float, None]:
        history = self.ui.history.text().strip(',').split()[0]
        history = history.replace(",", ".")
        print(history)
        return float(history) if '.' in history else int(history)

    def get_history_sign(self) -> Optional[str]:
        if self.ui.history.text():
            return self.ui.history.text().strip(',').split()[-1]


    def calculate(self) -> Optional[str]:
        entry = self.ui.entry.text()
        temp = self.ui.history.text()

        if temp:
            result = self.remove_trailing_zeroes(
                str(operations[self.get_history_sign()](self.get_history_number(), self.get_entry_number()))
            )
            result = result.replace(".", ",")
            history = temp + self.remove_trailing_zeroes(entry) + " ="
            history = history.replace(".", ",")
            self.ui.history.setText(history)
            self.ui.entry.setText(result)
            return result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())


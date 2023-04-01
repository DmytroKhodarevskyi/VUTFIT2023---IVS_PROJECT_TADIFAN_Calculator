import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox, QCheckBox, QFileDialog, QProgressBar, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QMenu, QAction, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QCoreApplication
from PyQt5.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase
from Newdesign import Ui_MainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

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
        self.ui.Button_Plus.clicked.connect(lambda: self.add_history("+"))

    def add_number(self, Button_text: str) -> None:
        if self.ui.entry.text() == "0":
            self.ui.entry.setText(Button_text)
        else:
            self.ui.entry.setText(self.ui.entry.text() + Button_text)

    def add_point(self) -> None:
        if '.' not in self.ui.entry.text():
            self.ui.entry.setText(self.ui.entry.text() + '.')

    def clear_all(self) -> None:
        self.ui.entry.setText("0")
        self.ui.history.clear()

    def clear_entry(self) -> None:
        self.ui.entry.setText("0")

    def add_history(self, math_sign: str) -> None:
       if not self.ui.history.text():
           self.ui.history.setText(self.remove_trailing_zeroes(self.ui.entry.text()) + f'{math_sign}')
           self.ui.entry.setText("0")

    @staticmethod
    def remove_trailing_zeroes(number: str) -> str:
        n = str(float(number))
        return n[:-2] if n.endswith('.0') else n

    def get_entry_number(self) -> float:
        entry = self.ui.entry.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())




################################################################################
## Form generated from reading UI file 'My_design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/free-icon-calculator-7378252.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: rgb(18, 18, 18);\n"
"	font-family: Rubik;\n"
"	font-size: 16pt; \n"
"	font-weight: 600;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(300, 500))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.history = QLabel(self.centralwidget)
        self.history.setObjectName(u"history")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history.sizePolicy().hasHeightForWidth())
        self.history.setSizePolicy(sizePolicy)
        self.history.setMinimumSize(QSize(0, 33))
        self.history.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.history.setFont(font1)
        self.history.setStyleSheet(u"color: gray;\n"
"background-color: rgb(29, 29, 29);\n"
"font-family: Bahnschrift;\n"
"border-radius: 5px;")
        self.history.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.history)

        self.entry = QLineEdit(self.centralwidget)
        self.entry.setObjectName(u"entry")
        sizePolicy.setHeightForWidth(self.entry.sizePolicy().hasHeightForWidth())
        self.entry.setSizePolicy(sizePolicy)
        self.entry.setMinimumSize(QSize(0, 83))
        self.entry.setMaximumSize(QSize(16777215, 83))
        self.entry.setStyleSheet(u"font-size: 40pt;\n"
"background-color: rgb(30, 30, 30);\n"
"border: none;\n"
"border-radius: 10px;\n"
"   ")
        self.entry.setMaxLength(16)
        self.entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.entry.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.entry)

        self.ButtonsGrid = QFrame(self.centralwidget)
        self.ButtonsGrid.setObjectName(u"ButtonsGrid")
        self.ButtonsGrid.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ButtonsGrid.sizePolicy().hasHeightForWidth())
        self.ButtonsGrid.setSizePolicy(sizePolicy1)
        self.ButtonsGrid.setFont(font)
        self.ButtonsGrid.setStyleSheet(u"")
        self.Buttons_Container_3 = QGridLayout(self.ButtonsGrid)
        self.Buttons_Container_3.setSpacing(5)
        self.Buttons_Container_3.setObjectName(u"Buttons_Container_3")
        self.Buttons_Container_3.setContentsMargins(5, 5, 5, 5)
        self.Button_8 = QPushButton(self.ButtonsGrid)
        self.Button_8.setObjectName(u"Button_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy2)
        self.Button_8.setMinimumSize(QSize(0, 0))
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_8.setIconSize(QSize(105, 105))
        self.Button_8.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_8, 3, 1, 1, 1)

        self.Button_7 = QPushButton(self.ButtonsGrid)
        self.Button_7.setObjectName(u"Button_7")
        sizePolicy2.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy2)
        self.Button_7.setMinimumSize(QSize(0, 0))
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_7.setIconSize(QSize(105, 105))
        self.Button_7.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_7, 3, 0, 1, 1)

        self.Button_6 = QPushButton(self.ButtonsGrid)
        self.Button_6.setObjectName(u"Button_6")
        sizePolicy2.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy2)
        self.Button_6.setMinimumSize(QSize(0, 0))
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_6.setIconSize(QSize(105, 105))
        self.Button_6.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_6, 2, 2, 1, 1)

        self.Button_Power = QPushButton(self.ButtonsGrid)
        self.Button_Power.setObjectName(u"Button_Power")
        sizePolicy2.setHeightForWidth(self.Button_Power.sizePolicy().hasHeightForWidth())
        self.Button_Power.setSizePolicy(sizePolicy2)
        self.Button_Power.setMinimumSize(QSize(0, 0))
        self.Button_Power.setFont(font)
        self.Button_Power.setMouseTracking(True)
        self.Button_Power.setTabletTracking(True)
        self.Button_Power.setStyleSheet(u"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #333333;\n"
"	border-radius: 10px;\n"
"color: #0094C6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	/*color: #333;*/\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_Power.setIcon(icon1)
        self.Button_Power.setIconSize(QSize(30, 30))
        self.Button_Power.setCheckable(False)
        self.Button_Power.setChecked(False)
        self.Button_Power.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Power, 2, 4, 1, 1)

        self.Button_3 = QPushButton(self.ButtonsGrid)
        self.Button_3.setObjectName(u"Button_3")
        sizePolicy2.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy2)
        self.Button_3.setMinimumSize(QSize(0, 0))
        self.Button_3.setSizeIncrement(QSize(2, 2))
        self.Button_3.setFont(font)
        self.Button_3.setMouseTracking(True)
        self.Button_3.setTabletTracking(True)
        self.Button_3.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_3.setIconSize(QSize(105, 105))
        self.Button_3.setCheckable(False)
        self.Button_3.setChecked(False)
        self.Button_3.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_3, 1, 2, 1, 1)

        self.Button_Divide = QPushButton(self.ButtonsGrid)
        self.Button_Divide.setObjectName(u"Button_Divide")
        sizePolicy2.setHeightForWidth(self.Button_Divide.sizePolicy().hasHeightForWidth())
        self.Button_Divide.setSizePolicy(sizePolicy2)
        self.Button_Divide.setMinimumSize(QSize(0, 0))
        self.Button_Divide.setFont(font)
        self.Button_Divide.setMouseTracking(True)
        self.Button_Divide.setTabletTracking(True)
        self.Button_Divide.setStyleSheet(u"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #333333;\n"
"	border-radius: 10px;\n"
"color: #0094C6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #333;\n"
"}")
        self.Button_Divide.setIconSize(QSize(105, 105))
        self.Button_Divide.setCheckable(False)
        self.Button_Divide.setChecked(False)
        self.Button_Divide.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Divide, 1, 3, 1, 1)

        self.Button_2 = QPushButton(self.ButtonsGrid)
        self.Button_2.setObjectName(u"Button_2")
        sizePolicy2.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy2)
        self.Button_2.setMinimumSize(QSize(0, 0))
        self.Button_2.setFont(font)
        self.Button_2.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_2.setIconSize(QSize(105, 105))
        self.Button_2.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_2, 1, 1, 1, 1)

        self.Button_Plus = QPushButton(self.ButtonsGrid)
        self.Button_Plus.setObjectName(u"Button_Plus")
        sizePolicy2.setHeightForWidth(self.Button_Plus.sizePolicy().hasHeightForWidth())
        self.Button_Plus.setSizePolicy(sizePolicy2)
        self.Button_Plus.setMinimumSize(QSize(0, 0))
        self.Button_Plus.setFont(font)
        self.Button_Plus.setMouseTracking(True)
        self.Button_Plus.setTabletTracking(True)
        self.Button_Plus.setStyleSheet(u"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #333333;\n"
"	border-radius: 10px;\n"
"color: #0094C6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #333;\n"
"}")
        self.Button_Plus.setIconSize(QSize(105, 105))
        self.Button_Plus.setCheckable(False)
        self.Button_Plus.setChecked(False)
        self.Button_Plus.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Plus, 3, 3, 1, 1)

        self.Button_9 = QPushButton(self.ButtonsGrid)
        self.Button_9.setObjectName(u"Button_9")
        sizePolicy2.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy2)
        self.Button_9.setMinimumSize(QSize(0, 0))
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_9.setIconSize(QSize(105, 105))
        self.Button_9.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_9, 3, 2, 1, 1)

        self.Button_Minus = QPushButton(self.ButtonsGrid)
        self.Button_Minus.setObjectName(u"Button_Minus")
        sizePolicy2.setHeightForWidth(self.Button_Minus.sizePolicy().hasHeightForWidth())
        self.Button_Minus.setSizePolicy(sizePolicy2)
        self.Button_Minus.setMinimumSize(QSize(0, 0))
        self.Button_Minus.setFont(font)
        self.Button_Minus.setMouseTracking(True)
        self.Button_Minus.setTabletTracking(True)
        self.Button_Minus.setStyleSheet(u"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #333333;\n"
"	border-radius: 10px;\n"
"color: #0094C6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #333;\n"
"}")
        self.Button_Minus.setIconSize(QSize(105, 105))
        self.Button_Minus.setCheckable(False)
        self.Button_Minus.setChecked(False)
        self.Button_Minus.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Minus, 4, 3, 1, 1)

        self.Button_4 = QPushButton(self.ButtonsGrid)
        self.Button_4.setObjectName(u"Button_4")
        sizePolicy2.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy2)
        self.Button_4.setMinimumSize(QSize(0, 0))
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_4.setIconSize(QSize(105, 105))
        self.Button_4.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_4, 2, 0, 1, 1)

        self.Button_Factorial = QPushButton(self.ButtonsGrid)
        self.Button_Factorial.setObjectName(u"Button_Factorial")
        sizePolicy2.setHeightForWidth(self.Button_Factorial.sizePolicy().hasHeightForWidth())
        self.Button_Factorial.setSizePolicy(sizePolicy2)
        self.Button_Factorial.setMinimumSize(QSize(0, 0))
        self.Button_Factorial.setFont(font)
        self.Button_Factorial.setMouseTracking(True)
        self.Button_Factorial.setTabletTracking(True)
        self.Button_Factorial.setStyleSheet(u"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #333333;\n"
"	border-radius: 10px;\n"
"color: #0094C6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	/*color: #333;*/\n"
"}")
        self.Button_Factorial.setIconSize(QSize(105, 105))
        self.Button_Factorial.setCheckable(False)
        self.Button_Factorial.setChecked(False)
        self.Button_Factorial.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Factorial, 3, 4, 1, 1)

        self.Button_Root = QPushButton(self.ButtonsGrid)
        self.Button_Root.setObjectName(u"Button_Root")
        sizePolicy2.setHeightForWidth(self.Button_Root.sizePolicy().hasHeightForWidth())
        self.Button_Root.setSizePolicy(sizePolicy2)
        self.Button_Root.setMinimumSize(QSize(0, 0))
        self.Button_Root.setFont(font)
        self.Button_Root.setMouseTracking(True)
        self.Button_Root.setTabletTracking(True)
        self.Button_Root.setStyleSheet(u"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #333333;\n"
"	border-radius: 10px;\n"
"color: #0094C6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	/*color: #333;*/\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/square-root-of-x-mathematical-signs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_Root.setIcon(icon2)
        self.Button_Root.setIconSize(QSize(30, 30))
        self.Button_Root.setCheckable(False)
        self.Button_Root.setChecked(False)
        self.Button_Root.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Root, 1, 4, 1, 1)

        self.Button_Multiply = QPushButton(self.ButtonsGrid)
        self.Button_Multiply.setObjectName(u"Button_Multiply")
        sizePolicy2.setHeightForWidth(self.Button_Multiply.sizePolicy().hasHeightForWidth())
        self.Button_Multiply.setSizePolicy(sizePolicy2)
        self.Button_Multiply.setMinimumSize(QSize(0, 0))
        self.Button_Multiply.setFont(font)
        self.Button_Multiply.setMouseTracking(True)
        self.Button_Multiply.setTabletTracking(True)
        self.Button_Multiply.setStyleSheet(u"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #333333;\n"
"	border-radius: 10px;\n"
"color: #0094C6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #333;\n"
"}")
        self.Button_Multiply.setIconSize(QSize(105, 105))
        self.Button_Multiply.setCheckable(False)
        self.Button_Multiply.setChecked(False)
        self.Button_Multiply.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Multiply, 2, 3, 1, 1)

        self.Button_5 = QPushButton(self.ButtonsGrid)
        self.Button_5.setObjectName(u"Button_5")
        sizePolicy2.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy2)
        self.Button_5.setMinimumSize(QSize(0, 0))
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_5.setIconSize(QSize(105, 105))
        self.Button_5.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_5, 2, 1, 1, 1)

        self.Button_ce = QPushButton(self.ButtonsGrid)
        self.Button_ce.setObjectName(u"Button_ce")
        sizePolicy2.setHeightForWidth(self.Button_ce.sizePolicy().hasHeightForWidth())
        self.Button_ce.setSizePolicy(sizePolicy2)
        self.Button_ce.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #666;\n"
"	border-radius: 10px;\n"
"color: #333;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #999;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #bbb;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #121212\n"
"}")
        self.Button_ce.setIconSize(QSize(105, 105))
        self.Button_ce.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_ce, 0, 1, 1, 1)

        self.Button_Comma = QPushButton(self.ButtonsGrid)
        self.Button_Comma.setObjectName(u"Button_Comma")
        sizePolicy2.setHeightForWidth(self.Button_Comma.sizePolicy().hasHeightForWidth())
        self.Button_Comma.setSizePolicy(sizePolicy2)
        self.Button_Comma.setMinimumSize(QSize(0, 0))
        self.Button_Comma.setFont(font)
        self.Button_Comma.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_Comma.setIconSize(QSize(105, 105))
        self.Button_Comma.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Comma, 4, 2, 1, 1)

        self.Button_Equal = QPushButton(self.ButtonsGrid)
        self.Button_Equal.setObjectName(u"Button_Equal")
        sizePolicy2.setHeightForWidth(self.Button_Equal.sizePolicy().hasHeightForWidth())
        self.Button_Equal.setSizePolicy(sizePolicy2)
        self.Button_Equal.setMinimumSize(QSize(0, 0))
        self.Button_Equal.setFont(font)
        self.Button_Equal.setMouseTracking(True)
        self.Button_Equal.setTabletTracking(True)
        self.Button_Equal.setStyleSheet(u"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #08a;\n"
"	border-radius: 10px;\n"
"color: #333333;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #0ac;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #0cf;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #fff;\n"
"}")
        self.Button_Equal.setIconSize(QSize(105, 105))
        self.Button_Equal.setCheckable(False)
        self.Button_Equal.setChecked(False)
        self.Button_Equal.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Equal, 4, 4, 1, 1)

        self.Button_c = QPushButton(self.ButtonsGrid)
        self.Button_c.setObjectName(u"Button_c")
        sizePolicy2.setHeightForWidth(self.Button_c.sizePolicy().hasHeightForWidth())
        self.Button_c.setSizePolicy(sizePolicy2)
        self.Button_c.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #666;\n"
"	border-radius: 10px;\n"
"	color: #333;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #999;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #bbb;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #121212\n"
"}")
        self.Button_c.setIconSize(QSize(105, 105))
        self.Button_c.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_c, 0, 0, 1, 1)

        self.Button_0 = QPushButton(self.ButtonsGrid)
        self.Button_0.setObjectName(u"Button_0")
        sizePolicy2.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy2)
        self.Button_0.setMinimumSize(QSize(0, 0))
        self.Button_0.setSizeIncrement(QSize(1, 0))
        self.Button_0.setFont(font)
        self.Button_0.setToolTipDuration(-1)
        self.Button_0.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_0.setIconSize(QSize(105, 105))
        self.Button_0.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_0, 4, 0, 1, 2)

        self.Button_Sign = QPushButton(self.ButtonsGrid)
        self.Button_Sign.setObjectName(u"Button_Sign")
        sizePolicy2.setHeightForWidth(self.Button_Sign.sizePolicy().hasHeightForWidth())
        self.Button_Sign.setSizePolicy(sizePolicy2)
        self.Button_Sign.setMinimumSize(QSize(0, 0))
        self.Button_Sign.setFont(font)
        self.Button_Sign.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #666;\n"
"	border-radius: 10px;\n"
"color: #333;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #999;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #bbb;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #121212\n"
"}")
        self.Button_Sign.setIconSize(QSize(105, 105))
        self.Button_Sign.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_Sign, 0, 2, 1, 1)

        self.Button_backspace = QPushButton(self.ButtonsGrid)
        self.Button_backspace.setObjectName(u"Button_backspace")
        sizePolicy2.setHeightForWidth(self.Button_backspace.sizePolicy().hasHeightForWidth())
        self.Button_backspace.setSizePolicy(sizePolicy2)
        self.Button_backspace.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #333333;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #888;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"	color: #Dff;\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/outline_backspace_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_backspace.setIcon(icon3)
        self.Button_backspace.setIconSize(QSize(30, 30))
        self.Button_backspace.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_backspace, 0, 3, 1, 2)

        self.Button_1 = QPushButton(self.ButtonsGrid)
        self.Button_1.setObjectName(u"Button_1")
        self.Button_1.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy2)
        self.Button_1.setMinimumSize(QSize(0, 0))
        self.Button_1.setSizeIncrement(QSize(2, 2))
        self.Button_1.setFont(font)
        self.Button_1.setMouseTracking(True)
        self.Button_1.setTabletTracking(True)
        self.Button_1.setStyleSheet(u"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"width: 5px;\n"
"    color: #FFF;\n"
"    background-color: #222;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #444;\n"
"	border-bottom: 2px solid rgb(128, 128, 128);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #666;\n"
"	border-bottom: 2px solid rgb(255, 255, 255);\n"
"color: #Dff;\n"
"}")
        self.Button_1.setIconSize(QSize(105, 105))
        self.Button_1.setCheckable(False)
        self.Button_1.setFlat(True)

        self.Buttons_Container_3.addWidget(self.Button_1, 1, 0, 1, 1)

        self.Buttons_Container_3.setRowStretch(0, 1)
        self.Buttons_Container_3.setRowStretch(1, 1)
        self.Buttons_Container_3.setRowStretch(2, 1)
        self.Buttons_Container_3.setRowStretch(3, 1)
        self.Buttons_Container_3.setRowStretch(4, 1)
        self.Buttons_Container_3.setColumnStretch(0, 1)
        self.Buttons_Container_3.setColumnStretch(1, 1)
        self.Buttons_Container_3.setColumnStretch(2, 1)
        self.Buttons_Container_3.setColumnStretch(3, 1)
        self.Buttons_Container_3.setColumnStretch(4, 1)

        self.verticalLayout_2.addWidget(self.ButtonsGrid)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.history.setText("")
        self.entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        # self.Button_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.Button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        # self.Button_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.Button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        # self.Button_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Power.setText("")
        self.Button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        # self.Button_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
#if QT_CONFIG(shortcut)
        # self.Button_Divide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.Button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        # self.Button_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        # self.Button_Plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.Button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        # self.Button_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        # self.Button_Minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.Button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        # self.Button_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Factorial.setText(QCoreApplication.translate("MainWindow", u"x!", None))
        self.Button_Root.setText("")
        self.Button_Multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.Button_Multiply.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.Button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        # self.Button_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.Button_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.Button_Comma.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)

        for sc in (',', '.'):
            QShortcut(sc, self.Button_Comma).activated.connect(self.Button_Comma.animateClick)

#endif // QT_CONFIG(shortcut)
        self.Button_Equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)

        for sc in ('=', 'Enter', 'Return'):
                QShortcut(sc, self.Button_Equal).activated.connect(self.Button_Equal.animateClick)

#endif // QT_CONFIG(shortcut)
        self.Button_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        # self.Button_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.Button_Sign.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.Button_backspace.setText("")
#if QT_CONFIG(shortcut)
        # self.Button_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        # self.Button_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


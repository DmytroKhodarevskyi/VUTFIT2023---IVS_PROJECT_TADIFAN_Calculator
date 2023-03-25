# -*- coding: utf-8 -*-

    def Button_1_Click(self):
        self.Display.setText(self.Display.text() + "1")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True

    def Button_2_Click(self):
        self.Display.setText(self.Display.text() + "2")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True


    def Button_3_Click(self):
        self.Display.setText(self.Display.text() + "3")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True


    def Button_4_Click(self):
        self.Display.setText(self.Display.text() + "4")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True


    def Button_5_Click(self):
        self.Display.setText(self.Display.text() + "5")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True


    def Button_6_Click(self):
        self.Display.setText(self.Display.text() + "6")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True


    def Button_7_Click(self):
        self.Display.setText(self.Display.text() + "7")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True


    def Button_8_Click(self):
        self.Display.setText(self.Display.text() + "8")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True
        print(Ui_MainWindow.CanPlaceComma)


    def Button_9_Click(self):
        self.Display.setText(self.Display.text() + "9")
        Ui_MainWindow.NoMoreOperators = False
        Ui_MainWindow.IsLastIsNumber = True


    def Button_0_Click(self):
        print("ABOOOOOBA")

        CanPlaceNulls = False
        expression = self.Display.text()

        last_op_index = max(expression.rfind(op) for op in ['+', '-', '*', '/'])
        if last_op_index == -1:
                last_num_str = expression
        else:
                last_num_str = expression[last_op_index + 1:]

        if "," in last_num_str:
                CanPlaceNulls = True
        else:
                CanPlaceNulls = False

        if CanPlaceNulls == True or Ui_MainWindow.IsLastIsNumber == True:
                self.Display.setText(self.Display.text() + "0")
                Ui_MainWindow.NoMoreOperators = False
                Ui_MainWindow.IsLastIsNumber = True



    def Button_Comma_Click(self):
        print(Ui_MainWindow.CanPlaceComma, Ui_MainWindow.IsLastIsNumber)

        if Ui_MainWindow.CanPlaceComma == True and Ui_MainWindow.IsLastIsNumber == True:
            self.Display.setText(self.Display.text() + ",")
        Ui_MainWindow.CanPlaceComma = False

        expression = self.Display.text()


        last_op_index = max(expression.rfind(op) for op in ['+', '-', '*', '/'])
        if last_op_index == -1:
                last_num_str = expression
                print(last_num_str)
        else:
                last_num_str = expression[last_op_index + 1:]

        if expression == "" or last_num_str == "":
                self.Display.setText(self.Display.text() + "0,")
                Ui_MainWindow.CanPlaceComma = False
                Ui_MainWindow.IsLastIsNumber = False
                Ui_MainWindow.NoMoreOperators = False

        print(last_num_str)
        if "," in last_num_str:
                Ui_MainWindow.CanPlaceComma = False
        elif expression != "":
                Ui_MainWindow.CanPlaceComma = True

    def Button_Plus_Click(self):
        if Ui_MainWindow.NoMoreOperators == False and Ui_MainWindow.IsLastIsNumber == True:
                self.Display.setText(self.Display.text() + "+")
        Ui_MainWindow.NoMoreOperators = True
        Ui_MainWindow.CanPlaceComma = True
        Ui_MainWindow.IsLastIsNumber = False

    def Button_Minus_Click(self):
        print(Ui_MainWindow.NoMoreOperators, Ui_MainWindow.IsLastIsNumber)
        if Ui_MainWindow.NoMoreOperators == False and Ui_MainWindow.IsLastIsNumber == True:
                self.Display.setText(self.Display.text() + "-")
        Ui_MainWindow.NoMoreOperators = True
        Ui_MainWindow.CanPlaceComma = True
        Ui_MainWindow.IsLastIsNumber = False


    def Button_Multiply_Click(self):
        print(Ui_MainWindow.NoMoreOperators, Ui_MainWindow.IsLastIsNumber)

        if Ui_MainWindow.NoMoreOperators == False and Ui_MainWindow.IsLastIsNumber == True:
                self.Display.setText(self.Display.text() + "*")
        Ui_MainWindow.NoMoreOperators = True
        Ui_MainWindow.CanPlaceComma = True
        Ui_MainWindow.IsLastIsNumber = False


    def Button_Divide_Click(self):
        print(Ui_MainWindow.NoMoreOperators, Ui_MainWindow.IsLastIsNumber)

        if Ui_MainWindow.NoMoreOperators == False and Ui_MainWindow.IsLastIsNumber == True:
                self.Display.setText(self.Display.text() + "/")
        Ui_MainWindow.NoMoreOperators = True
        Ui_MainWindow.CanPlaceComma = True
        Ui_MainWindow.IsLastIsNumber = False

    def Button_Backspace_Click(self):
            self.Display.setText(self.Display.text()[:-1])
            expression = self.Display.text()
            last_symbol = expression[-1]
            symbols = "+-*/"
            # print(type(expression), expression)
            # print(last_symbol)
            if last_symbol not in symbols:
                    # print("if")
                    Ui_MainWindow.NoMoreOperators = False
                    Ui_MainWindow.IsLastIsNumber = True
                    Ui_MainWindow.CanPlaceComma = True
            else:
                    # print("else")
                    Ui_MainWindow.NoMoreOperators = True
                    Ui_MainWindow.IsLastIsNumber = False
                    Ui_MainWindow.CanPlaceComma = True

            last_op_index = max(expression.rfind(op) for op in ['+', '-', '*', '/'])
            if last_op_index == -1:
                    last_num_str = expression
            else:
                    last_num_str = expression[last_op_index + 1:]

            if "," in last_num_str:
                    Ui_MainWindow.CanPlaceComma = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Background = QtWidgets.QWidget(self.centralwidget)
        self.Background.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy)
        self.Background.setMaximumSize(QtCore.QSize(1920, 1080))
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet("QWidget{\n"
"background: black\n"
"}\n"
"")
        self.Background.setObjectName("Background")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Background)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Main_Container = QtWidgets.QGridLayout()
        self.Main_Container.setContentsMargins(10, 50, 20, 10)
        self.Main_Container.setHorizontalSpacing(30)
        self.Main_Container.setVerticalSpacing(100)
        self.Main_Container.setObjectName("Main_Container")
        self.ButtonsGrid = QtWidgets.QFrame(self.Background)
        self.ButtonsGrid.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ButtonsGrid.sizePolicy().hasHeightForWidth())
        self.ButtonsGrid.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.ButtonsGrid.setFont(font)
        self.ButtonsGrid.setObjectName("ButtonsGrid")
        self.Buttons_Container = QtWidgets.QGridLayout(self.ButtonsGrid)
        self.Buttons_Container.setContentsMargins(-1, -1, 1, 10)
        self.Buttons_Container.setHorizontalSpacing(1)
        self.Buttons_Container.setVerticalSpacing(12)
        self.Buttons_Container.setObjectName("Buttons_Container")
        self.Button_6 = QtWidgets.QPushButton(self.ButtonsGrid)
        self.Button_6.clicked.connect(self.Button_6_Click)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_6.sizePolicy().hasHeightForWidth())
        self.Button_6.setSizePolicy(sizePolicy)
        self.Button_6.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_6.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_6.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_6_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_6.setIconSize(QtCore.QSize(105, 105))
        self.Button_6.setFlat(True)
        self.Button_6.setObjectName("Button_6")
        self.Buttons_Container.addWidget(self.Button_6, 1, 2, 1, 1)
        self.Button_Power = QtWidgets.QPushButton(self.ButtonsGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Power.sizePolicy().hasHeightForWidth())
        self.Button_Power.setSizePolicy(sizePolicy)
        self.Button_Power.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Power.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Power.setFont(font)
        self.Button_Power.setMouseTracking(True)
        self.Button_Power.setTabletTracking(True)
        self.Button_Power.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Power.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Power_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_Power.setIconSize(QtCore.QSize(105, 105))
        self.Button_Power.setCheckable(False)
        self.Button_Power.setChecked(False)
        self.Button_Power.setFlat(True)
        self.Button_Power.setObjectName("Button_Power")
        self.Buttons_Container.addWidget(self.Button_Power, 1, 4, 1, 1)
        self.Button_Comma = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_Comma.clicked.connect(self.Button_Comma_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Comma.sizePolicy().hasHeightForWidth())
        self.Button_Comma.setSizePolicy(sizePolicy)
        self.Button_Comma.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Comma.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Comma.setFont(font)
        self.Button_Comma.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Comma.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Comma_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_Comma.setIconSize(QtCore.QSize(105, 105))
        self.Button_Comma.setFlat(True)
        self.Button_Comma.setObjectName("Button_Comma")
        self.Buttons_Container.addWidget(self.Button_Comma, 3, 2, 1, 1)
        self.Button_Equal = QtWidgets.QPushButton(self.ButtonsGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Equal.sizePolicy().hasHeightForWidth())
        self.Button_Equal.setSizePolicy(sizePolicy)
        self.Button_Equal.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Equal.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Equal.setFont(font)
        self.Button_Equal.setMouseTracking(True)
        self.Button_Equal.setTabletTracking(True)
        self.Button_Equal.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Equal.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Equal_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid #333333;\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #0094C6;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"color: black;\n"
"    font-color: black;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #FFFFFF;\n"
"border-bottom: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_Equal.setIconSize(QtCore.QSize(105, 105))
        self.Button_Equal.setCheckable(False)
        self.Button_Equal.setChecked(False)
        self.Button_Equal.setFlat(True)
        self.Button_Equal.setObjectName("Button_Equal")
        self.Buttons_Container.addWidget(self.Button_Equal, 3, 4, 1, 1)
        self.Button_3 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_3.clicked.connect(self.Button_3_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3.sizePolicy().hasHeightForWidth())
        self.Button_3.setSizePolicy(sizePolicy)
        self.Button_3.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_3.setMaximumSize(QtCore.QSize(330, 345))
        self.Button_3.setSizeIncrement(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_3.setFont(font)
        self.Button_3.setMouseTracking(True)
        self.Button_3.setTabletTracking(True)
        self.Button_3.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_3.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_3_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Button_3.setIconSize(QtCore.QSize(105, 105))
        self.Button_3.setCheckable(False)
        self.Button_3.setChecked(False)
        self.Button_3.setFlat(True)
        self.Button_3.setObjectName("Button_3")
        self.Buttons_Container.addWidget(self.Button_3, 0, 2, 1, 1)
        self.Button_9 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_9.clicked.connect(self.Button_9_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_9.sizePolicy().hasHeightForWidth())
        self.Button_9.setSizePolicy(sizePolicy)
        self.Button_9.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_9.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_9.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_9_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_9.setIconSize(QtCore.QSize(105, 105))
        self.Button_9.setFlat(True)
        self.Button_9.setObjectName("Button_9")
        self.Buttons_Container.addWidget(self.Button_9, 2, 2, 1, 1)
        self.Button_0 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_0.clicked.connect(self.Button_0_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_0.sizePolicy().hasHeightForWidth())
        self.Button_0.setSizePolicy(sizePolicy)
        self.Button_0.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_0.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_0.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_0_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_0.setIconSize(QtCore.QSize(105, 105))
        self.Button_0.setFlat(True)
        self.Button_0.setObjectName("Button_0")
        self.Buttons_Container.addWidget(self.Button_0, 3, 1, 1, 1)
        self.Button_8 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_8.clicked.connect(self.Button_8_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_8.sizePolicy().hasHeightForWidth())
        self.Button_8.setSizePolicy(sizePolicy)
        self.Button_8.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_8.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_8.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_8_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_8.setIconSize(QtCore.QSize(105, 105))
        self.Button_8.setFlat(True)
        self.Button_8.setObjectName("Button_8")
        self.Buttons_Container.addWidget(self.Button_8, 2, 1, 1, 1)
        self.Button_7 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_7.clicked.connect(self.Button_7_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_7.sizePolicy().hasHeightForWidth())
        self.Button_7.setSizePolicy(sizePolicy)
        self.Button_7.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_7.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_7.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_7_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_7.setIconSize(QtCore.QSize(105, 105))
        self.Button_7.setFlat(True)
        self.Button_7.setObjectName("Button_7")
        self.Buttons_Container.addWidget(self.Button_7, 2, 0, 1, 1)
        self.Button_Divide = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_Divide.clicked.connect(self.Button_Divide_Click)


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Divide.sizePolicy().hasHeightForWidth())
        self.Button_Divide.setSizePolicy(sizePolicy)
        self.Button_Divide.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Divide.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Divide.setFont(font)
        self.Button_Divide.setMouseTracking(True)
        self.Button_Divide.setTabletTracking(True)
        self.Button_Divide.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Divide.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Divide_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"    color: #0094C6;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Button_Divide.setIconSize(QtCore.QSize(105, 105))
        self.Button_Divide.setCheckable(False)
        self.Button_Divide.setChecked(False)
        self.Button_Divide.setFlat(True)
        self.Button_Divide.setObjectName("Button_Divide")
        self.Buttons_Container.addWidget(self.Button_Divide, 0, 3, 1, 1)
        self.Button_2 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_2.clicked.connect(self.Button_2_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2.sizePolicy().hasHeightForWidth())
        self.Button_2.setSizePolicy(sizePolicy)
        self.Button_2.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_2.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_2.setFont(font)
        self.Button_2.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_2.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_2_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Button_2.setIconSize(QtCore.QSize(105, 105))
        self.Button_2.setFlat(True)
        self.Button_2.setObjectName("Button_2")
        self.Buttons_Container.addWidget(self.Button_2, 0, 1, 1, 1)
        self.Button_Root = QtWidgets.QPushButton(self.ButtonsGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Root.sizePolicy().hasHeightForWidth())
        self.Button_Root.setSizePolicy(sizePolicy)
        self.Button_Root.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Root.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Root.setFont(font)
        self.Button_Root.setMouseTracking(True)
        self.Button_Root.setTabletTracking(True)
        self.Button_Root.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Root.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Root_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.Button_Root.setIconSize(QtCore.QSize(105, 105))
        self.Button_Root.setCheckable(False)
        self.Button_Root.setChecked(False)
        self.Button_Root.setFlat(True)
        self.Button_Root.setObjectName("Button_Root")
        self.Buttons_Container.addWidget(self.Button_Root, 0, 4, 1, 1)
        self.Button_Multiply = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_Multiply.clicked.connect(self.Button_Multiply_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Multiply.sizePolicy().hasHeightForWidth())
        self.Button_Multiply.setSizePolicy(sizePolicy)
        self.Button_Multiply.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Multiply.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Multiply.setFont(font)
        self.Button_Multiply.setMouseTracking(True)
        self.Button_Multiply.setTabletTracking(True)
        self.Button_Multiply.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Multiply.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Multiply_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #0094C6;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_Multiply.setIconSize(QtCore.QSize(105, 105))
        self.Button_Multiply.setCheckable(False)
        self.Button_Multiply.setChecked(False)
        self.Button_Multiply.setFlat(True)
        self.Button_Multiply.setObjectName("Button_Multiply")
        self.Buttons_Container.addWidget(self.Button_Multiply, 1, 3, 1, 1)
        self.Button_Factorial = QtWidgets.QPushButton(self.ButtonsGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Factorial.sizePolicy().hasHeightForWidth())
        self.Button_Factorial.setSizePolicy(sizePolicy)
        self.Button_Factorial.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Factorial.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Factorial.setFont(font)
        self.Button_Factorial.setMouseTracking(True)
        self.Button_Factorial.setTabletTracking(True)
        self.Button_Factorial.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Factorial.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Factorial_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_Factorial.setIconSize(QtCore.QSize(105, 105))
        self.Button_Factorial.setCheckable(False)
        self.Button_Factorial.setChecked(False)
        self.Button_Factorial.setFlat(True)
        self.Button_Factorial.setObjectName("Button_Factorial")
        self.Buttons_Container.addWidget(self.Button_Factorial, 2, 4, 1, 1)
        self.Button_5 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_5.clicked.connect(self.Button_5_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_5.sizePolicy().hasHeightForWidth())
        self.Button_5.setSizePolicy(sizePolicy)
        self.Button_5.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_5.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_5.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_5_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_5.setIconSize(QtCore.QSize(105, 105))
        self.Button_5.setFlat(True)
        self.Button_5.setObjectName("Button_5")
        self.Buttons_Container.addWidget(self.Button_5, 1, 1, 1, 1)
        self.Button_Sign = QtWidgets.QPushButton(self.ButtonsGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Sign.sizePolicy().hasHeightForWidth())
        self.Button_Sign.setSizePolicy(sizePolicy)
        self.Button_Sign.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Sign.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Sign.setFont(font)
        self.Button_Sign.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Sign.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Sign_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_Sign.setIconSize(QtCore.QSize(105, 105))
        self.Button_Sign.setFlat(True)
        self.Button_Sign.setObjectName("Button_Sign")
        self.Buttons_Container.addWidget(self.Button_Sign, 3, 0, 1, 1)
        self.Button_Plus = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_Plus.clicked.connect(self.Button_Plus_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Plus.sizePolicy().hasHeightForWidth())
        self.Button_Plus.setSizePolicy(sizePolicy)
        self.Button_Plus.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Plus.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Plus.setFont(font)
        self.Button_Plus.setMouseTracking(True)
        self.Button_Plus.setTabletTracking(True)
        self.Button_Plus.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Plus.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Plus_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #0094C6;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_Plus.setIconSize(QtCore.QSize(105, 105))
        self.Button_Plus.setCheckable(False)
        self.Button_Plus.setChecked(False)
        self.Button_Plus.setFlat(True)
        self.Button_Plus.setObjectName("Button_Plus")
        self.Buttons_Container.addWidget(self.Button_Plus, 2, 3, 1, 1)
        self.Button_4 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_4.clicked.connect(self.Button_4_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_4.sizePolicy().hasHeightForWidth())
        self.Button_4.setSizePolicy(sizePolicy)
        self.Button_4.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_4.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_4.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_4_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_4.setIconSize(QtCore.QSize(105, 105))
        self.Button_4.setFlat(True)
        self.Button_4.setObjectName("Button_4")
        self.Buttons_Container.addWidget(self.Button_4, 1, 0, 1, 1)
        self.Button_Minus = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_Minus.clicked.connect(self.Button_Minus_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Minus.sizePolicy().hasHeightForWidth())
        self.Button_Minus.setSizePolicy(sizePolicy)
        self.Button_Minus.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_Minus.setMaximumSize(QtCore.QSize(330, 345))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        self.Button_Minus.setFont(font)
        self.Button_Minus.setMouseTracking(True)
        self.Button_Minus.setTabletTracking(True)
        self.Button_Minus.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Minus.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Minus_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #0094C6;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.Button_Minus.setIconSize(QtCore.QSize(105, 105))
        self.Button_Minus.setCheckable(False)
        self.Button_Minus.setChecked(False)
        self.Button_Minus.setFlat(True)
        self.Button_Minus.setObjectName("Button_Minus")
        self.Buttons_Container.addWidget(self.Button_Minus, 3, 3, 1, 1)
        self.Button_1 = QtWidgets.QPushButton(self.ButtonsGrid)

        self.Button_1.clicked.connect(self.Button_1_Click)

        self.Button_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.Button_1.sizePolicy().hasHeightForWidth())
        self.Button_1.setSizePolicy(sizePolicy)
        self.Button_1.setMinimumSize(QtCore.QSize(110, 115))
        self.Button_1.setMaximumSize(QtCore.QSize(330, 345))
        self.Button_1.setSizeIncrement(QtCore.QSize(2, 2))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(50)
        font.setKerning(True)
        self.Button_1.setFont(font)
        self.Button_1.setMouseTracking(True)
        self.Button_1.setTabletTracking(True)
        self.Button_1.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_1.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_1_Pressed.png\');\n"
"background-origin: content-box;\n"
"    background-size: 50%;    \n"
"    background-position: center;\n"
"background-repeat: no-repeat;\n"
"}I*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"  font-size: 50%;\n"
"  text-align: justify;\n"
"\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.Button_1.setIconSize(QtCore.QSize(105, 105))
        self.Button_1.setCheckable(False)
        self.Button_1.setFlat(True)
        self.Button_1.setObjectName("Button_1")
        self.Buttons_Container.addWidget(self.Button_1, 0, 0, 1, 1)
        self.Buttons_Container.setColumnStretch(0, 1)
        self.Buttons_Container.setColumnStretch(1, 1)
        self.Buttons_Container.setColumnStretch(2, 1)
        self.Buttons_Container.setColumnStretch(3, 1)
        self.Buttons_Container.setColumnStretch(4, 1)
        self.Buttons_Container.setRowStretch(0, 1)
        self.Buttons_Container.setRowStretch(1, 1)
        self.Buttons_Container.setRowStretch(2, 1)
        self.Buttons_Container.setRowStretch(3, 1)
        self.Main_Container.addWidget(self.ButtonsGrid, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Display = QtWidgets.QLineEdit(self.Background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Display.sizePolicy().hasHeightForWidth())
        self.Display.setSizePolicy(sizePolicy)
        self.Display.setMinimumSize(QtCore.QSize(0, 100))
        self.Display.setMaximumSize(QtCore.QSize(1920, 150))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(35)
        self.Display.setFont(font)
        self.Display.setStyleSheet("QLineEdit{\n"
"    /*border: 2px solid rgb(37, 39, 48);*/\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"    /*border-radius: 20px;*/\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    /*background-color: rgb(34, 36, 44);*/\n"
"    background-color: black\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*QLineEdit{\n"
"    background-color:rgb(202, 255, 227);\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    selection-background-color: darkgray;\n"
"    font-size: 16px;}\n"
"QLineEdit:focus { \n"
"    background-color:rgb(192, 192, 255);\n"
"}*/")
        self.Display.setFrame(True)
        self.Display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Display.setClearButtonEnabled(False)
        self.Display.setObjectName("Display")
        self.verticalLayout.addWidget(self.Display)
        self.Main_Container.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.BackSpace = QtWidgets.QPushButton(self.Background)

        self.BackSpace.clicked.connect(self.Button_Backspace_Click)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackSpace.sizePolicy().hasHeightForWidth())
        self.BackSpace.setSizePolicy(sizePolicy)
        self.BackSpace.setMinimumSize(QtCore.QSize(100, 100))
        self.BackSpace.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.BackSpace.setFont(font)
        self.BackSpace.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BackSpace.setStyleSheet("/*QPushButton {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Root.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(\'C:/Users/dimon/Documents/IVS 2/Buttons/NumButton_Root_Pressed.png\');\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}*/\n"
"\n"
"QPushButton{\n"
"    border-bottom: 2px solid rgb(0, 148, 198);\n"
"    border-left: 1rem solid rgb(0, 0, 0);\n"
"    border-top: none;\n"
"    border-right: none;\n"
"border-bottom-left-radius: 8px 8px;\n"
"border-bottom-right-radius: 8px 8px;\n"
"width: 5px;\n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #333333;\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   \n"
"font-family: Bahnschrift;\n"
"    color: #FFF;\n"
"   padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: #444444;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.BackSpace.setIconSize(QtCore.QSize(20, 20))
        self.BackSpace.setObjectName("BackSpace")
        self.Main_Container.addWidget(self.BackSpace, 0, 1, 1, 1)
        self.Main_Container.setColumnStretch(0, 1)
        self.Main_Container.setRowStretch(0, 1)
        self.gridLayout_2.addLayout(self.Main_Container, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.Background, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_Power.setText(_translate("MainWindow", "a^"))
        self.Button_Comma.setText(_translate("MainWindow", ","))
        self.Button_Equal.setText(_translate("MainWindow", "="))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_Divide.setText(_translate("MainWindow", "÷"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_Root.setText(_translate("MainWindow", "√"))
        self.Button_Multiply.setText(_translate("MainWindow", "×"))
        self.Button_Factorial.setText(_translate("MainWindow", "!"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_Sign.setText(_translate("MainWindow", "±"))
        self.Button_Plus.setText(_translate("MainWindow", "+"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_Minus.setText(_translate("MainWindow", "-"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Display.setText(_translate("MainWindow", ""))
        self.BackSpace.setText(_translate("MainWindow", "⌫"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

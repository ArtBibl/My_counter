# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'СurrentСosts.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

import main_window
from payment_in_tab import WindowNewCustomer

from new_division import NewDivision
from del_division import DelDivision
from request_base import Request


class CurrentPaymentWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_del_div = DelDivision(self)
        self.window_new_div = NewDivision(self)
        self.window_new_customer_in_tab = WindowNewCustomer(self)

        self.tab = None
        self.setObjectName("CurrentPayment")
        self.setWindowTitle("Щомісячні витрати")
        # self.resize(850, 530)
        self.setFixedSize(850, 530)

        """main layout"""
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(650, 340, 180, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tab_widgets()
        self.layout_main_button()
        self.right_top_layout()

    def layout_main_button(self):
        """main buttons"""
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        """new division"""
        self.newdivision = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.newdivision.setObjectName("newdivision")
        self.verticalLayout.addWidget(self.newdivision)
        self.newdivision.setText("Створити новий розділ витрат")
        self.newdivision.clicked.connect(self.new_division)
        """delete division"""
        self.del_div_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.del_div_button.setObjectName("del_div_button")
        self.verticalLayout.addWidget(self.del_div_button)
        self.del_div_button.setText("Видалити розділ")
        self.del_div_button.clicked.connect(self.del_division)
        """close window"""
        self.closebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.closebutton.setObjectName("closebutton")
        self.verticalLayout.addWidget(self.closebutton)
        self.closebutton.setText("Закрити вікно")
        self.closebutton.clicked.connect(self.close)
        """exit from program"""
        self.close_program_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.close_program_button.setObjectName("close_program_button")
        self.verticalLayout.addWidget(self.close_program_button)
        self.close_program_button.setText("Вихід з програми")
        self.close_program_button.clicked.connect(main_window.MainWindow.push_button_exit)

    def tab_widgets(self):
        """Tab widget - division. Example '122' or 'Other'."""
        self.tabWidget.clear()
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 610, 500))
        self.tabWidget.setObjectName("tabWidget")
        sql_req = "SELECT * FROM system ORDER BY div"
        request = Request()
        data = request.show_base(sql_req)
        for id_div in data:
            # print(id_div[0])
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName(f"{id_div[1]}")

            self.refresh_but = QtWidgets.QPushButton(self.tab)
            self.refresh_but.setGeometry(QtCore.QRect(480, 410, 100, 30))
            self.refresh_but.setObjectName("refresh_but")
            self.refresh_but.setText("Оновити")
            self.refresh_but.clicked.connect(self.refresh)

            self.insert_but = QtWidgets.QPushButton(self.tab)
            self.insert_but.setGeometry(QtCore.QRect(370, 410, 100, 30))
            self.insert_but.setObjectName("insert_but")
            self.insert_but.setText("Внести зміни")

            self.del_but = QtWidgets.QPushButton(self.tab)
            self.del_but.setGeometry(QtCore.QRect(260, 410, 100, 30))
            self.del_but.setObjectName("del_but")
            self.del_but.setText("Видалити платіж")

            self.add_but = QtWidgets.QPushButton(self.tab)
            self.add_but.setGeometry(QtCore.QRect(150, 410, 100, 30))
            self.add_but.setObjectName("add_but")
            self.add_but.setText("Додати платіж")
            self.name_div = f"{id_div[1]}"
            self.add_but.clicked.connect(self.add_payment)

            self.dateEdit = QtWidgets.QDateEdit(self.tab)  # calendar
            self.dateEdit.setGeometry(QtCore.QRect(50, 410, 90, 30))
            self.dateEdit.setObjectName("calendar_dateEdit")
            self.dateEdit.setDate(QDate.currentDate())

            self.groupBox = QtWidgets.QGroupBox(self.tab)
            self.groupBox.setGeometry(QtCore.QRect(40, 30, 540, 360))
            self.groupBox.setObjectName("groupBox")
            self.groupBox.setTitle("Розрахунок поточних платежів:")
            """Full name of division"""
            self.label_full_name_div = QtWidgets.QLabel(self.groupBox)
            self.label_full_name_div.setGeometry(QtCore.QRect(60, 25, 250, 15))
            self.label_full_name_div.setAlignment(QtCore.Qt.AlignLeft)
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(True)
            self.label_full_name_div.setFont(font)
            self.label_full_name_div.setObjectName("full_name_div")
            self.label_full_name_div.setText(f"{id_div[2]}")

            self.gridLayout_tab = QtWidgets.QWidget(self.groupBox)
            self.gridLayout_tab.setGeometry(QtCore.QRect(10, 50, 520, 300))  # size layout
            self.gridLayout_tab.setObjectName("gridLayout_tab")

            self.gridLayout = QtWidgets.QGridLayout(self.gridLayout_tab)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("gridLayout")

            """ head labels into tabs for widgets """
            self.write_header_for_widgets("name_customer", "Постачальник:", 0, 0, 1, 1)
            self.write_header_for_widgets("price", "Ціна, грн:", 0, 1, 1, 1)
            self.write_header_for_widgets("counter_old", "Старі показники:", 0, 2, 1, 1)
            self.write_header_for_widgets("counter_new", "Нові показники:", 0, 3, 1, 1)
            self.write_header_for_widgets("total", "Сума до сплати:", 0, 4, 1, 1)
            self.write_header_for_widgets("button", " ", 0, 5, 1, 1)

            """ empty string (--------) """
            for i in range(6):
                self.write_header_for_widgets("space", "-------------------", 1, i, 1, 1)

            """ string from db"""
            sys_widget_string = [(43, "water", True, True, True,),
                                 (53, "gas", True, True, True,), 
                                 (63, "internet", False, False, True,)]
            """ widget lines """
            self.label_customer = QtWidgets.QLabel(self.gridLayout_tab)
            self.label_customer.setAlignment(QtCore.Qt.AlignCenter)
            self.label_customer.setObjectName("label_customer")
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            self.gridLayout.addWidget(self.label_customer, 2, 0, 1, 1)
            self.label_customer.setFont(font)
            self.label_customer.setText("Вода та стоки")

            self.lineEdit_price = QtWidgets.QLineEdit(self.gridLayout_tab)
            self.lineEdit_price.setObjectName("lineEdit_price")
            self.lineEdit_price.setAlignment(QtCore.Qt.AlignRight)
            self.lineEdit_price.setText("0.0")
            self.gridLayout.addWidget(self.lineEdit_price, 2, 1, 1, 1)

            self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayout_tab)
            self.lineEdit_7.setObjectName("lineEdit_7")
            self.lineEdit_price.setAlignment(QtCore.Qt.AlignRight)
            self.gridLayout.addWidget(self.lineEdit_7, 2, 2, 1, 1)  # temporary label

            self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayout_tab)
            self.lineEdit_8.setObjectName("lineEdit_8")
            self.lineEdit_price.setAlignment(QtCore.Qt.AlignRight)
            self.lineEdit_7.setPlaceholderText("Кількість")
            self.gridLayout.addWidget(self.lineEdit_8, 2, 3, 1, 1)

            self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayout_tab)
            self.lineEdit_15.setObjectName("lineEdit_15")
            self.lineEdit_price.setAlignment(QtCore.Qt.AlignRight)
            self.gridLayout.addWidget(self.lineEdit_15, 2, 4, 1, 1)

            self.button_push_payment = QtWidgets.QPushButton(self.gridLayout_tab)

            self.button_push_payment.setObjectName("label_check")
            self.button_push_payment.setText("OK!")
            self.gridLayout.addWidget(self.button_push_payment, 2, 5, 1, 1)

            self.label_empty = QtWidgets.QLabel(self.gridLayout_tab)
            self.label_empty.setAlignment(QtCore.Qt.AlignCenter)
            self.label_empty.setObjectName("label_empty")
            self.label_empty.setText(" ")
            self.gridLayout.addWidget(self.label_empty, 3, 5, 1, 1)

            self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Expanding)
            self.gridLayout.addItem(self.spacerItem, 100, 1, 1, 1)

            # """ dynamic button """
            # self.button_close = QtWidgets.QPushButton(self.tab)
            # self.button_close.setGeometry(QtCore.QRect(370, 410, 100, 30))
            # self.button_close.setObjectName(f"{id_div[2]}")
            # self.button_close.setText(f"{id_div[2]}")

            self.tabWidget.addTab(self.tab, "")
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), f"{id_div[1]}")

    def right_top_layout(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(660, 20, 160, 40))
        self.label.setObjectName("label")
        self.label.setText("Обов\'язкові поточні платежи")

        """   Line in top  """
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(650, 50, 180, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        """ right-top layout """
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(650, 70, 180, 170))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        for i in range(8):
            self.label_water = QtWidgets.QLabel(self.gridLayout_tab)
            self.label_water.setAlignment(QtCore.Qt.AlignLeft)
            self.label_water.setObjectName("label_water")
            self.label_water.setText("Інтернет: 160 грн.")
            self.verticalLayout_2.addWidget(self.label_water)

        # self.label_welcome_speach = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        # self.label_welcome_speach.setObjectName("label_welcome_speach")
        # self.label_welcome_speach.setText("Вода")
        # self.verticalLayout_2.addWidget(self.label_welcome_speach)
        #
        # self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        # self.label_4.setObjectName("label_4")
        # self.label_4.setText("Інтернет")
        # self.verticalLayout_2.addWidget(self.label_4)
        #
        # self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        # self.label_3.setText("Охорона")
        # self.label_3.setObjectName("label_3")
        # self.verticalLayout_2.addWidget(self.label_3)
        """ right-middle line """
        self.line_5 = QtWidgets.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(650, 220, 180, 70))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        """ middle layout """
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(650, 265, 180, 60))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label_balance = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_balance.setObjectName("label_stat")
        self.label_balance.setText("     Місячний баланс")
        self.verticalLayout_3.addWidget(self.label_balance)

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_stat")
        self.label_5.setText("Сплачено: 0 грн.")
        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Заборгованість: 2000 грн.")
        self.verticalLayout_3.addWidget(self.label_6)

        """  Line under main buttons"""
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(650, 330, 180, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        """  Bottom line   """
        self.line_bottom = QtWidgets.QFrame(self)
        self.line_bottom.setGeometry(QtCore.QRect(20, 500, 810, 25))
        self.line_bottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_bottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_bottom.setObjectName("line_bottom")

    def new_division(self):
        self.window_new_div.show()

    def del_division(self):
        self.window_del_div.show()

    def add_payment(self):
        self.window_new_customer_in_tab.show()

    def refresh(self):
        # self.tab_widgets()
        self.close()
        self.dialog_refresh = CurrentPaymentWindow()
        self.dialog_refresh.show()

    def write_header_for_widgets(self, name_label, text, p1, p2, p3, p4):
        label = QtWidgets.QLabel(self.gridLayout_tab)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName(f"{name_label}")
        label.setText(text)
        self.gridLayout.addWidget(label, p1, p2, p3, p4)

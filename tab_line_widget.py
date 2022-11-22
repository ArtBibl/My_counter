from PyQt5 import QtCore, QtGui, QtWidgets


class LineWidget:
    def __init__(self, customer=None, price=0, counter_old=None, counter_new=None, total=0):
        self.label_name_customer = customer
        self.price = price
        self.counter_old = counter_old
        self.counter_new = counter_new
        self.total = total

    def draw_line_customer_widget(self):
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
        self.gridLayout.addWidget(self.lineEdit_price, 2, 1, 1, 1)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayout_tab)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 2, 2, 1, 1)  # temporary label

        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayout_tab)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_7.setPlaceholderText("Кількість")
        self.gridLayout.addWidget(self.lineEdit_8, 2, 3, 1, 1)

        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayout_tab)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 2, 4, 1, 1)

        self.button_push_payment = QtWidgets.QPushButton(self.gridLayout_tab)
        self.button_push_payment.setAlignment(QtCore.Qt.AlignCenter)
        self.button_push_payment.setObjectName("label_check")
        self.button_push_payment.setText("OK!")
        self.gridLayout.addWidget(self.button_push_payment, 2, 5, 1, 1)

        # self.label_empty = QtWidgets.QLabel(self.gridLayout_tab)
        # self.label_empty.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_empty.setObjectName("label_empty")
        # self.label_empty.setText(" ")
        # self.gridLayout.addWidget(self.label_empty, 3, 5, 1, 1)

        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(self.spacerItem, 100, 1, 1, 1)

from PyQt5 import QtCore, QtGui, QtWidgets


class LineWidget(QtWidgets.QWidget):
    def __init__(self, gridLayout_tab, gridLayout, div=None, customer=None,
                 price=0, counter_old=None, total=0):
        super().__init__(gridLayout_tab)
        self.gridLayout_tab = gridLayout_tab
        self.gridLayout = gridLayout
        self.div = div
        self.label_name_customer = customer
        self.price = price
        self.counter_old = counter_old
        self.counter_new = None
        self.total = total

    def create_line_customer_widget(self, line):
        """ widget lines """
        if self.div:
            self.label_customer = QtWidgets.QLabel(self.gridLayout_tab)
            self.label_customer.setAlignment(QtCore.Qt.AlignLeft)
            self.label_customer.setAlignment(QtCore.Qt.AlignVCenter)
            self.label_customer.setObjectName("label_customer")
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            self.label_customer.setFont(font)
            self.label_customer.setText(self.label_name_customer)
            self.gridLayout.addWidget(self.label_customer, line, 0, 1, 1)

            self.line_edit_price = QtWidgets.QLineEdit(self.gridLayout_tab)
            self.line_edit_price.setObjectName("line_edit_price")
            self.line_edit_price.setAlignment(QtCore.Qt.AlignRight)
            self.line_edit_price.setText(f"{self.price}")
            # self.line_edit_price.editingFinished.connect(self.__check_old_price)
            self.line_edit_price.editingFinished.connect(self.count_total)
            self.gridLayout.addWidget(self.line_edit_price, line, 1, 1, 1)

            if self.counter_old:
                self.line_counter_old = QtWidgets.QLineEdit(self.gridLayout_tab)
                self.line_counter_old.setObjectName("line_counter_old")
                self.line_counter_old.setAlignment(QtCore.Qt.AlignRight)
                self.line_counter_old.setText(f"{self.counter_old}")
                self.gridLayout.addWidget(self.line_counter_old, line, 2, 1, 1)

                self.line_counter_new = QtWidgets.QLineEdit(self.gridLayout_tab)
                self.line_counter_new.setObjectName("line_counter_new")
                self.line_counter_new.setAlignment(QtCore.Qt.AlignRight)
                self.counter_new = self.counter_old
                self.line_counter_new.setText(f"{self.counter_new}")
                self.line_counter_new.setMaxLength(10)  # Length chars
                self.line_counter_new.editingFinished.connect(self.count_total)
                self.gridLayout.addWidget(self.line_counter_new, line, 3, 1, 1)

            self.line_total = QtWidgets.QLineEdit(self.gridLayout_tab)
            self.line_total.setObjectName("line_total")
            self.line_total.setAlignment(QtCore.Qt.AlignRight)
            self.line_total.setText(f"{self.count_total()}")
            self.gridLayout.addWidget(self.line_total, line, 4, 1, 1)

            self.button_push_payment = QtWidgets.QPushButton(self.gridLayout_tab)
            self.button_push_payment.setObjectName("button_push_payment")
            self.button_push_payment.setText("OK!")
            # self.button_push_payment.clicked.connect(self.__check_old_price)
            self.button_push_payment.clicked.connect(self.push_button_total)
            self.gridLayout.addWidget(self.button_push_payment, line, 5, 1, 1)

    def push_button_total(self):
        price = self.line_edit_price.text()
        total = self.line_total.text()
        if self.counter_old:
            old_count = self.line_counter_old.text()
            new_count = self.line_counter_new.text()
            print(f"{price} * ( {new_count} - {old_count} ) = {total}grn. From {self.div} div")
        else:
            print(f"{price}  =  {total}grn..  From {self.div} div")

    def count_total(self) -> str:
        self.__check_old_price()
        if self.counter_old:
            total = round((float(self.line_counter_new.text()) - float(self.line_counter_old.text()))
                          * float(self.line_edit_price.text()), 2)
        else:
            total = str(self.line_edit_price.text())
        self.line_total.setText(str(total))
        return total

    def __check_old_price(self):
        self.__check_for_float(self.line_edit_price.text())
        if f"{self.price}" != self.line_edit_price.text():
            self.price = self.line_edit_price.text()
            print("new price")

    def __check_for_float(self, var):
        try:
            var = float(var)
        except ValueError:
            print("not float")
            return self.line_edit_price.setText(f"{self.price}")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from request_base import Request
from statistic import StatisticWindow


def check_for_float(var):
    try:
        float(var)
    except ValueError:
        print("Exception: not float")
        return False
    return True


class LineWidget(QtWidgets.QWidget):
    def __init__(self, gridLayout_tab, gridLayout, calendar, div=None, customer=None,
                 price=0, counter_old=None, total=0):
        super().__init__(gridLayout_tab)
        self.gridLayout_tab = gridLayout_tab
        self.gridLayout = gridLayout
        self.calendar = calendar
        self.div = div
        self.customer = customer
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
            self.label_customer.setText(self.customer)
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
                self.line_counter_new.editingFinished.connect(self.__check_old_price)
                self.gridLayout.addWidget(self.line_counter_new, line, 3, 1, 1)

            self.line_total = QtWidgets.QLineEdit(self.gridLayout_tab)
            self.line_total.setObjectName("line_total")
            self.line_total.setStyleSheet("QLineEdit{background : #D9DDDC;}")
            self.line_total.setAlignment(QtCore.Qt.AlignRight)
            self.line_total.setText(f"{self.count_total()}")
            self.line_total.editingFinished.connect(self.__check_total_val)
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
        calendar = self.calendar.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        # print(calendar)
        if self.counter_old:
            old_count = self.line_counter_old.text()
            new_count = self.line_counter_new.text()
            print(f"{self.customer} -> {price} * ( {new_count} - {old_count} ) "
                  f"= {total}grn. From {self.div} div. Date:{calendar}")
            if total == "0.0" or total == "0":
                QMessageBox.warning(self, 'Увага!',
                                    "Відсутня сума до зарахування до бази даних!", QMessageBox.Ok, QMessageBox.Ok)
            else:
                print(self.customer, new_count, price, total, self.div)
                self.__add_payment_to_db(self.customer, new_count, price, total, self.div, calendar)
        else:
            print(f"{self.customer} -> {price}  =  {total}grn..  From {self.div} div")
            if total == "0.0" or total == "0":
                QMessageBox.warning(self, 'Увага!',
                                    "Відсутня сума до зарахування до бази даних!", QMessageBox.Ok, QMessageBox.Ok)
            else:
                new_count = "NULL"
                self.__add_payment_to_db(self.customer, new_count, price, total, self.div, calendar)

    def count_total(self) -> str:
        self.__check_old_price()
        if self.counter_old:
            total = round((float(self.line_counter_new.text()) - float(self.line_counter_old.text()))
                          * float(self.line_edit_price.text()), 2)
        else:
            total = str(self.line_edit_price.text())
        self.line_total.setText(str(total))
        return total

    def __add_payment_to_db(self, name_pay, counter, price, money, div_pay, date):
        request = Request()
        print(f"INSERT INTO payments (date, name_pay, counter, price, money, div_pay) "
              f"VALUES ('{date}', '{name_pay}({div_pay})', {counter}, {price}, -{money}, '{div_pay}')")
        sql_req = f"INSERT INTO payments (date, name_pay, counter, price, money, div_pay) VALUES " \
                  f"('{date}', " \
                  f"'{name_pay}({div_pay})', " \
                  f"{counter}, " \
                  f"{price}, " \
                  f"-{money}, " \
                  f"'{div_pay}')"
        request.execute_data(sql_req)
        text_message = f"\n Платіж: '{name_pay}({div_pay})' на суму: {money} грн. \n " \
                       f"було успішно записано до бази даних у розділ: '{div_pay}'\n"
        QMessageBox.information(self, 'Успішний запис витрат!', text_message, QMessageBox.Ok, QMessageBox.Ok)

    def __check_old_price(self):
        price = self.line_edit_price.text()
        if check_for_float(price) is not True:
            self.line_edit_price.setText(f"{self.price}")
        elif f"{self.price}" != price:
            request = Request()
            sql_req = f"UPDATE system SET first_price = {price} WHERE first_price = {self.price} and name_customer = '{self.customer}'"
            # print(f"UPDATE system SET first_price = {price} WHERE first_price = {self.price} and name_customer = '{self.customer}'")
            request.execute_data(sql_req)
            print(f"The data in the 'system' table has been overwritten. Old price {self.price} for new price {price}.")
            self.price = price

    def __check_total_val(self):
        print("check total line_edit")

        if self.line_total.text() == "":
            print("empty line")
            self.line_total.setText(f"{self.count_total()}")
            QMessageBox.warning(self, 'Увага!', 'Некоректна сума послуг!',
                                QMessageBox.Ok, QMessageBox.Ok)
        if not check_for_float(self.line_total.text()):
            print("not check_for_float(self.line_total.text())")
            self.line_total.setText(f"{self.count_total()}")
            QMessageBox.warning(self, 'Увага!', 'Некоректна сума послуг!',
                                QMessageBox.Ok, QMessageBox.Ok)

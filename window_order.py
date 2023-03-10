from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

from const import *
from request_base import Request


class Order(QWidget):
    def __init__(self, regular_pay_window=None, div=None, date=None):
        super().__init__()
        self.div = div
        self.calendar = date
        self.regular_pay_window = regular_pay_window
        self.setObjectName("OrderPayment")
        self.setWindowTitle("Щомісячні витрати")
        # self.resize(850, 530)
        self.setFixedSize(FIX_SIZE_X, FIX_SIZE_Y)

        self.vBox = QVBoxLayout()

        self.calendar = self.calendar.dateTime().toString("yyyy-MM-dd")

        request = Request()
        query = f"SELECT name_customer FROM system " \
                f"WHERE div = '{self.div}' AND name_customer NOT NULL " \
                f"ORDER BY id;"
        self.data = request.show_base(query)
        header = ["Постачальник:", "Поч.показ.:", "Кін.показ.:", "Спожито:", "Тариф:", "Сума:"]

        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # not editable
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(len(self.data[0]))
        self.tableWidget.setColumnWidth(0, 105)
        self.tableWidget.setColumnWidth(1, 60)
        self.tableWidget.setColumnWidth(2, 150)
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setHorizontalHeaderLabels(header)

        row = -1
        for i in self.data:
            row += 1
            column = 0
            self.tableWidget.setRowHeight(row, ROW_HEIGHT)
            for x in i:
                if x is None:
                    self.tableWidget.setItem(row, column, QTableWidgetItem(""))
                else:
                    item = QTableWidgetItem(str(x))
                    self.tableWidget.setItem(row, column, QTableWidgetItem(item))
                column += 1

        self.vBox.addWidget(self.tableWidget)
        self.setLayout(self.vBox)
        """ All value """
        print(self.div, self.calendar, self.data)

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout
from pyqt5_plugins.examplebutton import QtWidgets
from request_base import Request


class StatSomeElse(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Stat_some_else")
        self.resize(500, 600)
        self.setWindowTitle("Статистика різних витрат")
        # self.setGeometry(500, 400, 500, 300)
        self.setFixedWidth(500)  # fixed size of window
        self.sql_req = "SELECT name_pay, money, date FROM payments"
        self.request = Request()
        self.data = self.request.show_base(self.sql_req)
        self.tables_stat_other()

    def tables_stat_other(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # not editable
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(len(self.data[0]))
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setHorizontalHeaderLabels(["Витрати:", "Сума:", "Дата:"])

        # self.tableWidget.setGeometry(QRect(0, 0, 800, 680))

        row = -1
        for i in self.data:
            row += 1
            column = 0
            for x in i:
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(x)))
                column += 1

        # self.tableWidget.resizeColumnsToContents()

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.refresh = QtWidgets.QPushButton("Оновити")
        hbox.addWidget(hbox.refresh)
        hbox.refresh.clicked.connect(self.button_refresh)

        hbox.cancelButton = QtWidgets.QPushButton("Закрити")
        hbox.addWidget(hbox.cancelButton)
        hbox.cancelButton.clicked.connect(self.cancel_button)

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.tableWidget)
        self.vBox.addLayout(hbox)
        self.setLayout(self.vBox)

    def button_refresh(self):
        self.update()
        self.repaint()
        print("Still doesn't work!!! :(")

    def cancel_button(self):
        self.close()

# if __name__ == '__main__':
#     import sys
#     App = QApplication(sys.argv)
#     window = StatSomeElse()
#     sys.exit(App.exec())

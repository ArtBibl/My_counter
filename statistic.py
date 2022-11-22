from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout
from pyqt5_plugins.examplebutton import QtWidgets
from request_base import Request


class StatisticWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("StatisticWindow")
        # self.resize(500, 600)
        self.setWindowTitle("Статистика різних витрат")
        self.setGeometry(0, 0, 500, 300)
        self.setFixedWidth(520)  # fixed size of window
        self.tableWidget = QTableWidget()
        self.create_table_stat()
        self.create_buttons()

        # self.tableWidget.resizeColumnsToContents()

    def create_table_stat(self):
        sql_req = "SELECT name_pay, money, date FROM payments ORDER BY date DESC"
        request = Request()
        data = request.show_base(sql_req)
        
        self.draw_table_stat(data, ["Витрати:", "Сума:", "Дата:"])
        
    def create_buttons(self):
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
        self.create_table_stat()

    def cancel_button(self):
        self.close()

    def draw_table_stat(self, data, header):
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # not editable
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setHorizontalHeaderLabels(header)
        # self.tableWidget.setGeometry(QRect(0, 0, 800, 680))
        # data = (['asda', -2, '23'], ['asda', 3, '23'])
        row = -1
        for i in data:
            if i[1] > 0:
                color_text = True
            else:
                color_text = False
            row += 1
            column = 0
            for x in i:
                if color_text and column == 1:
                    item = QTableWidgetItem(str(x))
                    item.setForeground(QBrush(QColor(0, 255, 0)))
                    self.tableWidget.setItem(row, column, QTableWidgetItem(item))
                elif color_text is False and column == 1:
                    item = QTableWidgetItem(str(x))
                    item.setForeground(QBrush(QColor(255, 0, 0)))
                    self.tableWidget.setItem(row, column, QTableWidgetItem(item))
                else:
                    item = QTableWidgetItem(str(x))
                    item.setForeground(QBrush(QColor(0, 0, 0)))
                    self.tableWidget.setItem(row, column, QTableWidgetItem(item))
                column += 1


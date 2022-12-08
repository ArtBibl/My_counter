
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout
from pyqt5_plugins.examplebutton import QtWidgets
from request_base import Request
from const import *


class StatisticWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.vBox = None
        self.setObjectName("StatisticWindow")
        self.setWindowTitle("Статистика різних витрат")
        self.setGeometry(SET_GEO_X1, SET_GEO_Y1, SET_GEO_X2, SET_GEO_Y2)
        # self.setFixedWidth(SET_FIX_WID)  # fixed size of window
        self.tableWidget = QTableWidget()
        self.create_table_stat()
        self.create_buttons()

        # self.tableWidget.resizeColumnsToContents()

    def create_table_stat(self):
        request = Request()
        data = request.show_base(STAT_SQL)
        
        self.draw_table_stat(data, STAT_HEADER)
        
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
        # data = (['asda', -2, '23'], ['asda', 3, '23'])  # for test
        # if data is None:
        #     data = ([None, None, None])
        row = -1
        for i in data:
            row += 1
            column = 0
            for x in i:
                if x is None:
                    self.tableWidget.setItem(row, column, QTableWidgetItem(""))
                elif i[1] > 0 and column == 1:
                    item = QTableWidgetItem(str(x))
                    item.setForeground(QBrush(QColor('Green')))
                    self.tableWidget.setItem(row, column, QTableWidgetItem(item))
                elif i[1] < 0 and column == 1:
                    item = QTableWidgetItem(str(x))
                    item.setForeground(QBrush(QColor('Red')))
                    self.tableWidget.setItem(row, column, QTableWidgetItem(item))
                else:
                    item = QTableWidgetItem(str(x))
                    item.setForeground(QBrush(QColor('Black')))
                    self.tableWidget.setItem(row, column, QTableWidgetItem(item))
                column += 1

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

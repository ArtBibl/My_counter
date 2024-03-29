# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'del_division.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QMessageBox

from request_base import Request
from const import *


class DelDivision(QWidget):
    def __init__(self, regular_pay_window=None):
        super().__init__()
        self.regular_pay_window = regular_pay_window
        self.setObjectName("del_division")
        self.setWindowTitle("Видалення розділу витрат")
        self.setFixedSize(SET_FIX_SIZE_X, SET_FIX_SIZE_Y)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 180, 340, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 30, 290, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Оберіть назву розділу для видалення")

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 80, 260, 50))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.short_name_div = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.short_name_div.setObjectName("lineEdit")
        self.short_name_div.setPlaceholderText("Скороченне ім\'я розділу")
        self.verticalLayout.addWidget(self.short_name_div)

        self.buttonBox.accepted.connect(self.accept_click)
        self.buttonBox.rejected.connect(self.close)

    @pyqtSlot()
    def accept_click(self):
        short_name = self.short_name_div.text()

        request = Request()
        sql_req = "SELECT div FROM system"
        data = request.show_base(sql_req)

        if short_name not in str(data):
            QMessageBox.critical(self, "Такий розділ не існує!",
                                 "Введіть назву розділу!", QMessageBox.Ok, QMessageBox.Ok)
            self.short_name_div.setText('')
        elif short_name != '':
            sql_req = "DELETE FROM system WHERE div = '" + short_name + "';"
            request = Request()
            request.execute_data(sql_req)
            QMessageBox.information(self, "Вітаю!", "Розділ було успішно видаленно!", QMessageBox.Ok, QMessageBox.Ok)
            self.short_name_div.setText('')
            self.close()
            if self.regular_pay_window is not None:
                self.regular_pay_window.tab_widgets()
        else:
            QMessageBox.critical(self, "Відсутнє скороченне ім'я розділу!",
                                 "Введіть скорочену назву розділу для видалення!", QMessageBox.Ok, QMessageBox.Ok)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

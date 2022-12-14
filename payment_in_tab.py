# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_division.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox, QCheckBox

from request_base import Request


class WindowNewCustomer(QWidget):
    def __init__(self, name_div):
        super().__init__()
        self.name_div = name_div
        print(self.name_div)
        self.setObjectName("new_pay")
        self.setWindowTitle("Новий розділ")
        self.setFixedSize(400, 260)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 180, 340, 90))
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
        self.label.setText("Введіть назву нового розділу")

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 70, 260, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.short_name_div = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.short_name_div.setObjectName("short_name_div")
        self.short_name_div.setPlaceholderText("Им\'я нового розділу")
        self.verticalLayout.addWidget(self.short_name_div)

        self.full_name_div = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.full_name_div.setObjectName("full_name_div")
        self.full_name_div.setPlaceholderText("Повна назва нового розділу")
        self.verticalLayout.addWidget(self.full_name_div)

        """ Checkbox for add counter """
        self.add_counter_checkbox = QCheckBox("Додати до розрахунку поля лічильника", self)
        self.verticalLayout.addWidget(self.add_counter_checkbox)

        """Button for close/accept"""
        self.buttonBox.accepted.connect(self.accept_click)
        self.buttonBox.rejected.connect(self.close)

    @pyqtSlot()
    def accept_click(self):
        short_name = self.short_name_div.text()
        full_name = self.full_name_div.text()

        request = Request()
        sql_req = "SELECT div FROM system"
        data = request.show_base(sql_req)

        if short_name in str(data):
            QMessageBox.critical(self, "Таке ім'я нового розділу вже існує!",
                                 "Введіть унікальну назву нового розділу!", QMessageBox.Ok, QMessageBox.Ok)
            self.short_name_div.setText('')
        elif short_name != '':
            if self.add_counter_checkbox.isChecked():
                self.sql_req = "INSERT INTO system (div, div_full_name) VALUES ('" + short_name + "', '" + full_name + "')"
            if self.add_counter_checkbox.isChecked() is not True:
                self.sql_req = "INSERT INTO system (div, div_full_name) VALUES ('" + short_name + "', '" + full_name + "')"
            self.request.execute_data(self.sql_req)
            QMessageBox.information(self, "Вітаю!", "Новий розділ успішно створенно!", QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.critical(self, "Відсутнє ім'я нового розділу!",
                                 "Введіть скорочену назву нового розділу!", QMessageBox.Ok, QMessageBox.Ok)

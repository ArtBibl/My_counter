# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'some_else.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QWidget
from request_base import Request


class SomeElse(QWidget):
    def __init__(self):
        super().__init__()
        self.sql_req = None
        self.setObjectName("Dialog")
        self.setFixedSize(420, 240)
        self.request = Request()
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 180, 340, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(38, 20, 290, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 330, 40))
        self.gridLayoutWidget.setObjectName("gridLayout_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.coast = QLineEdit(self)
        self.coast.setObjectName("coast")
        self.coast.setPlaceholderText("Сума витрат, грн..")
        self.gridLayout.addWidget(self.coast, 1, 1, 1, 1)
        self.name_payments = QLineEdit(self)
        self.name_payments.setObjectName("name_payments")
        self.name_payments.setPlaceholderText("Назва витрат")
        self.gridLayout.addWidget(self.name_payments, 1, 0, 1, 1)

        self.retranslate_ui(self)
        self.buttonBox.accepted.connect(self.push_payment)
        self.buttonBox.rejected.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Витрати"))
        self.label.setText(_translate("Dialog", "Ваші нерегулярні витрати:"))
        self.label_3.setText(_translate("Dialog", " Витрачена сума:"))
        self.label_2.setText(_translate("Dialog", " Призначення витрат:"))

    @pyqtSlot()
    def push_payment(self):
        textbox_value = self.name_payments.text()
        if textbox_value != '':
            try:
                coast = float(self.coast.text())
                text_message = textbox_value + ": " + str(coast) + "грн."
                QMessageBox.information(self, 'Успішний запис витрат!', text_message, QMessageBox.Ok, QMessageBox.Ok)
                self.sql_req = "INSERT INTO payments (name_pay, money, date) VALUES ('" + textbox_value + "', " + str(
                    coast) + ", datetime('now', 'localtime'))"
                self.request.execute_data(self.sql_req)
                self.name_payments.setText("")
            except ValueError:
                QMessageBox.critical(self, 'Некоректна сума!',
                                     'Спробуйте ще раз ввести суму..', QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Відсутнє призначення витрат!',
                                 'Спробуйте ще раз ввести призначення платежу..', QMessageBox.Ok, QMessageBox.Ok)
        self.coast.setText("")

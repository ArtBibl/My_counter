# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'some_else.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QDate, QTime
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QWidget
from request_base import Request


class UnregularPayments(QWidget):
    def __init__(self, stat_window=None):
        super().__init__()
        self.stat_window = stat_window
        self.setObjectName("Unreg_payments")
        self.setWindowTitle("Витрати")
        self.setFixedSize(420, 260)

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
        self.label.setText("Ваші нерегулярні витрати:")

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 330, 100))
        self.gridLayoutWidget.setObjectName("gridLayout_tab")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_welcome_speach")
        self.label_2.setText(" Призначення витрат:")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setText(" Витрачена сума:")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.coast = QLineEdit(self)
        self.coast.setObjectName("coast")
        self.coast.setFixedHeight(20)
        self.coast.setPlaceholderText("Сума витрат, грн..")
        self.gridLayout.addWidget(self.coast, 1, 1, 1, 1)

        self.name_payments = QLineEdit(self)
        self.name_payments.setObjectName("name_profit")
        self.name_payments.setFixedHeight(20)
        self.name_payments.setPlaceholderText("Назва витрат")
        self.gridLayout.addWidget(self.name_payments, 1, 0, 1, 1)

        self.label_calendar = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_calendar.setObjectName("label_3")
        self.label_calendar.setText(" Дата платежу:")
        self.gridLayout.addWidget(self.label_calendar, 2, 0, 1, 1)

        self.dateEdit = QtWidgets.QDateTimeEdit(self, calendarPopup=True)  # calendar
        # self.dateEdit.setGeometry(QtCore.QRect(50, 410, 90, 30))
        self.dateEdit.setFixedHeight(20)
        self.dateEdit.setObjectName("calendar_dateEdit")
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setTime(QTime.currentTime())
        self.dateEdit.setDisplayFormat('dd-MM-yyyy | hh:mm:ss')
        # print(self.calendar_edit.text().replace('.', '-'))
        self.gridLayout.addWidget(self.dateEdit, 3, 0, 1, 1)

        self.buttonBox.accepted.connect(self.push_payment)
        self.buttonBox.rejected.connect(self.close)

    @pyqtSlot()
    def push_payment(self):
        textbox_value = self.name_payments.text()
        date = self.dateEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        if textbox_value != '':
            try:
                coast = float(self.coast.text())
                coast = abs(coast)
                text_message = f"\n{textbox_value}: {coast} грн. \n" \
                               f"Дата: {date} \n"
                QMessageBox.information(self, 'Успішний запис витрат!', text_message, QMessageBox.Ok, QMessageBox.Ok)
                request = Request()
                sql_req = "INSERT INTO payments (name_pay, money, date) VALUES ('" + textbox_value + "', -" + str(
                    coast) + ", '" + date + "')"
                # sql_req = "INSERT INTO payments (name_pay, money, date) VALUES ('" + textbox_value + "', -" + str(
                #     coast) + ", datetime('now', 'localtime'))"
                request.execute_data(sql_req)
                self.name_payments.setText("")
                if self.stat_window is not None:
                    self.stat_window.button_refresh()
            except ValueError:
                QMessageBox.critical(self, 'Некоректна сума!',
                                     'Спробуйте ще раз ввести суму..', QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Відсутнє призначення витрат!',
                                 'Спробуйте ще раз ввести призначення платежу..', QMessageBox.Ok, QMessageBox.Ok)
        self.coast.setText("")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

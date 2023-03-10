from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QCheckBox, QDialog

from window_regular_payments import *
from request_base import Request


class WindowDelCustomer(QDialog):
    def __init__(self, parent=None, tab_widget=None):
        super().__init__(parent)
        self.tab = tab_widget
        self.customers_list = []
        request = Request()
        req_select_div = f"SELECT name_customer FROM system WHERE div='{self.tab}' AND name_customer NOT NULL"
        self.customer = request.show_base(req_select_div)
        self.setObjectName("del_customer")
        self.setWindowTitle("Видалити постачальника послуг")
        self.setFixedSize(400, 340)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 210, 340, 170))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 30, 330, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(f"  Оберіть постачальника посуг яких \nбажаєте "
                           f"видалити з розділу: '{self.tab}'")

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 90, 260, 180))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        print(self.customer)
        for customer in self.customer:
            check_box = QCheckBox(customer[0])
            check_box.setChecked(False)
            check_box.customer = customer[0]
            check_box.stateChanged.connect(self.on_clicked)
            self.verticalLayout.addWidget(check_box)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem)

        """Button for close/accept"""
        self.buttonBox.accepted.connect(self.__accept_click)
        self.buttonBox.rejected.connect(self.close)

    def on_clicked(self):
        check_box = self.sender()
        if check_box.isChecked():
            self.customers_list.append(check_box.customer)
        else:
            self.customers_list.remove(check_box.customer)

    @pyqtSlot()
    def __accept_click(self):
        if not self.customers_list:
            QMessageBox.warning(self, 'Увага!', 'Відсутній розділ для видалення!\n'
                                                'Виберіть розділ, який необхідно видалити!',
                                QMessageBox.Ok, QMessageBox.Ok)
        else:
            print(self.customers_list)
            for cust in self.customers_list:
                req = f"DELETE FROM system WHERE (div = '{self.tab}' AND name_customer = '{cust}')"
                print(req)
                request = Request()
                request.execute_data(req)
            self.close()

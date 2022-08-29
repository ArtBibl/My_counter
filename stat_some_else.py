
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from pyqt5_plugins.examplebutton import QtWidgets
from request_base import Request


class StatSomeElse(QWidget):
    def __init__(self):
        super().__init__()
        self.buttonBox = None
        self.setObjectName("Dialog")
        self.resize(365, 400)
        self.setWindowTitle("Statistic by 'Other' table")
        # self.setGeometry(500, 400, 500, 300)
        self.data = Request.show_other()
        self.tables()

    def tables(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # not editable
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(len(self.data[0]))
        self.tableWidget.setColumnWidth(0, 200)

        row = -1
        for i in self.data:
            row += 1
            column = 0
            for x in i:
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(x)))
                column += 1

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.tableWidget)
        self.setLayout(self.vBox)

# if __name__ == '__main__':
#     import sys
#     App = QApplication(sys.argv)
#     window = StatSomeElse()
#     sys.exit(App.exec())


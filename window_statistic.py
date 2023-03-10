from datetime import datetime

import pyqtgraph as pg
import csv

from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog, \
    QLineEdit

from pyqt5_plugins.examplebutton import QtWidgets
from request_base import Request
from const import *
from sort_by_date import sort_by_date


class StatisticWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("StatisticWindow")
        self.setWindowTitle("Статистика витрат")
        self.setGeometry(SET_GEO_X1, SET_GEO_Y1, SET_GEO_X2, SET_GEO_Y2)
        # self.setFixedWidth(SET_FIX_WID)  # fixed size of window

        request = Request()
        self.data = request.show_base(STAT_SQL)

        self.h_main_layout = QHBoxLayout()
        self.vBox = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.graphWidget = pg.plot(title="Витрати за поточний час")

        self.create_filter_buttons()
        self.create_table_stat()
        self.vBox.addWidget(self.tableWidget)
        self.create_bottom_buttons()

        self.setLayout(self.vBox)

        self.h_main_layout.addLayout(self.vBox)
        self.h_main_layout.addWidget(self.graphWidget)

    def create_table_stat(self):

        if not self.data:
            self.data = [(None, None, None)]

        self.draw_table_stat(self.data, STAT_HEADER)

        print(f"List from db: {self.data}")
        self.draw_graph(self.data)

    def draw_graph(self, data):
        """graph"""
        if data == [(None, None, None)]:
            print(f"Data base not detected. Data base was created. Name db: {DATA_BASE}")
            data = [(0, '')]
        else:
            data = sort_by_date(data)
        print(f"List for graph: {data}")
        """ draw value in graph"""
        date_graph = [i for i in range(0, len(data))]

        money_graph = [i[0] for i in data]
        print(f"Days scale: {date_graph}")

        self.graphWidget.clear()
        self.graphWidget.setTitle('<h3>Баланс витрат за поточний проміжок часу</h3>')
        self.graphWidget.setBackground('w')
        self.graphWidget.addLegend()
        self.graphWidget.setLabel('left', 'Сума (грн.)')
        self.graphWidget.setLabel('bottom', 'Календарний день')
        self.graphWidget.showGrid(x=None, y=True, alpha=None)
        # self.graphWidget.addLine(x=0, y=200)

        bg = pg.BarGraphItem(x=date_graph, height=money_graph, width=0.5, brush='g')

        self.graphWidget.addItem(bg)

        """ get middle value of all payments"""
        middle_money = round((sum(i[0] for i in data)) / len(data), 2)
        self.graphWidget.plot([-1, len(data)], [middle_money, middle_money], pen='red', symbol='o', symbolPen='g',
                              symbolBrush=0.2,
                              name=f'Середній баланс за день: {middle_money}грн.', symbolSize=0)

        self.setLayout(self.h_main_layout)

    def create_bottom_buttons(self):
        hbox = QHBoxLayout()

        hbox.import_file = QtWidgets.QPushButton("Імпорт .csv")
        hbox.addWidget(hbox.import_file)
        hbox.import_file.clicked.connect(self.import_file)

        hbox.addStretch()

        hbox.del_row = QtWidgets.QPushButton("Видалити")
        hbox.addWidget(hbox.del_row)
        hbox.del_row.clicked.connect(self.delete_row)

        hbox.refresh = QtWidgets.QPushButton("Оновити")
        hbox.addWidget(hbox.refresh)
        hbox.refresh.clicked.connect(self.button_refresh)

        hbox.cancelButton = QtWidgets.QPushButton("Закрити")
        hbox.addWidget(hbox.cancelButton)
        hbox.cancelButton.clicked.connect(self.cancel_button)

        self.vBox.addLayout(hbox)

    def create_filter_buttons(self):
        self.first_date = self.data[-1][2].rsplit(' ', -1)[0]
        self.last_date = QDate.currentDate()
        print("First date for filters:", self.first_date)

        hbox = QHBoxLayout()

        hbox.label_date_from = QtWidgets.QLabel(self)
        hbox.label_date_from.setAlignment(QtCore.Qt.AlignCenter)
        hbox.label_date_from.setText("Пошук від:")
        hbox.addWidget(hbox.label_date_from)

        self.edit_date_from = QtWidgets.QDateEdit(self)  # calendar
        self.edit_date_from.setGeometry(QtCore.QRect(50, 410, 90, 30))
        self.edit_date_from.setObjectName("calendar_dateEdit")
        self.edit_date_from.setDate(QDate.fromString(self.first_date, "yyyy-MM-dd"))
        self.edit_date_from.editingFinished.connect(self.__get_new_data_by_filter)
        hbox.addWidget(self.edit_date_from)

        hbox.label_date_to = QtWidgets.QLabel(self)
        hbox.label_date_to.setAlignment(QtCore.Qt.AlignCenter)
        hbox.label_date_to.setText(" по:")
        hbox.addWidget(hbox.label_date_to)

        self.edit_date_to = QtWidgets.QDateEdit(self)  # calendar
        self.edit_date_to.setGeometry(QtCore.QRect(50, 410, 90, 30))
        self.edit_date_to.setObjectName("calendar_dateEdit")
        self.edit_date_to.setDate(self.last_date)
        self.edit_date_to.editingFinished.connect(self.__get_new_data_by_filter)
        hbox.addWidget(self.edit_date_to)

        hbox.addStretch()  # spacer

        self.search_name = QLineEdit(self)
        # hbox.edit_date_to.setGeometry(QtCore.QRect(50, 410, 90, 30))
        self.search_name.setObjectName("search")
        self.search_name.setPlaceholderText("Текст для пошуку")
        self.search_name.editingFinished.connect(self.__get_new_data_by_filter)
        hbox.addWidget(self.search_name)

        self.vBox.addLayout(hbox)

    def __get_new_data_by_filter(self):
        first_date = self.edit_date_from.date()
        last_date = self.edit_date_to.date()
        first_date = first_date.toPyDate()
        last_date = last_date.toPyDate()
        search_text = self.search_name.text()

        req = f"SELECT name_pay, money, date FROM payments WHERE DATE(date) BETWEEN '{first_date}' AND '{last_date}' AND name_pay LIKE '%{search_text}%' AND money NOT NULL ORDER BY date DESC"
        request = Request()
        self.data = request.show_base(req)
        print(f"SELECT name_pay, money, date FROM payments WHERE DATE(date) BETWEEN '{first_date}' AND '{last_date}' AND name_pay LIKE '%{search_text}%' AND money NOT NULL ORDER BY date DESC")
        self.create_table_stat()

    def draw_table_stat(self, data, header):
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # not editable
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setColumnWidth(0, 105)
        self.tableWidget.setColumnWidth(1, 60)
        self.tableWidget.setColumnWidth(2, 150)
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setHorizontalHeaderLabels(header)

        row = -1
        for i in data:
            row += 1
            column = 0
            self.tableWidget.setRowHeight(row, ROW_HEIGHT)
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

    def import_file(self):
        today = datetime.today()
        date_file_name = today.strftime("%Y-%m-%d")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Імпорт таблиці в файл у CSV форматі",
                                                   f"My_payments{date_file_name}.csv",
                                                   "Table Files (*.csv);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w', encoding='utf8', newline='') as f:
                writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                writer.writerow(STAT_HEADER)
                for row in self.data:
                    writer.writerow(row)

            label_link = QtWidgets.QLabel(self)
            label_link.setText(
                f'<a href="https://products.aspose.app/cells/editor/edit?FolderName=6c973635-a08e-4603-8ad8-a136d0f912b2&'
                f'FileName=My_payments{date_file_name}.csv&Uid=ffe824aa-38ff-40ad-b397-965bbf954566.xlsx"> '
                f'Відкрити файл в браузері </a>')
            label_link.setOpenExternalLinks(True)

            QMessageBox.information(self, 'Успішний запис витрат! Для відкривання .CSV використовуйте посилання:',
                                    label_link.text(), QMessageBox.Ok, QMessageBox.Ok)

    def button_refresh(self):
        request = Request()
        self.data = request.show_base(STAT_SQL)
        self.create_table_stat()

    def cancel_button(self):
        self.close()

    def delete_row(self):
        data = self.data
        print(f"Data list for del: {data}")
        current_row = self.tableWidget.currentRow()
        if self.tableWidget.currentItem() is not None:
            data = data[current_row]
            button = QMessageBox.question(
                self, 'Увага!',
                f"Ви впевнені що бажаєте видалити платіж:\n"
                f"\nпризначення платежу: {data[0]}\n"
                f"на суму: {data[1]}грн.\n"
                f"платіж від: {data[2]}\n"
                f"\nВи переконані? Дані буду видалені назавжди!\n",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if button == QMessageBox.StandardButton.Yes:
                self.tableWidget.removeRow(current_row)
                request = Request()
                sql_req = f"DELETE FROM payments WHERE " \
                          f"name_pay = '{data[0]}' AND " \
                          f"money = {data[1]} AND " \
                          f"date = '{data[2]}'"
                request.execute_data(sql_req)
                self.button_refresh()
        else:
            QMessageBox.warning(self, 'Увага!',
                                "Відсутні рядки для видалення!", QMessageBox.Ok, QMessageBox.Ok)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Delete:
            self.delete_row()

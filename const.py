
""" Constants for project 'My_counter' """
# from const import *

""" request_base.py """
DATA_BASE = 'Test.db'
# DATA_BASE = 'my_base.db'

""" main_window.py """
MAIN_WINDOW_LENGTH, MAIN_WINDOW_HEIGHT = 800, 600

""" window_statistic.py """
SET_GEO_X1, SET_GEO_Y1, SET_GEO_X2, SET_GEO_Y2 = 500, 500, 1000, 600  # setGeometry

SET_FIX_WID = 520  # setFixedWidth

ROW_HEIGHT = 17  # self.tableWidget.setRowHeight

STAT_HEADER = ["Витрати:", "Сума:", "Дата:"]
STAT_SQL = "SELECT name_pay, money, date FROM payments WHERE money NOT NULL ORDER BY date DESC"

""" window_del_division.py """
SET_FIX_SIZE_X, SET_FIX_SIZE_Y = 400, 240  # setFixedSize

""" window_regular_payments.py"""
FIX_SIZE_X, FIX_SIZE_Y = 850, 530

# REGULAR_PAYMENTS_SQL_LAST_MONTH = f"SELECT name_pay, money FROM payments WHERE div_pay = {None} " \
#                                   f"ORDER BY date DESC LIMIT 4"

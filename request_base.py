import sqlite3
from const import *


class Request(object):
    def __init__(self):
        self.con = sqlite3.connect(DATA_BASE)  # Can I use "with"?
        self.cur = self.con.cursor()

    def close_db(self):
        if self.con is not None:
            self.con.close()

    def show_base(self, request):
        try:
            self.cur.execute(request)
            rows = self.cur.fetchall()
            self.close_db()
            if not rows:
                rows = [(None, None, None)]
            return rows
        except sqlite3.OperationalError:
            self.__create_table_db()

    def execute_data(self, request):
        self.cur.execute(request)
        self.con.commit()
        self.close_db()

    def __create_table_db(self):
        self.con.executescript(
            "CREATE TABLE system("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "div VARCHAR (15), "
            "div_full_name VARCHAR (40));"
            
            "CREATE TABLE payments("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "date DATE, "
            "name_pay VARCHAR (30), "
            "counter_any DECIMAL(7, 2), "
            "price_any DECIMAL (5, 2), "
            "money DECIMAL (7, 2), "
            "any_text VARCHAR (30), "
            "div_pay VARCHAR (10));"

            "CREATE TABLE sys_widgets("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "name_div VARCHAR(15), "
            "name_customer VARCHAR(15), "
            "counter_old DECIMAL(10, 2);"
        )
        self.con.commit()
        self.close_db()

# req = "INSERT INTO OTHER (NAME, PAYMENTS) VALUES ('novus', 45.45)"
# request = Request()
# app = request.execute_data(req)

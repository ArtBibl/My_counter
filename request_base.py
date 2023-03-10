import sqlite3
import const


class Request(object):
    def __init__(self):
        self.con = sqlite3.connect(const.DATA_BASE)  # Can I use "with"?
        self.cur = self.con.cursor()

    def close_db(self):
        if self.con is not None:
            self.con.close()

    def show_base(self, request):
        try:
            self.cur.execute(request)
            rows = self.cur.fetchall()
            self.close_db()
            return rows
        except sqlite3.OperationalError:
            self.__create_table_db()

    def execute_data(self, request):
        self.cur.execute(request)
        self.con.commit()
        self.close_db()

    def __create_table_db(self):
        self.con.executescript(
            "CREATE TABLE IF NOT EXISTS system("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "div VARCHAR (15), "
            "div_full_name VARCHAR (40), "
            "name_customer VARCHAR (15), "
            "first_price DECIMAL(10, 2), "
            "first_counter DECIMAL(10, 3));"
            
            "CREATE TABLE IF NOT EXISTS payments("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "date DATE, "
            "name_pay VARCHAR (30), "
            "counter DECIMAL(10, 3), "
            "price DECIMAL (10, 2), "
            "money DECIMAL (10, 2), "
            "any_text VARCHAR (30), "
            "div_pay VARCHAR (10)); "
        )
        self.con.commit()
        self.close_db()

# req = "INSERT INTO OTHER (NAME, PAYMENTS) VALUES ('novus', 45.45)"
# request = Request()
# app = request.execute_data(req)

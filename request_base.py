import sqlite3


class Request(object):
    def __init__(self):
        self.con = sqlite3.connect('NewBase.db')  # Can I use "with"?
        self.cur = self.con.cursor()

    def close_db(self):
        if self.con is not None:
            self.con.close()

    def show_base(self, request):
        self.cur.execute(request)
        rows = self.cur.fetchall()
        self.close_db()
        if not rows:
            rows = [(None, None, None)]
        return rows

    def execute_data(self, request):
        self.cur.execute(request)
        self.con.commit()
        self.close_db()

    # @staticmethod
    # def insert_payments(name, counter, price, money, any_text):
    #     con = sqlite3.connect('NewBase.db')
    #     cur = con.cursor()
    #     request = "INSERT INTO payments(date, name_pay, counter_any, price_any, money, any_text) " \
    #               "VALUES (datetime('now', 'localtime'), '" + str(name) + "', " + str(counter) + ", " + str(price) \
    #               + ", " + str(money) + ", '" + str(any_text) + "')"
    #     cur.execute(request)
    #     con.commit()
    #     con.close()

# req = "INSERT INTO OTHER (NAME, PAYMENTS) VALUES ('novus', 45.45)"
# request = Request()
# app = request.execute_data(req)

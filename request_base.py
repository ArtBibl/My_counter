import sqlite3


class Request(object):
    def __init__(self):
        self.con = sqlite3.connect('NewBase.db')
        self.cur = self.con.cursor()

    def close_db(self):
        if self.con is not None:
            self.con.close()

    def show_other(self):

        request = "SELECT * FROM OTHER"
        self.cur.execute(request)
        rows = self.cur.fetchall()

        return rows

    @staticmethod
    def add_other(name, coast):
        con = sqlite3.connect('NewBase.db')
        cur = con.cursor()
        request = "INSERT INTO OTHER (NAME, PAYMENTS) VALUES ('" + str(name) + "', " + str(coast) + ")"
        cur.execute(request)
        con.commit()
        con.close()

    @staticmethod
    def insert_payments(name, counter, price, money, any_text):
        con = sqlite3.connect('NewBase.db')
        cur = con.cursor()
        request = "INSERT INTO payments(date, name_pay, counter_any, price_any, money, any_text) " \
                  "VALUES (datetime('now', 'localtime'), '" + str(name) + "', " + str(counter) + ", " + str(price) \
                  + ", " + str(money) + ", '" + str(any_text) + "')"
        cur.execute(request)
        con.commit()
        con.close()


# name1 = "novus"
# coast1 = 23.48
# app = Request.add_other(name1, coast1)
# app = Request.insert_payments("OSBB", 20.53, 10.20, 15.60, "any")
import sqlite3


class Request(object):
    @staticmethod
    def show_other():
        con = sqlite3.connect('NewBase.db')
        cur = con.cursor()
        request = "SELECT * FROM OTHER"
        cur.execute(request)
        rows = cur.fetchall()
        con.close()
        return rows

    @staticmethod
    def add_other(name, coast):
        con = sqlite3.connect('NewBase.db')
        cur = con.cursor()
        request = "INSERT INTO OTHER (NAME, PAYMENTS) VALUES ('" + str(name) + "', " + str(coast) + ")"
        cur.execute(request)
        con.commit()
        con.close()


# name1 = "novus"
# coast1 = 23.48
# app = Request.add_other(name1, coast1)

from datetime import datetime
from request_base import Request


def get_month_sql(month: int = None) -> list:
    if month is None:
        today = datetime.today()
        day = today.day
        month = today.month
        year = today.year
    sql_req = f"SELECT * FROM payments WHERE strftime('%m', date) = '0{month}'"
    request = Request()
    data = request.show_base(sql_req)
    return data


""" for test """
print(get_month_sql(2))

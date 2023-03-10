import datetime
from count_days import count_days

# data = [
#     ('telephone(1)', -160, '2022-12-30 18:18:38'),
#     ('sequrity(1)', -190, '2023-01-01 18:22:07'), ('new(1)', -24, '2023-01-01 18:22:01'),
#     ('telephone(1)', -160, '2023-01-03 18:18:38'),
#     ('new(1)', -24, '2023-01-04 18:18:15'),
#     ('osbb(1)', -150.33, '2023-01-05 01:07:43'),
#     ('telephone(1)', -160, '2023-01-06 01:07:33'), ('osbb(2)', -350.56, '2023-01-06 00:23:02'),
#     ('sequrity(1)', -190, '2023-01-07 00:22:59'), ('new(1)', -24, '2023-01-07 00:22:59'),
#     ('telephone(1)', -160, '2023-01-08 00:22:58'), ('osbb(1)', -150.33, '2023-01-08 00:22:55'),
#     ('osbb(2)', -350.56, '2023-01-09 13:42:05'), ('new(1)', -24, '2023-01-09 13:40:10'),
#     ('osbb(2)', -350.56, '2023-01-10 13:31:11'), ('sequrity(1)', -190, '2023-01-10 13:28:25'),
#     ('telephone(1)', -160, '2023-01-11 13:28:16'), ('osbb(1)', -150.33, '2023-01-11 13:26:37'),
#     ('sequrity(1)', -190, '2023-01-12 13:22:07'), ('gas(1)', -86.6, '2023-01-12 23:51:44'),
#     ('osbb(2)', -350.56, '2023-01-13 23:51:22'), ('telephone(1)', -160, '2023-01-13 23:51:20'),
#     ('osbb(1)', -150.33, '2023-01-14 23:51:19'),
#     ('electric(1)', -73.92, '2023-01-16 23:39:00'),
#     ('telephone(1)', -145, '2023-01-17 23:38:58'), ('telephone(1)', -160, '2023-01-17 23:38:53'),
#     ('fgdha', 564, '2023-01-18 23:38:26'),
#     ('fgh', 56, '2023-01-19 23:38:21'), ('dh', -445, '2023-01-19 23:38:03'),
#     ('ghfj', -546, '2023-01-20 23:38:00'),
#     ('electric(1)', -73.92, '2023-01-21 23:37:51'),
#     ('osbb(1)', -150.33, '2023-01-22 23:37:41'), ('osbb(2)', -350.56, '2023-01-22 23:37:39'),
#     ('osbb', -350.25, '2023-01-23 23:25:10'), ('telephone', -160, '2023-01-23 23:15:01'),
#     ('fghj', -234, '2023-01-24 15:08:23'), ('gjf', -57, '2023-01-24 15:08:16')
#     ]


def sort_by_date(data: list) -> list:
    """return sorted list by data"""
    data_old = data[::-1]

    first_date = data_old[0][2].rsplit(' ', -1)[0]
    last_date = data_old[-1][2].rsplit(' ', -1)[0]
    # print(f"first_date: {first_date}, last_date: {last_date}")
    # print(data_old)
    minus_day = count_days(first_date, last_date)
    first_date = datetime.datetime.strptime(first_date, "%Y-%m-%d").date()
    new_data = [[0, str(first_date + datetime.timedelta(days=i))]
                for i in range(0, minus_day)]

    index_new_data = 0
    for i in data_old:
        while True:
            if new_data[index_new_data][1] not in i[2]:
                index_new_data += 1
                continue
                # print(f"not found {new_data[index_new_data][1]} in {i[2]}")
            new_data[index_new_data][0] += i[1]
            new_data[index_new_data][0] = round(new_data[index_new_data][0], 2)
            # print(f"find {new_data[index_new_data][1]} in {i[2]}")
            break
    return new_data

# print(sort_by_date(data))

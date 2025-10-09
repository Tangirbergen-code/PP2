
from datetime import date, timedelta, datetime

# # 1
# now = date.today()
# new_date = now - timedelta(days=5)
# print(new_date)

# # 2
# today = date.today()
# yesterday = today - timedelta(days=1)
# tomorrow = today + timedelta(days=1)

# print(today)
# print(yesterday)
# print(tomorrow)

# # 3
# now = datetime.now()
# nomicro = now.replace(microsecond = 0)
# print(now)
# print(nomicro)

# # 4

# date1 = datetime(2025, 10, 1, 12, 0, 0)
# date2 = datetime(2025, 10, 9, 12, 0, 0)

# diff = date2 - date1
# diffsec = diff.total_seconds()
# print(diff)
# print(diffsec)
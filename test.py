import datetime
import calendar

# 現在の年と月を取得
today = datetime.date.today()
year = today.year
month = today.month

# 平日の日付を出力
for day in range(1, calendar.monthrange(year, month)[1] + 1):
    date = datetime.date(year, month, day)
    if date.weekday() < 5:
        print(date)
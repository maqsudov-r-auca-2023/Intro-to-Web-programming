import datetime

current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")

custom_date = datetime.date(2023, 12, 25)
print(f"Custom date: {custom_date}")

future_date = current_time + datetime.timedelta(days=7)
print(f"Date after 7 days: {future_date}")

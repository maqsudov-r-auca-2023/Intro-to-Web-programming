import datetime

def days_until_new_year():
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)
    difference = new_year - today
    print("Days until New Year's Eve:", difference.days)

days_until_new_year()

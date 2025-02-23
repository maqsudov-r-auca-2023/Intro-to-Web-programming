import datetime

def display_current_datetime():
    now = datetime.datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()
import time

def countdown_timer(seconds):
    while seconds:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Timer finished!")

countdown_timer(10)  
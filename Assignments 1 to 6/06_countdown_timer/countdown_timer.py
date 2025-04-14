import time

def countdown_timer (t):
    while t:
        min, sec = divmod(t, 60)
        time_format = '{:02d}: {:02d}'.format(min, sec)

        print(time_format, end='\r')
        time.sleep(1)
        t -= 1

    print("Timer completed!")


t = input("Enter a time to start: ")
countdown_timer(int(t))
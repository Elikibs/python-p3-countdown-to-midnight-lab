# your code goes here!
import time
def countdown(secs):
    while secs > 0:
        print(f'{secs} SECOND(S)!')
        secs -= 1
    print("HAPPY NEW YEAR")
countdown(10)


# // Countdown with time sleeep
def countdown_with_sleep(secs):
    while secs > 0:
        print(f'{secs} SECOND(S)!')
        secs -= 1
        time.sleep(2)
    print("HAPPY NEW YEAR")
countdown_with_sleep(10)
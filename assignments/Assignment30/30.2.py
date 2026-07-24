# program to display current date and time

import time 
import schedule
from datetime import datetime

def display():
    print("Current date-time is: ", datetime.now())

def main():
    schedule.every(1).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()        
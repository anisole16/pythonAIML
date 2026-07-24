# program to print a particular sentence every day at a particular time

import schedule
import time

def greet():
    print("Namaskar... Have a good day Ahead !")
def main():
    schedule.every().day.at("10:35").do(greet)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()            
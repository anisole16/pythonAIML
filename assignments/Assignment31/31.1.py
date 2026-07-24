# python program that accepts message from user and prints it after  given interval

import schedule
import time



message = input("Enter  the message you want to print: ").strip()
interval = int(input("Enter time in seconds: "))


def display(msg):
    print(msg)
    


def main():
    schedule.every(interval).seconds.do(display, message)

    while True:
        schedule.run_pending() 
        time.sleep(1)  

if __name__ == "__main__":
    main()



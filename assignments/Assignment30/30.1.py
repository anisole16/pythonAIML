# write a program that display a sentene after every 2sec


import schedule  
import time


def display():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()        
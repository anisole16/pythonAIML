# create a function named display_msg to display the message given by user

import schedule
import time

message = input("Enter the message you want to print: ").strip()


def display_message(msg):
    print(msg)

def main():
    schedule.every(5).seconds.do(display_message, message)


    while True:
        schedule.run_pending()
        time.sleep(1) 

if __name__ == "__main__":
    main()      
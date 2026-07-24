# print luch time at 1pm and wrap up work at 6pm in diff function

import time
import schedule

def lunch():
    print("Its lunch Time....")

def work():
    print("Wrap up the work.....")

def main():
    schedule.every().day.at("13:05").do(lunch) 
    schedule.every().day.at("18:05").do(work)       

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()        
# schdeule a program


import schedule
import time

def monday():
    print("Start Your Schedule....")

def wednesday():
    print("Review your Schedule...")

def friday():
    print("Weekly Work Completed...")

def main():
    schedule.every().monday.at("09:00").do(monday)
    schedule.every().wednesday.at("17:00").do(wednesday)    
    schedule.every().friday.at("18:00").do(friday)    

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
                  
# create a new log file after every 10 min

import schedule
import time
from datetime import datetime

def create():
    current = datetime.now()

    filename = "new" + current.strftime("%d-%m-%Y-%H-%M-%S") + ".txt"

    with open(filename, "w") as fobj:
        fobj.write("File created Successfully...\n")
        fobj.write("Current-time: "+ current.strftime("%d-%m-%Y %I:%M:%S %p"))

    print(filename , "created.")

def main():
    schedule.every(10).minutes.do(create)
    create()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()        

           



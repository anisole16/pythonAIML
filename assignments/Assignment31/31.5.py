# count the number of files in the directory

import os
import schedule
import time
from datetime import datetime

name = input("Enter directory path: ").strip()

def count():
    total = 0

    for Folder , SubFolder , Files in os.walk(name):
        total += len(Files)

    print("\nDirectory: ", name)
    print("\nTotal Files: ",total )
    print("Time: ",datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))


def main():
    schedule.every(5).minutes.do(count) 
    count() 

    while True:
        schedule.run_pending()
        time.sleep(1)


 

if __name__ == "__main__":
    main()      


# create a file Marvellous and print the current data and time in that file


import schedule
import time
from datetime import datetime

def write_file():
    with open("Marvellous.txt", "a") as fobj:
        current = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        fobj.write(current + "\n")
        print("Entry Added..")

def main():
    schedule.every(1).minutes.do(write_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
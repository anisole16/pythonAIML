# backup file every hour


import schedule
import time
import os
from datetime import datetime
import shutil

source = input("Entry source File name: ").strip()
destination = input("Entry Destination File name: ").strip()

def backup():
    current = datetime.now.strftime("%d-%m-%Y-%H-%M-%S")
    backup_file = destination + "/Backup_" + current + ".txt"
    shutil.copy(source, backup_file)

    with open("backup_log.txt", "a") as fobj:
        fobj.write("Backup Completed at" + current + "\n")
        print("Backup Completed...")

def main():
    schedule.every().seconds.do(backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


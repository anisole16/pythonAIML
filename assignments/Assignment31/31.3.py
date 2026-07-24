import schedule
import time
import os
from datetime import datetime

name = input("Enter the directory path you want to scan: ").strip()

def scan():
    if not os.path.isdir(name):
        print("Invalid directory!")
        return

    files = 0
    subdirs = 0

    for root, folders, filenames in os.walk(name):
        files += len(filenames)
        subdirs += len(folders)

    print("\n----------------------------")
    print("Directory:", name)
    print("Total Files:", files)
    print("Total Subdirectories:", subdirs)
    print("Scan Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
    scan()  # Initial scan

    # Scan every minute
    schedule.every().minute.do(scan)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
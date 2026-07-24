# monitor the size of the file every every 30sec

import os
import schedule
import time
from datetime import datetime



file_name = input("Enter file path: ").strip()
log_file = "demo.txt"

while True:
    with open(log_file , "a") as fobj:
        if os.path.exists(file_name):
            size = os.path.getsize(file_name)
            fobj.write(f"Size: {size}bytes\n")
            fobj.write(f"Date & Time: {datetime.now()}\n")
            print(f"Logged: {size} bytes\n")
        else:
            print("File does not exist....")

    time.sleep(30)            

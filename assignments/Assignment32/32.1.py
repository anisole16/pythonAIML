# program to create txt file within 1 second


import time 
import schedule
from datetime import datetime

while True:
    current = datetime.now()

    filename = current.strftime("File-%d-%m-%Y-%H-%M-%S.txt")

    with open(filename , "w") as fobj:
        fobj.write(f"Filename: {filename}\n")
        fobj.write(f"Create-date: {current.strftime('%d-%m-%Y')}\n")
        fobj.write(f"Create-time: {current.strftime('%H:%M:%S')}\n")

    print(f"{filename} created Successfully...")

    time.sleep(60)








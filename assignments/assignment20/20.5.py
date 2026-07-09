# two threads 1-50 and other 50-1

import threading

def accending():
    for i in range(1,51):
        print(i, end = "")

def deccending():
    for i in range(50,0, -1):
        print(i, end = "")

t1 = threading.Thread(target = accending)
t2 = threading.Thread(target = deccending)

t1.start()
t1.join()

t2.start()
t2.join()

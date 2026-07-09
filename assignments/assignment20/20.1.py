# two seperate thread Even and Odd

import threading

def even():
    print("First 10 even number: ")
    for i in range(2, 21, 2):
        print(i, end = "")

def odd():
    print("First 10 odd numbers: ")
    for i in range(1,20,2):
        print(i , end = "")

t1 = threading.Thread(target = even)
t2 = threading.Thread(target = odd)

t1.start()
t2.start()

t1.join()
t2.join()
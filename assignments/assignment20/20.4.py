# three threads small capital and digit
import threading


s = input("Enter a string: ")
class SmallThread(threading.Thread):
    def run(self):
        count = sum(1 for ch in s if ch.islower())
        print("\nThread Id:",threading.get_ident())
        print("\nThread Name: ", threading.current_thread().name)
        print("Lowercase  Letters: ",count)

class UpperThread(threading.Thread):
    def run(self):
        count = sum(1 for ch in s if ch.isupper())
        print("\nThread Id:",threading.get_ident())
        print("\nThread Name: ", threading.current_thread().name)
        print("Upercase  Letters: ",count)  

class DigitThread(threading.Thread):
    def run(self):
        count = sum(1 for ch in s if ch.isdigit())
        print("\nThread Id:",threading.get_ident())
        print("\nThread Name: ", threading.current_thread().name)
        print("Digits: ",count)              


t1 = SmallThread(name = "Small")
t2 = UpperThread(name = "Upper")
t3 = DigitThread(name = "Digit")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

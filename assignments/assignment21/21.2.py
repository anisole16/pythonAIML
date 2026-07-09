import threading

def maximum(lst):
    print("Maximum elements from list", max(lst))

def minimum(lst):
    print("Minimum elements from list", min(lst))    

n = int(input("Enter number of elements in list: "))
lst = []

for i in range(n):
    lst.append(int(input()))

t1 = threading.Thread(target = maximum, args=(lst,))    
t2 = threading.Thread(target = minimum, args=(lst,))   

t1.start()
t2.start()

t1.join()
t2.join()
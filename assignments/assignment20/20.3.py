#acept one list two threads evenlist and oddlist 


import threading

def even_list(arr):
    sum = 0
    print("Even elements from the list are: ")
    for i in arr:
        if i % 2 == 0:
            print(i)
            sum = sum + i
    print("Sum of Even elements: ", sum)     


def odd_list(arr):
    sum = 0
    print("Odd elements from the list are: ")
    for i in arr:
        if i % 2 != 0:
            print(i)
            sum = sum + i
    print("Sum of Odd elements: ", sum)             

n = int(input("Enter the number of elements in the list: "))
arr = []

for i in range(n):
    x = int(input("Enter elements: "))
    arr.append(x)

t1 = threading.Thread(target = even_list, args= (arr,))    
t2 = threading.Thread(target = odd_list, args= (arr,))  

t1.start()
t2.start()

t1.join()
t2.join()
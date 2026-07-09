# python application that accepts two thread prime and non prime


import threading


def prime(l):
    print("Prime Numbers are: ")
    for n in l:
        if n > 1:
            for i in range(2,n):
                if n % i == 0:
                    break
                else:
                    print(n , end= "")
    print()


def nonprime(l):
    print("Non prime numbers are: ")                    
    for n in l:
        if n <= 1:
            print(n, end = "")
        else:
            for i in range(2,n):
                if n % i == 0:
                    print(n, end = "")
                    break
    print()

size = int(input("Enter number of elements:"))
l =[]
print("Enter elements: ")
for i in range(size):
    l.append(int(input()))    


t1 = threading.Thread(target = prime, args=(l,))        
t2 = threading.Thread(target = nonprime, args=(l,))  

t1.start()
t2.start()

t1.join()
t2.join()
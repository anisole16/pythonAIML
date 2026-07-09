# create two thread even factor and odd factor


import threading

def even_factor(no):
    sum = 0
    print("Even fators of the given number are: ")
    for i in range(1, no + 1):
        if (no  % i == 0 and no % 2 == 0):
            print(i)
    print("Sum of Even Factors: ",sum)      


def odd_factor(no):
    sum = 0
    print("Odd fators of the given number are: ")
    for i in range(1, no + 1):
        if (no  % i == 0 and no % 2 != 0):
            print(i)
    print("Sum of Odd Factors: ",sum)  

n = int(input("Enter number: "))    

t1 = threading.Thread(target = even_factor, args =(n,))
t2 = threading.Thread(target = odd_factor, args =(n,))

t1.start()
t2.start()

t1.join()
t2.join()



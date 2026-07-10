# sum of all the even numbers using pool

from multiprocessing import Pool
import os

def  sum_even(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum = sum + i
    print(" Process_id: ",os.getpid())
    print("Input Number: ",n)
    print("Sum of even numbers is: ", sum)
    print()    

if __name__ == "__main__":
    data = [100, 200, 300, 400]

    p = Pool()
    p.map(sum_even, data)
    p.close()
    p.join()



   




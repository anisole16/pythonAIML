# count even numbers from 1 to n


import multiprocessing 
import os

def even_count(n):
    count = 0

    for i in range(2, n+1,2):
        count = count + 1

    print("Process-Id: ", os.getpid())
    print("Input numbers: ", n)
    print("Even Numbers Count: ",count)
    print()

if __name__ == "__main__":
    data = [100, 200, 300]

    p = multiprocessing.Pool()
    p.map(even_count, data)
    p.close()
    p.join()
    



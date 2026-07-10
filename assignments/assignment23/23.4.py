import multiprocessing 
import os

def odd_count(n):
    count = 0

    for i in range(1, n+1,2):
        count = count + 1

    print("Process-Id: ", os.getpid())
    print("Input numbers: ", n)
    print("odd Numbers Count: ",count)
    print()

if __name__ == "__main__":
    data = [100, 200, 300]

    p = multiprocessing.Pool()
    p.map(odd_count, data)
    p.close()
    p.join()
    
#factorial of multiple numbers using Pool

from multiprocessing import Pool
import math
import os


def factorial(n):
    return (os.getpid(), n, math.factorial(n))

if __name__ == "__main__":
    numbers = [10 ,25 ,30, 68]

    with Pool() as p:
        result = p.map(factorial, numbers)

    for pid , num , fact in result:
        print("Proces_id: ", pid)
        print("Input Number: ", num)
        print("Fcatorial: ",fact)
        print()    

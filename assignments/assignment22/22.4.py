from multiprocessing import Pool
import time


def sum_power(n):
    return sum(i ** 5 for i in range(1, n+ 1))

if __name__ == "__main__":
    numbers = [100, 200, 300]

    start = time.perf_counter()

    with Pool() as p:
        result = p.map(sum_power, numbers)

    end = time.perf_counter()

    for n , ans in zip(numbers, result):
        print("N=", n)
        print("Sum = ", ans)
        print()

    print("Execution time: ", end - start, "Seconds")        
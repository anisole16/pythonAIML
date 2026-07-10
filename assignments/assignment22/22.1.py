# sum of the square of first n natural number using pool map

from multiprocessing import Pool

def sum_of_square(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i * i
    return sum      
    

if __name__ == "__main__":
    numbers = [1000000, 2000000, 3000000, 40000000]

    with Pool() as p:
        result = p.map(sum_of_square, numbers)

    print(result)        


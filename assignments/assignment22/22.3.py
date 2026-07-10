from multiprocessing import Pool

def prime_num(n):
    count = 0

    for i in range(2, n+1):
        prime = True
        for j in range(2,i):
            if i % j == 0:
                prime = False
                break

        if prime:
            count = count + 1

        return count

if __name__ == "__main__":
    num = [1000000, 2000000, 3000000]

    p = Pool()
    result = p.map(prime_num, num)

    p.close()
    p.join()

    for i in range(len(num)):
        print("prime count from 1 to num[i]", "=", result[i])             

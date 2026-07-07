# factors of a given number


def factors(num):
    print("Factors are:")
    for i in range(1, num+1, 1):
        if num % i == 0:
            print(i, end = " ")
n = int(input("Enter any number"))
factors(n)            
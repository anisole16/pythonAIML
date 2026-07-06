# accept a number and sum of first  natural number


def SumNatural(num):
    count =  0
    for i in range(1, num + 1):
        count = count + i
    print("Sum =", count) 

n = int(input("Enter any number"))
SumNatural(n)       

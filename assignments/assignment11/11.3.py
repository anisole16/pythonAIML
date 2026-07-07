# accept one number and print sum of the digits


def SumDigit(num):
    total = 0
    while num >0:
        total = total + num % 10
        num //= 10 
    print("Sum = ", total)    
n = int(input("Enter any number: "))
SumDigit(n)        

# accept one number and print the number of count of digits in that number

def CountDigit(num):
    count = 0
    
    while (num > 0):
        count = count + 1
        num //= 10
    print("count =", count)

n = int(input("Enter any number: "))
CountDigit(n)        

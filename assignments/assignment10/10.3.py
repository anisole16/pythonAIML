# accept a number and take factorial

def Factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial =", fact)
n = int(input("Enter any number: ")) 
Factorial(n)       
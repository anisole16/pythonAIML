# acept a number and find factorial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

num = int(input("Enter any number: "))
print("Factorial of the given number is: ",
factorial(num) )   
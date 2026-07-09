# python program to acept two numbers and perfrom addition

def add(a,b):
    return a + b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    print("Summation is: ", result)
    add(num1, num2)

main()    

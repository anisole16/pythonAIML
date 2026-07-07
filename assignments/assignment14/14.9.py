# lambda function to multiply two number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
product = lambda a, b: a*b
print("Product of two number is: ", product(a,b))
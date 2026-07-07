# lambda  function to add two number


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add = lambda a , b: a+b
print("Addition of two number is: ",add(a,b))
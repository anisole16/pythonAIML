num1 = int(input("enter first number: "))
num2 = int(input("Enter second number: "))
maximum = lambda num1 , num2: num1 if (num1 > num2) else num2
print("Maximum among two number is: ", maximum(num1, num2))
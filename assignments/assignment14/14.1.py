#lambda function to take square of a number

num = int(input("Enter any Number: "))
square = lambda num: num ** 2
print("Square of the number is: ", square(num))
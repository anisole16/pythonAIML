# lambda function to return minimum of two numbers


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
minimum = lambda a , b: a if(a < b) else a
print("Minimum number among two  number is:  ", minimum(a,b))
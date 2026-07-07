#lambda function to check whether number is divisible ny 5

num =int(input("Enter any number"))
is_divisble = lambda num: num % 5 == 0 
print(is_divisble(num))
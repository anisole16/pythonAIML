# lambda function to check whether number is odd

num = int(input("Enter any Number: "))
is_odd = lambda num: num % 2 != 0
print(is_odd(num))
# lambda function to check number is even

num = int(input("Enter any number: "))
is_even = lambda num: num % 2 == 0
print(is_even(num))
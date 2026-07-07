# maximum number using reduce function 

from functools import reduce
num = list(map(int, input("Enter a list of numbers").split()))

maximum = reduce(lambda x, y: x if x > y else y, num)
print("Maximum among number is: ", maximum)
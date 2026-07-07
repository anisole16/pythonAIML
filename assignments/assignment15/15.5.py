# minimum elements using reduce

from functools import reduce
num = list(map(int, input("Enter a list of numbers").split()))

minimum = reduce(lambda x, y: x if x < y else y, num)
print("Minimum among number is: ", minimum)

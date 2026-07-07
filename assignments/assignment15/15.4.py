# sum of all elements using reduce
from functools import reduce

num = list(map(int, input("Enter the list of numbers to be added seperated by space").split()))

total = reduce(lambda x , y: x+ y, num )
print("Sum of all the elements is: ", total)
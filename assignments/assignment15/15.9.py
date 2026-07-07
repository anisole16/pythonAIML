#product of the numbers using reduce

from functools import reduce

num = list(map(int,input("Enter the list of numbers").split()))
product = reduce(lambda x , y: x*y, num)
print("Product: ",product)
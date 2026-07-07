# number divisible by 3 and 5

numbers = list(map(int, input("enter numbers seperated  by space: ").split()))

result = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print("Numbers divisible by 3 and 5 are: ", result)
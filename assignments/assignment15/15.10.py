#count even numbers using filter()

num = list(map(int,input("Enter numbers seperated by space").split()))

count = len(list(filter(lambda x: x % 2 == 0, num)))
print("Count of even numbers is: ",count)
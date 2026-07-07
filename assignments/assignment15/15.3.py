# find odd numbers using using filter


num = list(map(int,input("Enter the numbers seperated by space: ").split()))
odd_num = list(filter(lambda x: x % 2 != 0, num))

print("ODD numbers from the list are: ", odd_num)
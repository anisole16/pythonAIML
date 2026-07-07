# ecven number using filter

num = list(map(int, input("Enter the number seperated by space").split()))
even_num = list(filter(lambda x : x % 2 == 0 ,num ))

print("Even numbers from the given list is: ", even_num)
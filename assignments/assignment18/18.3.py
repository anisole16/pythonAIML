def minimum(arr):
    return min(arr)

n = int(input("enter number of elements in array: "))
arr = []

for i in range(n):
    num = int(input("Enter the element: "))
    arr.append(num)

print("Minimum number among the given number is: ", minimum(arr))    
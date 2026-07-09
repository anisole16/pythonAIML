# accept n numbers store it in ary return the maximum number


def maximum(arr):
    return max(arr)

n = int(input("enter number of elements in array: "))
arr = []

for i in range(n):
    num = int(input("Enter the element: "))
    arr.append(num)

print("Maximum number among the given number is: ", maximum(arr))    
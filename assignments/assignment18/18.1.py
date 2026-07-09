# accpet n number from user store it in list and sum the elements in the list


def list_sum(arr):
    return sum(arr)

n = int(input("Enter number of element in the list: "))

arr = []

for i in range(n):
    num = int(input("Enter the elemets: "))
    arr.append(num)

print("Sum of elements: ",
    list_sum(arr))    

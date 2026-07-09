# acpet n number and return frequency of he given number


def frequency(arr, num):
    return arr.count(num)

n = int(input("Enter the number of elements in array: "))
arr = []
for i in range(n):
    num = int(input("Enter elements: "))
    arr.append(num)
 
search = int(input("Enter the number to search: "))
print("frequency = ",frequency(arr, search)) 
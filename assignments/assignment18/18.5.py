# accept n numbers and return adition of prime numbers

def prime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter elements: "))
    arr.append(num)

sum = 0

for i in arr:
    if prime(i):
        sum = sum + i
print("Sum of the prime number is: ", sum)        





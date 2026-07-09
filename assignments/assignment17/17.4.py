# find the adition of its factorss


def factors(n):
    total = 0
    for i in range(1,n):
        if (n % i == 0):
            total = total + i
    return total  

num = int(input("Enter number: "))
print("Adition of its factors is: ",factors(num))       
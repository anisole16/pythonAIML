# check the number is prime


def prime(n):
    if n <= 1:
        return False

    for i in range(2,n):
        if(n % i == 0):
            print(n,"is not prime number")
        return
    print(n,"is a prime number")  

def main():
    num = int(input("Enter any number: "))
    prime(num)

main()                  
        
# accept one number and print odd number

def OddNum(num):
    for i in range(1, num+1, 2):
        print(i , end = " ")
n = int(input("Enter any number: "))
OddNum(n)        
# accepts one number and multiplication table 

def mul_table(a):
    for i in range(1,11):
        print(a * i, end = " ")
num1 = int(input("Enter any number: "))
mul_table(num1)         
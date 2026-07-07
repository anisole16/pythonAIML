# check the number is perfect or not

def perfect_num(num):
    sum = 0
    for i in range(1,num):
        if(num % i == 0):
            sum = sum + i
    if sum == num:
        print("perfect number")
    else:
        print("Not perfect")   

n = int(input("Enter any number: "))
perfect_num(n)         


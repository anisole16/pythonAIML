# print numbers 1 to n

def print_number(num):
    for i in range(1, num+1, 1):
        print(i ,"\t" ,  end = "")
n = int(input("enter any number: "))
print_number(n)        
# print numbers from n to 1


def reverse_number(n):
    for i in range(n , 0, -1):
        print(i ,"\t" , end = "")
num = int(input("Enter a number: "))
reverse_number(num)
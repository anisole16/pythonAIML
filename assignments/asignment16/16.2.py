# function to display one function to check even and odd


def check_num(no):
    if (no % 2 == 0):
        print(no, "is even")
    else:
        print(no, "is odd")

def main():
    num = int(input("Enter any number: "))
    
    check_num(num)
main()
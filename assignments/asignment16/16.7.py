# accpet one function return true if divisble by 5


def divisibility(no):
    if (no % 5 == 0):
        print("True")
    else:
        print("False")   

def main():
    num =int(input("enter any number: "))
    divisibility(num)

main()             
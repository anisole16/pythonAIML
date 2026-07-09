# check number is positive and negative

def positive_negative(no):
    if (no >= 0):
        print(no, "is positive")

    else:
        print(no, "is negative")

def main():
    num = int(input("Enter any number: "))
    positive_negative(num)

main()           

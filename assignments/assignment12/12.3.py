# Perform addition subtraction multiplication and division


def arithmatic(num1, num2):
    print("Addition of the given numbers is: ", num1 + num2)
    print("Subtraction  of the given numbers is: ", num1 - num2)
    print("Multiplication of the given numbers is: ", num1 * num2)
    if num2 == 0:
        print("Division not possible")
    else:
        print("Division is: ",num1/num2)

n = int(input("Enter first number: "))
m = int(input("Enter first number: "))
arithmatic(n,m)
     


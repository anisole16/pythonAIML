# sum of the digit
def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

num = int(input("enter any number: "))
print("The sum of digit is: ", sum_digit(num))    


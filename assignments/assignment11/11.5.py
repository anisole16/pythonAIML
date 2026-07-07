# check palindrome ( number whose reverse are same)

def reverse_num(num):
    reverse = 0
    while (num > 0):
        digit = num % 10
        reverse = reverse * 10 + digit 
        num = num // 10
    return reverse

def palindrome(num):
    if num == reverse_num(num):
        print(num, "is a palindrome")
    else:
        print(num , "is not a palindrome")        
    
n = int(input("Enter any number"))
palindrome(n)
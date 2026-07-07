# accept a number and print its reverse

def reverse_num(num):
    reverse = 0
    
    while (num > 0):
        digit = num % 10               # 123 % 10 = 3
        reverse = reverse * 10 + digit  # 0 * 10 + 3 = 3
        num = num // 10                 # 123 // 10 = 12 
    print("Reverse of the given number is: ", reverse)

n = int(input("Enter any number"))
reverse_num(n)        
        

    

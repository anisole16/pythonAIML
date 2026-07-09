# accept a number and count the numberof digit

def num_count(n):
    count = 0
    while (n > 0):
        count = count + 1 
        n //= 10
    return count
    
def main():
    num = int(input("Enter a number: "))
    print("The total number of digits are: ",num_count(num) )
    
main()        
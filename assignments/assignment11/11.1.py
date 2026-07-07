# accept a number and check whether prime or not 

def PrimeNum(num):
    if (num <= 1):
        print("Number is not even nor odd")
    
    for i in range(2, num):
        if (num % i == 0):
            print(num,"is not prime")
            return 
        
    
    print(num, "is prime")  
n = int(input("Enter any number: "))
PrimeNum(n)                      


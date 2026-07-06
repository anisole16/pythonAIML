def divisible(a):
    if(a % 5 == 0 and a % 3 == 0):
        print(a,"is divisible by 5 and 3 both")
    else:
        print("Not divisible ! ") 
num1 = int(input("Enter any number: "))
divisible(num1)           
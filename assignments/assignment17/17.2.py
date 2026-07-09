# take a number and print in following pattern 

def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
        print("")

num = int(input("enter any number: "))
pattern(num)

            

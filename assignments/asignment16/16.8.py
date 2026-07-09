# accept number and print no of  * on screen 


def pattern(no):
    for i in range(no):
        print("*", end = "")

    

def main():
    num = int(input("Enter any number: "))
    pattern(num)
main()    

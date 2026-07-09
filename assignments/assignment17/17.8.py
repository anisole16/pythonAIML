# triangle pattern 


def pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j , end = " ")
        print()    
def main():
    num = int(input("Enter any number: "))        

    pattern(num) 
main()       
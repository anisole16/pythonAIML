# number pattern 

def num_pattern(n):
    for i in range(n):
        for j in range(1,n+1):
            print(j , end= "")
        print()

def main():
    num = int(input("Enter any number: "))
    num_pattern(num)
main()                
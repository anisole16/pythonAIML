def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("* ", end = " " )
        print()

def main():
    num = int(input("Enter any number: "))
    pattern(num)

main()             
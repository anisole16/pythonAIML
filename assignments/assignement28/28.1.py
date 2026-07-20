# python program to accept the file from user and count the number of lines in the file

name = input("Enter the name of the file: ").strip()

with open(name , "r") as file:
    count = 0
    for line in file:
        count = count + 1

print("Total number of lines in the file are: ",count)        
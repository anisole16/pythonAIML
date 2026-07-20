# display the content line by line


name = input("Enter the name of the file: ").strip()

with open(name , "r") as file:
    for line in file:
        print(line, end = "")
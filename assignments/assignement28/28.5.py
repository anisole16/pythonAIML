# search the word in the file

name = input("Enter the name of the file: ").strip()
word = input("Enter the word to be searched in the file: ").strip()


with open(name , "r") as file:
    data = file.read()

if word in data:
    print("Word Found !")   
else:
    print("Enter valid word to be searched")     

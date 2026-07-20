# count the words in the file


name = input("Enter the name of the file: ").strip()  # strip removes the extra spaces b/a the nsame

with open(name , "r") as file:
    data = file.read()     # stores the contenet in variables data
    words = data.split()   # split seperate the text in words whenever there is space

print("Total no of words in the file: ",len(words))   
  

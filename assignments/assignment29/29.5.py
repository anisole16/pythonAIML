# write a python program to accept filename and one string and returns the frequency of string

filename = input("Enter the name of the file: ").strip()
word = input("Enter String: ").strip()

try: 
    with open(filename , "r") as fobj1:
        data = fobj1.read()

    count = data.count(word)
    print("Frequency: ",count)    
except FileNotFoundError:
    print("File not found")      
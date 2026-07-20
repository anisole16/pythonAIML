# python program to accept filename from user and display the contents from user

filename = input("Enter the name of the file: ").strip()

try:
    with open(filename , "r") as fobj:
        print(fobj.read())
except FileNotFoundError:
    print("File not Found !")        

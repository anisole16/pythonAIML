# program to accept the file name and check whether present in the current directory or  not
import os


filename = input("Enter the name of the file: ").strip()

if os.path.exists(filename):   # exists function is used to show whether file is present in the current directory
    print(filename , "exists")
else:
    print("File not found")    
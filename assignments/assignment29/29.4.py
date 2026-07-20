# compare the content of two files in command line argument 

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]   # arguments are 2as two files are comapared


with open(file1 , "r") as fobj1:
    data1 = fobj1.read()

with open(file2 , "r") as fobj2:
    data2 = fobj2.read()
if data1 == data2:
    print("contents are same")
else:
    print("contents are not same")            
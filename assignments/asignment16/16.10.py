# find the length of string 


def len_str(s):
    count = 0
    for ch in s:
        count = count + 1
    return count

text = input("Enter a string: ")
length = len_str(text)
print("Length of the string is: ",length)


      



    
        

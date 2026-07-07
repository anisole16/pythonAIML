#  accepts a character and checks whether it is a vowel or consonant

def vowel_check(ch):
    if ch in "aeiouAEIOU":
        print(ch, "is a vowel")
    else:
        print(ch, "is a consonant")    

char = input("enter any alphabet: ")
vowel_check(char)
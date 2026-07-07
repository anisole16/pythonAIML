# grade with marks 


def grades(marks):
    if marks >= 75:
        print("Grade is A")
    elif marks >= 60:
        print("Grade is B")
    elif marks > 50:
        print("Grade is C")
    else:
        print("Fail")

m = int(input("enter your marks: "))
grades(m)                


# accept the length and width and print the area


def rec_area(length, width):
    area = length * width
    print("area is: " ,area)

len = int(input("Enter the length of the rectangle: "))
wid = int(input("Enter the width of the rectangle: "))
rec_area(len, wid)



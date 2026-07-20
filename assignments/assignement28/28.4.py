# copy the file content in another file

source = input("Enter the file name whose content are to be copied: ").strip()
destination = input("Enter the file name where content is pasted: ").strip()

with open(source , "r") as file:
    data = file.read()

with open(destination , "w") as file:
    file2 = file.write(data)

print("Content copied Successfully !")

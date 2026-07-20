# copy the content in the new file using commandline argument

import sys

source = sys.argv[1]   #hello.txt
destination = "Demo.txt"

with open(source , "r") as fobj:   # reads the content from source file
    data = fobj.read()             # copies the read data in variable data

with open(destination, "w") as fobj2:   # opens the destination file in write mode
    fobj2.write(data)                   # copies the data from "data" variable and wites in fobj2


print("Content copied successfully !")    
import os
fobj = open("First_File.txt")

line = fobj.readline()

while line != "":
    print(line,end="")
    line = fobj.readline()

path = os.getcwd()
print(path)

fobj.close()   
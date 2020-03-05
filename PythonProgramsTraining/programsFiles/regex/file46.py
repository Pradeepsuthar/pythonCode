import re

# opening file in read mode
fr = open("info.txt")
data = fr.read()
fr.close()
# extracting all numbers from file data
numbers = re.findall('\d+[.]?\d*', data)
print(numbers)

# opening/creating file in write mode
fw = open("numbers.txt", "w")
for item in numbers:
    fw.write(item+"\n")
else:
    fw.close()
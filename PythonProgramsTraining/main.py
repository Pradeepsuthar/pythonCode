# python provied function and methos to preform such as creating, reading, opening, closing etc.

# open file in python
# Syntax
#   fileobject = open(file_name[,access_mode][,buffring])
# NOTE : Default access_mode is read

# Create/Open file in write mode
fw = open("emp.txt","w")
# write data into file
fw.write("324156\n")
fw.write("Pradeep Suthar\n")
fw.write(input("Enter mobile Number : "))
fw,close()
print("Reading file\n")
fr = open("emp.txt")
data = fr.read()
fr.close()
print("\n",data)
















try:
    # task 1
    bill = int(input("Enter Bill Amount : "))
    quantity = int(input("Enter Quantity : "))
    rate = bill/quantity
    print("Rate per KG is : %0.2f Rs" %rate)
except Exception as ex1:
    print(type(ex1), " : ", ex1)
try:
    # task 2
    marks = [96.5, 86, 72, 56, 68, 74]
    rollno = int(input("Enter Roll No : "))
    print("marks of %d roll no is : %0.2f "%(rollno, marks[rollno-1]))
except Exception as ex2:
    print(type(ex2), " : ", ex2)
try:
    # task 3
    FILENAME = input("Enter File Name : ")
    fr = open(FILENAME)
    print("File Data : \n", fr.read())
    fr.close()
except Exception as ex3:
    print(type(ex3), " : ", ex3)
# end
print("All is Well")
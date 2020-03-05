try:
    # task 1
    bill = int(input("Enter Bill Amount : "))
    quantity = int( input("Enter Quantity : ") )
    rate = bill/quantity
    print("Rate per KG is : %0.2f Rs" %rate)
except Exception as ex1:
    print(type(ex1)," : ", ex1 )
try:
    # task 2
    marks = [92.5, 66, 84, 62, 76, 54]
    rollno = int(input("Enter Roll No : "))
    print("Marks of Roll No %d is : %0.2f"%(rollno, marks[rollno-1]))
except Exception as ex2:
    print(type(ex2)," : ", ex2 )
try:
    # task 3
    FILE_NAME = input("Enter File Name : ")
    fr = open(FILE_NAME)
    print(fr.read())
    fr.close()
except Exception as ex3:
    print(type(ex3)," : ", ex3 )
# end
print("All is Well")
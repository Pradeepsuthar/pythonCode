try:
    #task1
    bill = int(input("Enter bill Amount : "))
    qty = int(input("Enter Quantity : "))
    rate = bill/qty
    print("Rate per KG is : %0.2f Rs."%rate)
except Exception as ex1:
    print(Exception(ex1), " : ",ex1)

try:
    #task2
    marks = [96.5, 86, 72, 56, 68, 74]
    rollno = int(input("Enter Roll No. : "))
    print("Marks of %d roll no. is %0.2f "%(rollno,marks[rollno-1]))
except Exception as ex2:
    print(Exception(ex2), " : ",ex2)

try:
    #task3
    FILNAME = input("Enter File Name : ")
    fr = open(FILNAME)
    print("File Data : \n",fr.read())
    fr.close()
except Exception as ex3:
    print(Exception(ex3), " : ",ex3)

# end 
print("All Task Done Successfully")

try:
    bill = int(input("Enter bill amount:- "))
    quantity = float(input("Enter quantity:- "))
    rate=bill/quantity
    print("RATE:-  %0.2f"%rate)
except Exception as ex1:
    print(type(ex1)," : ",ex1)

try:
    marks=[90.2,34,56.87,15]
    rno=int(input("Enter roll number:- "))
    print("Marksof roll no %d is %0.2f"%(rno,marks[rno-1]))
except Exception as ex2:
    print(type(ex2)," : ",ex2)
try:
    FILE_NAME=input("Enter file name:- ")
    fr=open(FILE_NAME)
    print(fr.read())
    fr.close()
except Exception as ex3:
    print(type(ex3)," : ",ex3)
try:
    str="Divyansh"
    print(str[4])
except Exception as ex4:
    print(type(ex4)," : ",ex4)

print("HAHAHAAHAAHHAHAHHAHAHAHAHAHHAHAHHHAHAHAHHAHHAHHHHAHAHHHAHAHAHAHHAHAHAHAHHAHHAHAHAHAHHAHAHAHAHHAHAHAHHAHAHAHAHAHAHHAHAHAHHAHAAHHAHAHAHAHHAHAHAHAHAHHAAHAHAHHAHAHAHHAHAHAHAHHAHAHAH :)")
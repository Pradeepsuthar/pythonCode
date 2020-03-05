fr = None
try:
    FILENAME = input("Enter File Name : ")
    # opening file in read mode
    fr = open(FILENAME)
    lines = fr.readlines()
    Balance = float(lines[2])
    no = int( input("Enter No to devide : ") )
    Rs = Balance/no
    print("Rs per person is : %0.2f Rs" %Rs)
    print("Task Done")
except Exception as ex:
    # action code
    print(type(ex), " : ", ex)
finally:
    # code to release resource
    if fr:
        fr.close()
        print("File closed")
print("All is well")


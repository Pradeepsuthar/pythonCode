
FR = None
try:
    FILENAME = input("Enter File Name : ")
    # opening file in read mode
    FR = open(FILENAME)
    lines = FR.readlines()
    Balance = float(lines[2])
    no = int(input("Enter No of Persons : "))
    Rs = Balance/no
    print("Per Person Rs : %0.2f " %Rs)
    print("WellDone, Pranjal")
    # FR.close()
except Exception as ex:
    print( type(ex), " : ", ex)
finally:
    if FR:
        FR.close()
        print("File Closed")
print("All is Well")


FR = None
try:
    FILENAME = input("Enter File Name : ")
    # Opning file in read mode
    FR = open(FILENAME)
    lines = FR.realines()
    bal = float(lines([2]))
    no = int(input("Enter No of persons : "))
    Rs = bal/no
    print("Per Person Rs. %0.2f "%Rs)
    print("WellDone, Username")
except Exception as ex:
    print(type(ex), " : ",ex)
finally:
    if FR:
        FR.close()
        print("File closed")
print("Program executed successfully.")

   
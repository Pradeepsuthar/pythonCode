import datetime

def getBill(units, rate):
    'to calc bill'
    bill = units*rate*1.1
    print("Bill is : %0.2f Rs" %bill)

try:
    city = {294:'UDR', 44:"Chennai", 11:"Delhi", 22:"Mumbai"}
    std = int(input("Enter STD Code : "))
    print("%d is std code of %s" %(std, city[std]) )
    # calling fun
    getBill(400, 5.5)
    getBill(250, 2.5)
    fr = open( input("Enter File Name : ") )
    print( fr.read() )
    fr.close()
except ValueError as ve:
    print("Please value to sahi likho : ", ve)
except KeyError as ke:
    print("STD Code is not existing in Dict : %d - %s" %(std, ke) )
except Exception as ex:
    # creating/opening file in append mode
    fw = open("error.txt", "a")
    # returns currect date & time
    cdt = datetime.datetime.now()
    fw.write(str(cdt)+"\t"+str(type(ex))+"\t"+str(ex)+"\n")
    fw.close()
print("All is Well")






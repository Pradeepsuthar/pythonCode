import datetime
def getBill(units, rate):
    bill=units*rate*1.1
    print("Bill is:- %0.2f Rs"%bill)

try:
    city={294:'udr',44:'Chennai',88:'Bhinder'}
    std=int(input("Enter std code:- "))
    print("%d is std code of %s"%(std,city[std]))
    getbill(400, 5.5)
    getbill(250, 2.5)
    fr=open(input("Enter File name:- "))
    print(fr.read())
    fr.close()
except ValueError as ve:
    print("incorrect value")
except KeyError as ke:
    print("Std code not found")
except TypeError as te:
    print("incorrect type")
except Exception as ex:
    fw=open("error.txt","a")
    cdt=datetime.datetime.now()
    fw.write(str(cdt)+"\t"+str(type(ex))+"\t"+str(ex))
    fw.close()

print("all is well")

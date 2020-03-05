import datetime

def getGross(basic):
    gross = basic+basic*0.1+basic*0.2+basic*0.3
    print("Gross salary : %0.2fr Rs."%gross)

try:
    city={11:'New Dehli',22:'Mumbai',44:'Chennai'}
    std=int(input("Enter Std Code : "))
    #calling fun
    getGross(6000)
    getGross(7500)
    fr= open(input("Enter File name : "))
    print(fr.read())
    fr.close()
    print("Everything is fine")
except ValueError as vr:
    print("Please write coorect input %s"%vr)
except KeyError as kr:
    print("Given code %d is not STD List : %s"%(std,kr))
except Exception as ex:
    fw = open("errlog.txt","a")
    cdt = datetime.datetime.now()
    fw.write(str(cdt)+"\t\t"+str(type(ex)+"\t"+str(ex)+"\n"))
    fw.close()
    print("Error logged")

print("All is well")
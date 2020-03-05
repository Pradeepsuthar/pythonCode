import math
import re

class Operation:
    'to define basic methods to perform task'
    def areaCircle(self,radius):
        'to calc areaof circle'
        area = math.pi*radius**2
        print("Area of cirlce : %0.2f cm"%area)

    def countSpecial(self,str):
        'to extract special symbols'
        #extracting all symbols from str
        tokens = re.findall('[^a-z0-9]',str,re.I)
        print("Count : %d"%len(tokens))
        for ch in tokens:
            print(ch,end='')

# inheriting from base class
class Extra(Operation):
    def getNumber(self):
        str = input("Enter String : ")
        numbers = re.findall('\d+[.]?\d*',str)
        print(numbers)

obj = Extra()
obj.areaCircle(30)

obj.getNumber()
obj.countSpecial("UDAIPUR@2020#1cityofW0rld!n2020")


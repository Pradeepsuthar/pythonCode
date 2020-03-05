import math
import re

class Operation:
    'to define basic methods to perform task'

    def areaCircle(self, radius):
        'to calc area of circle'
        area = math.pi*radius**2
        print("Area of Circle is : %0.2f cm" %area)
    
    def countSpecial(self, str):
        'to extract special symbols'
        # extracting all symbols from str
        tokens = re.findall('[^a-z0-9]', str, re.I)
        print("Count : %d" %len(tokens) )
        for ch in tokens:
            print(ch, end='')

# inheriting from Base class
class Extra(Operation):
    'to define extra methods'
    
    def getNumbers(self):
        'to extract all numbers from str'
        str = input("Enter String : ")
        numbers = re.findall('\d+[.]?\d*', str)
        print( numbers)

# create an object
e1 = Extra()
e1.areaCircle(30)
e1.countSpecial("UDR@12#4570% ^we$#")
e1.getNumbers()





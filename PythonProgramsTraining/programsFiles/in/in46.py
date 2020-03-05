import math
import re

class Basic:
    'to define basic operations'

    def areaCylinder(self, radius, height):
        'to calc area of Cylinder'
        area = math.pi*radius*radius*height
        print("Area of Cylinder is : %0.2f cm" %area)
    
    def countSymbols(self, str):
        'to count special symbols'
        # extracting all non alpha & digits
        symbols = re.findall('[^a-z0-9]', str, re.I)
        print("Size : %d" %len(symbols) )
        for item in symbols:
            print(item, end="")

# inheriting Base class
class Advanced(Basic):
    'to define new operations'
    
    def getNumbers(self):
        'to extract all numbers from str'
        str = input("Enter String : ")
        numbers = re.findall('\d+[.]?\d*', str)
        print( numbers )

# creating an instance
ad1 = Advanced()
ad1.areaCylinder(20, 40)
ad1.countSymbols("Gits@2020$4010 #12 ^Ram&")
ad1.getNumbers()









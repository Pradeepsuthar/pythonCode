import math
import re

class Basic:

    def areaCylinder(self,radius,height):
        area = math.pi*radius*radius*height
        print("Area of cylinder is :%0.2f cm" %area)

    def countSymbols(self, str):
        symbols = re.findall('[^a-z0-9]', str ,re.I)
        print("Size: %d"%len(symbols))
        for item in symbols:
            print(item, end="")

class Advanced(Basic):
    'to define new operator'
    def getnumber(self):
        'to extract all numbers from str'
        str = input("Enter string:- ")
        numbers = re.findall('\d+[.]?\d*',str)
        print( numbers )
    
ad1 = Advanced()
ad1.areaCylinder(20, 40)
ad1.countSymbols("GITS_DIVYANSH2020200008 #12 ^Sita&")
ad1.getnumber()

        
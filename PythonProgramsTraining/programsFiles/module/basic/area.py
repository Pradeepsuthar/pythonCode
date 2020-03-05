'to define functions to calc area and class Book'
import math

def area_rect(len, wid):
    'to calc area of rectangle'
    area = len*wid
    print("Area of Rectangle is : %0.2f" %area)

def area_circle(radius):
    'to calc area of circle'
    area = math.pi*radius**2
    print("Area of Circle is : %0.2f " %area)

class Book:
    'to define Book information'

    def __init__(self, bc, bt, bp):
        'to initialize book'
        self.BCode = bc
        self.BTitle = bt
        self.BPrice = bp
    
    def getBookInfo(self):
        print("B Code : %d" %self.BCode)
        print("B Title : %s" %self.BTitle)
        print("B Price : %0.2f Rs" %self.BPrice)

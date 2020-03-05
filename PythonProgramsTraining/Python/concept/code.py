'to define area functions and class Book'
import math

def area_circle(radius):
    'to calc area of circle'
    area = math.pi*radius**2
    print("Area of Circle is : %0.2f " %area)

def area_rect(len, wid):
    'to calc area of rectangle'
    area = len*wid
    print("Area of rectangle is : %0.2f" %area)

class Book:
    'to define Book info'

    def __init__(self, BC, BT, BP):
        'to intiliaze book info'
        self.BCode = BC
        self.BTitle = BT
        self.BPrice = BP
    
    def getBInfo(self):
        print("B Code : %d" %self.BCode)
        print("B Title : %s" %self.BTitle)
        print("B Price : %0.2f Rs" %self.BPrice)

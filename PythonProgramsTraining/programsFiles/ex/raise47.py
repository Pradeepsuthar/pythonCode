import math
from datetime import datetime as dt

class NegativeValueError(RuntimeError):
    'to describe negative value error'
    def __init__(self, msg):
        'to initialize msg'
        self.MSG = msg
    
    def __str__(self):
        'to return an instance msg'
        return self.MSG

def get_tiles(area):
    'to find no of tiles to cover area'
    if area<0:
        # creating exception
        nve = NegativeValueError("kuchh to samjho, area kabhi bhi negative nahi hota hai")
        # raising an exception
        raise nve
    if area>=500:
        size = 9
    else:
        size = 4
    tiles = math.ceil(area/size)
    print("%d tiles required to cover %d area"%(tiles, area))

try:
    ar = int(input("Enter Area Size : "))
    # calling fun
    get_tiles( ar )
    get_tiles( 700 )
    get_tiles( -900 )
    print("everything in fine")
except Exception as ex:
    print( type(ex), " : ", ex,"\n", dt.now() )
print("All is Well")


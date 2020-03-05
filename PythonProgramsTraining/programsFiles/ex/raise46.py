# creating Exception class
class NegativeValueError(RuntimeError):
    'to represent negative value error'

    def __init__(self, msg):
        'to initialize a msg'
        self.msg = msg

    def __str__(self):
        return self.msg

def get_bill(units):
    'to calc electricity bill'
    if units<0:
        # creating exception
        nve=NegativeValueError("kabhi bhi units -ve nahi hoti hai")
        # raising an exception
        raise nve
    if units>=500:
        rate = 5.5
    else:
        rate = 3.5
    bill = units*rate*1.1
    print("Pay Bill is : %0.2f Rs" %bill)

try:
    units = int( input("Enter Units : ") )
    # calling fun
    get_bill(units)
    get_bill(-400)
    print("Everything is fine")
except Exception as ex:
    print( type(ex), " : ", ex)
print("All is well")




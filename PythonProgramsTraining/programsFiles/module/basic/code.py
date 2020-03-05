'to define some functions and variables'
import math

if __name__ == "__main__":
    print("u are executing code module directly")
    
def get_maintainance(size):
    'to calc monthly charge'
    if size>=1000:
        rate = 0.9
    else:
        rate = 1.1
    bill = size*rate*1.1
    return bill

def call_cost(duration, type):
    'to calc cost of call'
    # converting into mins
    mins = math.ceil(duration/60)
    if type.lower() == "isd":
        rate = 7.5
    else:
        rate = 1.5
    cost = mins*rate*1.1
    print("Call Cost is : %0.2f Rs" %cost)


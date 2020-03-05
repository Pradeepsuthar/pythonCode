import code        # importing module code
# importing specific attributes from bank module
from bank import ACT, withdraw, deposit
# importing all attributes from area module
from area import *

amt = code.get_maintainance(1500)
print("Monthly Charge : %0.2f Rs" %amt)
code.call_cost(190, "std")

print( ACT )
withdraw(4545, 10000)
deposit(4545, 15000)

area_circle(100)
area_rect(20, 10.5)
b1 = Book(1201, "python", 1050.50)
b1.getBookInfo()
# module info
print( code.__doc__ )
print( code.__file__ )
print( code.__name__ )
print( code.__package__ )
# returns list of attributes of given module
print( dir(code) )

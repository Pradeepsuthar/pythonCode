# importing basic module into main module
import basic
# importing specific attributes from bank module
from bank import ACT, withdraw, deposit
# importing all attributes from code module
from code import *

print( basic.MAX )
amt = basic.get_maintainance(1500)
print("Monthly Charge : %0.2f Rs" %amt)
basic.get_sum_digits("Gits@20$121$35, Raj")

print( ACT )
withdraw(2323, 10000)
deposit(2323, 5000)

area_circle(200)
area_rect(10, 15.5)
b1 = Book(1201, "Python", 450.90)
b1.getBInfo()
# getting module info
print( basic.__name__ )
print( basic.__file__ )
print( basic.__doc__ )
print( basic.__package__ )
# returns list of attributes in given module
print( dir(basic) )
print( __name__ )
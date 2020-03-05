# Operator
"""
city = ["Udaipur","Sirohi","Jaipur","Jodhpur","Kota"]

print(city)

ycity = input("Select your city : ")
if ycity in city:
	print("Your city is selected")
else:
	print("Your city is not selected")
	
"""
"""
a = 2
b = 4
print(a**b) # for find the power of values
print(a//b) # floar value/integer value

"""
# String
"""
str1 = 'Hello'
str2 = "Hello World"
str3 = '''Python is a 
programming language'''
str4 = '''Python is a 'programming language' '''
print(str1)
print(str2)
print(str3)
print(str4)

"""

# DMS
"""
print("\n----------Mobile Recharge----------\n")

mobile_no = input("Enter Mobile Number : ")
operator = input("Enter Mobile Operator : ")

print("\nMobile Number : ",mobile_no,"\nOperator : ",operator)

amt = int(input("\nAmount : "))

print("\nYour",operator,"Recharge Successful of Rs.%d"%amt)

"""
"""
b_salary = float(input("Enter Salary : "))
if b_salary >= 10000 : 
	ta = (10/100)*b_salary
	da = (15/100)*b_salary
	hra = (20/100)*b_salary
else:
	ta = (15/100)*b_salary
	da = (20/100)*b_salary
	hra = (30/100)*b_salary
	
total_amt = ta+da+hra
print("\nYour Basic Salary : ",b_salary)
print("\nT Amount : ",ta)
print("\nD Amount : ",da)
print("\nHr Amount : ",hra)
print("\nTotal Amount : ",total_amt)

"""
"""
print("Result")
marks1 = float(input("Enetr your 1st Subject Marks : "))
marks2 = float(input("Enetr your 2nd Subject Marks : "))
marks3 = float(input("Enetr your 3rd Subject Marks : "))

"""
"""
rd = int(input("Enetr your Racing Distance : "))

if rd >= 3000:
	rate = 3.5
	print("Platinum")
elif rd >= 2000:
	rate = 2.5
	print("Silver")
elif rd >= 1000:
	rate = 1.5
	print("Certificate")
else :
	print("Your are not selectd.Bettre luck next time...")

case_price = rd*rate
print("You will get case price : %0.2f"%case_price)

"""
# looping in python
# 1. for 	2. while

"""
1. for loop
for <iterative_variable> in <sequence> :
	statement1
        statement2
        statement3
else : 
      statement1
      statement2
      statement3   

where Sequence is range,list,string,dist,tuppel,set and iterative-objects etc.

2. while loop

initialization

while condition :
      statement1
      statement2
      statement3
	.
	.
	.
      statementn
else :     # this block is executed only if condition is false 
      statement1
      statement2
      statement3

"""
#practice

# range(r)/range(s,e) : predefine function whice is use to find range unti the given parameter

#print(range(5))

range(5)  #0, 1, 2, 3, 4
range(2,6)
range(4,19,3) # 4,7,10,13,16
range(50,9,-10) # 50,40,30,20,10
"""
for i in range(2,21,2):
	print(i)

print("\n")

for i in range(20,1,-2):
	print(i)

print("\n")

info = "pradeep"

for ch in info:
	print(ch,end="")

print("\n")


"""
"""
info = "pradeep"

for ch in info:
	if ch in "aeiouAEIOU":
	   print(ch,end="")
print("\n")
for ch in info:
	if ch not in "aeiouAEIOU":
	   print(ch,end="")
"""
"""
for item in range(200,19,-20):
	print(item)
else :
	print("Loop Complete")

"""

"""
text = "Hello081World@2019"
c=0
for i in text:
	if i in "0123456789":	
		c=c+1
else:
	print(c)

"""
"""
ch = 65
while ch<=90:
	print(chr(ch),end="\t")
	ch+=2
else:
 print("Thank you")
"""
"""
import math
x=1
while x<=5:
 no = float(input("Enter no. : "))
 if no >= 0:
  print("Sqrt is")
  sq=math.sqrt(no)
  print("SQRT of %0.2f is %0.2f"%(no,sq))  
  x+=1
 else:
  print("No. is -ve")
else:
 print("Done")	
"""         	


# Nested
"""
row = int(input("Enter row :"))

for r in range(0,row):
 c=1
 while c <=r:
  print(c, end="")
  c+=1
 else:
  print()

"""

# Loop Control statements
# 1. break	2. continue	3. pass

#break
"""
import random
while True:
	#return no. b/w 0.0 and 1.0
	no = int(random.random()*100)
	print(no)
	if no >= 90:
		break
else:
	print("Done")
"""

"""
str = input("Enter Text : ")
for ch in str:
	#convert into ASCII
	code = ord(ch)
	if code in range(48,58) or code in range(65,91) or code in range(97,123) or ch == " ":
		print(ch,end="")
	else:
		continue
else:
	print("\nDone")
"""

"""
i = 0
while i<= 30:
	i+=1	
	if i%7 != 0:
		continue
	print(i)
else:
	print("Done")

"""

"""
class Account:
	pass

if 40 in range(40,45):
	pass

"""

# string
"""
#String Special Operators
=	=> concatenation
*	=> Repetition
[]	=> slice/indexing
{:}	=> range
in	=> membership
not in	=> membership
r/R	=> Raw string
%	=> 

# String method

len(str)
str.index(obj)
str.isalnum()
str.isalpha()
str.isdigit()
str.isnummeric()
str.raplace()
str.islower()
str.isupper()
str.isspace()
str.capitalize()
str.swapcase()
str.count()
str.slipt()
"""

"""

str = "GITS, Raj $100"
#concatinates
print( str+"India" )
#repeatation
print("India "*5)
#Indexing
print(str[11])
print(str[-4])
print(str[4:11])
print(str[-11:-4])
print(str[3: ])
print(str[ :7])
print(str[-3:15])

if "city" in "Udaipur city":
	print("city Name")
#raw string
AcNo = 1230012
AcName = "Pradeep"
AcBal = 15000.90

str =r"Hello %s,\nu have bal\t%0.2f"\tRs. in Ac No.\t\t%d,\nGood\b\bRs."%(AcName, AcBal, AcNo)
print(str)
"""
'''
import random

for i in range(1000):
	code = random.randint(48,122)
	print(chr(code),end=" ")
	print("Upper case : ",code.isUpper())



# String method
'''
len(str)
str.index(obj)
str.isalnum()
str.isalpha()
str.isdigit()
str.isnummeric()
str.raplace()
str.islower()
str.isupper()
str.isspace()
str.capitalize()
str.swapcase()
str.count()
str.slipt()
'''
'''
method:str=object			function:math=modual
str.index()				math.sqrt()
'''

'''
#str method
info = "India $100 UDR @2019"

#return size of given str
print("Size of String :",len(info))
#return an index of given str
print("Index is:",info.index("$100"))
#retun no of occurances
print(info.count("0"))
#checking all chars are alphabates
print(info.isalpha())
#check all chars are spaces
print("  ".isspace())
#replaceing space with "-"
print(info.replace(" ","-")) 
#capitalize
print(info.islower())
print(info.isupper())
print(info.capitalize())
print(info.swapcase())
tokens = info.split("$")
print("Tokens of str :",tokens)



# Lists

1. The list is a most versatile datatype, which can be written as a list of comma-seprated various [items] b/w square breckets[].
2. it is a mutable object means flexible in runtime
<listName> = [item1,item2,item3,...]
price = [120,60,345]

# Built-in-functions
1. len(list)
2. max(list)
3. min(list)
4. list(seq)

# Methods
1. list.count(obj)
2. list.extend(seq)
3. list.index(obj)
4. list.insrt(index, obj)
5. list.pop(index)
6. list.remove(obj)
7. list.sort(obj)
8. list.reverse()

'''

# Tuples :
tup1 = ('apple','boy','cat')

# creating tuple to store marks

marks = (95, 86, 64, 57, 44, 99)
print(marks)

# iterate
print( marks[-5])
print( marks[2:6])
print( marks[-6:-3])
print( marks[4: ])
print( marks[ :-2])

# function
print( len(marks))
print( max(marks))
print( min(marks))
tp = tuple("Indea@2019")
print(tp)

# if a tuple has a mutable obj then u can change into that.


















































	
	
         	


























#string task
'''
str = input("Enter string : ")

alpha, digit, symbols, space = 0,0,0,0

for ch in str:
	if ch.isalpha():
		alpha+=1
	elif ch.isdigit():
		digit+=1
	elif ch.isspace():
		space+=1
	else:
		symbols+=1
else:
	print("Alphabates : %d \nDigits : %d \nSpaces : %d \nSymbols %d"\
%(alpha, digit, space, symbols))
	size = len(str)
	print("Size :",size)
	if symbols >= size*0.2:
		print("String is meanigful")
	else:
		print("String is not meaningful")

'''
'''
import random
print("Enter 20 time char : ")
for ch in range(1,21):
	print("Char :",ch,end=" : ")
	char = input()
	
	no = random.randint(65,90)
	gen_ch = chr(no)
	if ch == gen_ch:
		print("Winner")
		break
	else:
		print("Better luck next time")

'''

# List

'''
fruits = [1.5,2,3.5,1,2.25,4.5,2.5]
print( fruits )
'''

'''
dataList = [12001, "Pradeep", 30,000.00, "Udaipur", "i+j=10", "B", "Gits@2020", [1,2,3], ("A","B","C")]

for data in dataList:
	if type(data) in [int, float, complex]:
		print(data)
'''
'''
names = []
for i in range(5):
	n = input("Enter Name : ")
	names.append(n)
else:
	print(names)

# Searching

search = input("Enter name for search : ")
for name in names:
	temp_name = name.lower()
	if search in  temp_name:
		print(name) 

'''
'''
score = [10, 20, 30, 40, 50, 60, 50]

score.append(80)

#print(score)

#print(score.count(50))

extra=[22, 55]
score.extend(extra)
#print(score)

#print(score.index(30))

score.pop(3)
print(score)

score.reverse()
print(score)

score.sort(reverse=True)
print(score)

'''
'''
size_of_array = int(input("Enter size of the array : "))

array = []
print("Enter array elements : ")
for i in range(size_of_array):
	n = input()
	array.append(n)
else:
	print("Array is :",array)

# Sort array

sort = input("Do you want to sort this array (YES/NO) : ")

if sort == "yes" or sort == "YES":
	for element in array:
		print("Sort array in :-")
		print("1. Assending\t2. Disacending")
		choice = int(input())
		if choice == 1:
			array.sort()
			print("1. Assending :",array)
		else:
			array.sort(reverse=True)
			print("2. Disacending :",array)
			break
	else:
		print("Try agian")
else:
	print("Try Again")
					

'''
'''
account = []

for i in range(3):
	ac_no = int(input("Enter account no. : "))
	name = input("Enter name : ")
	bal = float(input("Enter balance :"))
	
	info = [ac_no, name, bal]
	account.append(info)
else:
	print("All accounts are created succesfully")
	print(account)

	print("\n1. Deposit\t2. Widthdraw")
	ac = int(input("Enter Account No. : "))
	for item in  account:
		if item == ac:
			print("Account no :",ac,"Account Holder Name :",name)
	

'''
'''

# creating tuple to mixed values

mix = (450, 25.5670, "Gits", "5j+3", 'UDP#01', 
      [120, "Android", 230.20],
      ('dehli', 2019), 1205, 
      {'EC101' : "Ganesh", 'EC102': "Pradeep"} )
mix[5][1] = "Google cloud"
mix[5].append(2500)
print(mix)

print("\nTuples list :\n")
for item in mix:
	print(item)
'''

'''
# functions in python : is define any task of reusibality

# Syntax
def <function>({arguments}):
    	"Function_doc_string"
	Function_suit
	return [expression]


# There are diffrent ways to call a function in python
# Types of function
1. Required args(positional order)
2. Keyword args(name of para)
3. Default args(default value)
4. Variable-length-arg

4. variable-length arg
def <function>(label,*tuple):
	'function_doc_string'
	function suite
	return [expression]


'''

#def fun():
#	print("Function is call")

#fun()


'''
def cost_and_mantainance(size):
	if size >=1000:
		rate = 2500
		mrate = 1.0
	else:
		rate = 2000
		mrate = 1.25
	cost = size*rate*1.15
	main_amt = size*mrate*1.1
	print("Cost is : %0.2f Rs. with monthly charge is : %0.2f Rs."\
		%(cost,main_amt))


size = int(input("Enter Size of House : "))
cost_and_mantainance(size)

'''
'''
info = [8440077147,"Pradeep",5000]

def deposit(ls,amt):
	if amt >= 500:
		ls[2] += amt
		print("Money Deposit successfuly")
		print("Current Balance is : Rs.%0.2f"%(ls[2]))
	else:
		print("Insufficient Balance your curent Balance is Rs.%0.2f"%(ls[2]))


def withdraw(ls, amt):
	if ls[2] >= amt:
		ls[2] -= amt
		print("Money withdraw successfuly")
		print("Current Balance is : Rs.%0.2f"%(ls[2]))
	else:
		print("Insufficient Balance your curent Balance is Rs.%0.2f"%(ls[2]))



deposit(info,500)
withdraw(info,500)

'''

def loan_el_amt(salary, bonus, fd):
	if salary >= 20000:
		loan = salary*6
	else:
		loan += bonus*4
	if bonus>=10000:
		loan += bonus*3
	else:
		loan += fd*0.5
		return loan

amt = loan_el_amt(25000, 9000, 70000)
print("Loan upto %0.2f Rs."%(amt))


amt = loan_el_amt(salary=25000, fd=100000, bonus=5000)
print("Loan upto %0.2f Rs."%(amt))





























 





















































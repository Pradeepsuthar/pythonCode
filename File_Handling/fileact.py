'''
FILE_NAME = "actinfo.txt"

def add_act_info():
	'to add new account into file'
	an = input("Enter Account No. : ")
	ahn = input("Enter Account Holder Name : ")
	pin = input("Enter Pin No. : ")
	ab = input("Enter Balance : ")

	# Open file in append mode
	writer = open(FILE_NAME,"a")
	writer.write(an+"\t"+ab+"\t"+pin+"\t"+ahn+"\n")
	writer.close()
	print("Act info writen into file")

def read_act_info():
	'to read all act info'
	# opening file in reading mode
	reader = open(FILE_NAME,"r")
	# reading all lines and return list
	lines = reader.readlines()
	for line in lines:
		print(line, end="")
	else:
		reader.close()

#for i in range(4):
#	add_act_info()

read_act_info()
'''

# JSON is syntax less format for storing and exachnig data b\w 2 resources
# such as client and server

# Key must be uniq and string.
# string can be denoted only  "string_name". 
# data can be in any combination of JSON array and JOSN Objects.
# JSON is predefine module to provieds functions to process JSON data.

'''
File : empinfo.json
[
	{"ECode": 1234,"EName": "Pradeep","ESal":20000.50},
	{"ECode": 4568,"EName": "Raj","ESal":25000.50}
]

'''
import json

FILE_NAME = "empinfo.json"

def read_emp_info():
	'to read all employee info from json file'
	# openig file in read mode
	fr = open(FILE_NAME)
	# reading all data from json file info python compative
	info = json.load(fr)
	fr.close()
	for item in  info:
		print("%d\t%s\t%0.2f"%(item["ECode"],item["EName"],item["ESal"]))

def add_emp_info():
	'to add new emp detail'
	fr = open(FILE_NAME)
	info = json.load(fr)
	fr.close()
	ec = int(input("Enter Emp code : "))
	en = input("Enter Emp Name : ")
	es = float(input("Enter salary : "))
	# CREATING DICT
	data = {'ECode': ec,'EName': en, 'ESal':es}
	info.append(data)
	# appending data in info list
	fw = open(FILE_NAME,"w")
	# dumping list into json file
	json.dump(info,fw)
	fw.close()
	print("\nEmp info Saved\n")


# calling function
read_emp_info()
add_emp_info()
read_emp_info()































import json

FILE_NAME = "empdata.json"

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

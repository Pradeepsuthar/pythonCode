import json
FILE_NAME = "emp46.json"

def read_emp_info():
    'to read emp detail'
    fr = open(FILE_NAME)
    # reading all data of json file
    data = json.load(fr)
    for item in data:
        print("%d\t%s\t%0.2f" %(item["EC"], item["EN"], item["ES"]))
    fr.close()

def add_emp_info():
    'to add new emp detail'
    fr = open(FILE_NAME)
    data = json.load(fr)
    fr.close()
    ec = int(input("Enter E Code : "))
    en = input("Enter E Name : ")
    es = float( input("Enter E Salary : ") )
    # creating dict to parse into JSON Object
    info = {'EC':ec, 'EN':en, 'ES':es}
    # adding/appending into list
    data.append( info )
    # opening file in write mode
    fw = open(FILE_NAME, "w")
    # dumping list(data) into JSON File
    json.dump(data, fw)
    fw.close()
# calling fun
add_emp_info()
read_emp_info()

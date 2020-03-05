import json
EMP_FILE = "empinfo.json"

def read_emp_info():
    'to read all employee info from json file'
    # opening json file in reading mode
    fr = open(EMP_FILE)
    # reading all data from json file into python compatible
    info = json.load(fr)
    fr.close()
    for item in info:
        print("%d\t%s\t%0.2f"%(item["ECode"], item["EName"], item["ESal"]))

def add_emp_info():
    'to add new emp detail'
    fr = open(EMP_FILE)
    info = json.load(fr)
    fr.close()
    ec = int( input("Enter Emp Code : "))
    en = input("Enter Emp Name : ")
    es = float( input("Enter Emp Salary : "))
    # creating dict
    data = {'ECode':ec, 'EName':en, 'ESal':es}
    # appending into list
    info.append(  data )
    # opening file in write mode
    fw = open(EMP_FILE, "w")
    # dumping list into json file
    json.dump(info, fw)
    fw.close()
    print("Emp Info saved")

# calling fun
read_emp_info()
add_emp_info()
read_emp_info()
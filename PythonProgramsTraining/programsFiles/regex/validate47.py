import re

# creating compiled regex for vehicle no
reVNo = re.compile('^(R|G)J\d{2}[A-Z]{2}\d{4}$', re.I)
for i in range(7):
    vno = input("Enter Vehicle No : ")
    # replacing spaces with blank
    vno = re.sub('\s', "", vno)
    print( vno )
    rs = reVNo.match( vno )
    if rs:
        print("Valid")
    else:
        print("Invalid")

# creating regex for roll no
reRollNo = re.compile('^(CS|IT)1[4-7]\d{3,4}$', re.I)

for i in range(7):
    rs = reRollNo.match( input("Enter Roll No : ") )
    if rs:
        print("Valid Roll No ")
    else:
        print("Invalid Roll No ")


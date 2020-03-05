import re

creating regex to validate roll no
reRollNo = re.compile("^(CS|IT)1[4-7]\d{3,4}$", re.I)

for i in range(7):
    # matching/validate roll no
    rs = reRollNo.match(input("Enter Roll No : "))
    if rs:
        print("Valid")
    else:
        print("Invalid")
# creating regex for vehicle no
reVNo = re.compile("^(G|R)J\d{2}[A-Z]{2}\d{4}$", re.I)

for i in range(7):
    vno = input("Enter Vehicle No : ")
    # replacing spaces with blank
    vno = re.sub(" ", "", vno)
    rs = reVNo.match( vno )
    if rs:
        print("Valid")
    else:
        print("Invalid")
        
import re

str = "the Cs15003 and cs15451 are topper but CS14601 has 2nd"
# matching from starting
rs = re.match('CS[0-9]{5}', str, re.I)
if rs:
    print( rs.group() )
else:
    print("Match not found")
# searching from anywhere in given input
rs = re.search("CS[0-9]{5}", str, re.I)
if rs:
    print( rs.group() )
else:
    print("Search not found")

mob = input("Enter Mobile No : ")
# validating mobile no
rs = re.match('^\d{10}$', mob)
if rs:
    print( rs.group(), "\tvalid")
else:
    print("Invalid mobile no")


import re

str = "APT/17/1151 ref no assigned to palak \
    but apt/19/2062 is vacant, Also apt/20/34567 is not valid"

# matching from starting char
rs = re.match('APT/[0-9]{2}/\d{4}', str, re.I)
if rs:
    print( rs.group() )
else:
    print("Match not found")

# searching from anywhere in the given string
rs = re.search('APT/[0-9]{2}/\d{4}', str, re.I)
if rs:
    print( rs.group() )
else:
    print("Search not found")

# creating compiled regex for ref No
reRefNo = re.compile('^APT[/-][01][1-9][/-]\d{4}$', re.I)
for i in range(10):
    # exact matching
    refNo = input("Enter Reference No : ")
    # matching/validate Ref No
    rs = reRefNo.match( refNo )
    if rs:
        print("Valid")
    else:
        print("Invalid")





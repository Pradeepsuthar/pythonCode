import re

str = "APT/17/1151 ref no is asssigned to pradeep\
    but apt/19/2034 is assigned to raj, also apt/20/43234 is not valid"

#matching from starting char
rs = re.match('APT/[0-9]{2}/\d{4}',str, re.I)

if rs:
    print(rs.group())
else:
    print("Match not found")


#creating compiled regex for refno
reRefno = re.compile('^APT[/-][01][0-9][/-]\d{4}$',re.I)
for i in range(5):
    refno = input("Enter ref no:")

    rs = reRefno.match(refno)
    if rs:
        print("Valid")
    else:
        print("Invalid")
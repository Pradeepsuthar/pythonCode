import re

rerollno = re.compile('^(CS|IT)1[4-7]\d{3,4}$',re.I)

for i in range(5):
    rs = rerollno.match(input("Enter roll No. "))
    if rs:
        print("Valid ")
    else:
        print("Invalid")
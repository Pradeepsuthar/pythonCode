import re       # importing regex module

regex = "[0-9][abcd]pur"
str = "6dpur and 5apur are near but 7epur is far from 3cpur."
# returns list of all matching tokens
tokens = re.findall(regex, str)
print( tokens )

reNo = re.compile("[0-9]+")
txt = "Gits since@1998 and 90 percent placement and 52540 Rs\
     avg salary. total 5 degrees and 2020 will be best, \
         finally 101"
# extracting all numbers from given str
numbers = reNo.findall(txt)
print( numbers )
# creating regex for roll no
reRollNo = re.compile("CS17\d{3}", re.I)
msg="cs17405 and Cs17505 are winner but \
    CS17670 and cs17324 are failure but CS19887 is not valid"
# extracting all roll no from given string
roll = reRollNo.findall(msg)
print( roll )

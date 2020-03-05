import re   # importing regex module

regex = "[0-9][abcd]pur"
str = "4epur and 7bpur are near but 3dpur is far from 4bpur"
# returns list of matching tokens
tokens = re.findall(regex, str)
print( tokens )

txt = "CS15905 and cs17109 are topper \
    but cS1645655 is third CS194595 is last"
# extracting all roll no
rollno = re.findall('CS1[4-7]\d{3,5}', txt, re.I)
print( rollno )

info = "2019 was good but i hope that 2020 will be better.\
    5rs wallet balance i need to trandfer 12345.65 Rs as EMI.\
        45Rs for notebook. 5670.56 Rs for mobile. \
        finally 142 students are placed"
# extracting all numbers from given str
numbers = re.findall('\d+[.]?\d*', info)
print( numbers )





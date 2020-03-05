import re

regex = "[0-9][abcd]pur"
str = "4epur and 7bpur are near but 4dpur is far from 4bpur"
# retrun list  of matching tokens 
tokens = re.findall(regex, str)
print(tokens)

txt = "CS15905 and cS171905 are topper \
    but cs1645654 is third cs19458 is last"

rollno = re.findall('CS1[4-7]\d{3,5}',txt,re.I)
print( rollno )

info = "2019 was good nut 2020 will be better .\
    5rs wallet balance i need to transfer 12345.65 EMI \
        rs45 for note book 5670.65 Rs for mobile.\
            finally 234 student placed"

number = re.findall('\d+[.]?\d*',info)
print( number )
import re

str = "2019 was good but i hope that \
    2020    will be better but i need 2020200 Rs in 2020\
        i learnt python in 2019 but want to learn ML in 2020\
            with Fees of 20200 Rs"
print(str)
str1 = re.sub("\s+2020|2020\s+", '2021 ', str)
print(str1)

str2 = re.sub('\s+20\d{2}|20{2}\s+', "____", str)
print( str2 )
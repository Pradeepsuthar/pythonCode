import re

regex = "[0-9][abcd]pur"
str = "4epur and 7bpur are near but 4dpur is far from 4bpur"
# retrun list  of matching tokens 
tokens = re.findall(regex, str)
print(tokens)
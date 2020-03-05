import re
# creating regex for soldier code
reSC = re.compile("1[6-9][A-Z]{2}\d{4}", re.I)
# opening file in read mode
fr = open("secret.txt")
data = fr.read()
fr.close()
# extracting all soldier codes from file data
codes = reSC.findall( data )
print( codes )

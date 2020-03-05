# creating dict to store emp detail
emp={'GITS1101':12500.90, "GITS1105":35600, "GITS1103":25300}
print( emp )
# iterate dict
for item in emp:
    print( item, " : ", emp[item] )
# adding new item
emp['GITS1104'] = 15600
print( emp )
# update an item
emp["GITS1101"] = 17500
print( emp )
# delete an item
del emp["GITS1103"]
print( emp )
# returns size of given dict
print( len(emp) )
info = str( emp )
print( type(info) )
print( info )


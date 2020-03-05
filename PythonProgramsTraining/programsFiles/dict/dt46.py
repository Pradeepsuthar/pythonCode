# creating dict to store student marks with roll no
marks = {'CS1901':55, "CS1904":86.5, 'CS1903':66}
print( marks )
# iterate dict
for item in marks:
    print( item, " : ", marks[item] )
# adding new item
marks["CS1905"] = 72.5
print( marks )
# update an item
marks['CS1901'] = 47
print( marks )
# delete an item
del marks["CS1903"]
print( marks )
# search value by key
print( marks["CS1905"] )
# returns size of dict
print( len(marks) )
# returns str 
info = str( marks )
print( info )
print( type(info) )




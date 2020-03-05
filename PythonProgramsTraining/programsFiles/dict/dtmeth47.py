# creating dict to store book detail
books = {'PE1201':450.90, 'PE1204':670.50, 'PE1202':1040.90}
# returns a copy of dict
info = books.copy()
print( info )
print( books.fromkeys("INDIA$50", 25) )
ecode = [22001, 22005, 2209, 22010]
# returns dict by extracting/iterating given sequence with default value
print( books.fromkeys(ecode, 1100) )
# returns a value of given key
print( books.get('PE1204') )
# returns list of tuple(key, value)
print( books.items() )
# returns list of keys
print( books.keys() )
# returns list of values
print( books.values() )
# add new item if key is not available
books.setdefault('PE1205', 1150.50)
print( books )
# merging into books dict
books.update( {'PE1206':450.90, 'PE1209':1450.50} )
print( books )
# clearing data of dict
books.clear()
print( books )

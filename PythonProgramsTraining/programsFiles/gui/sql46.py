import mysql.connector
# connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="aptech",
    database="gits46")
if mydb:
    print("DB Connected")
else:
    print("DB did not connected")
# create cursor
cursor = mydb.cursor()
ec=input("Enter E Code : ")
en=input("Enter E Name : ")
es=input("Enter E Salary : ")
ed=input("Enter E DOB : ")
ecity=input("Enter E City : ")
sql="insert into empmaster values\
    ("+ec+", '"+en+"', "+es+",'"+ed+"', '"+ecity+"')"
cursor.execute(sql)
mydb.commit()

if cursor.rowcount>0:
    print("Data Inserted")
else:
    print("Data did not inserted")

# retrieve all data from database
sql = "select * from empmaster"
# accessing data into cursor
cursor.execute(sql)
# fetching all rows into result
result = cursor.fetchall()
for item in result:
    print( item )
# closing connection
cursor.close()
mydb.close()

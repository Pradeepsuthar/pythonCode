import mysql.connector

# connect to db
con = mysql.connector.connect(host="localhost",port="3306",
user="root",passwd="aptech", database="gits47")
if con:
    print("DB Connected")
else:
    print("DB not connected")
# create cursor to carry SQL
cursor = con.cursor()
no = input("Enter Ac No : ")
name = input("Enter Ac Name : ")
bal = input("Enter Ac Balance : ")
dt = input("Enter Ac Date of Act : ")
city = input("Enter City : ")
sql="insert into accountmaster \
    values("+no+",'"+name+"',"+bal+",'"+dt+"','"+city+"');"
cursor.execute(sql)
# commiting SQL
con.commit()
if cursor.rowcount>0:
    print("Data Inserted")
else:
    print("Data did not inserted")
# retrieve data from db
sql="select * from accountmaster;"
cursor.execute(sql)
# fetching all records
result = cursor.fetchall()
for item in result:
    print( item )
# closing cursor & con
cursor.close()
con.close()

import mysql.connector

# connect to db
con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="",database="gits079")
if con:
    print("DB Connected")
else:
    print("DB Not Connected")

# Create cursor to carry sql
cursor = con.cursor()
no = input("Enter Ac No. : ")
name = input("Enter Ac Holder Name : ")
bal = input("Enter Balance : ")
date = input("Enter Ac Date of Act : ")
city = input("Enter City Name : ")

sql = "insert into accountmaster values("+no+",'"+name+"',"+bal+",'"+date+"','"+city+"');"
cursor.execute(sql)
#commiting sql
con.commit()

if cursor.rowcount>0:
    print("Data inserted")
else:
    print("Data Not inserted")

# Retrieve data from db
sql = "selecct * from accountmaster;"
cursor.execute(sql)

# fetching all records
result = cursor.fetchall()
for item in result:
    print(item)
# closing cursor and connection
cursor.close()
con.close()
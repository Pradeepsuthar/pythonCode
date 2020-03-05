import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  passwd="aptech",
  database="gits46")

mycursor = mydb.cursor()
# sql = "insert into empmaster values(12003, 'Palak Sharma', 45600.50, '1995-04-15')"
# mycursor.execute(sql)
# mydb.commit()
print( mycursor.rowcount )
mycursor.execute("select * from empmaster;")
record = mycursor.fetchall()
for item in record:
  print( item[0] )
mydb.close()
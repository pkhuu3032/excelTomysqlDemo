import mysql.connector
import xlrd

db1=mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="1234qwer",
  database ="testdb"
  )

#mycursor.execute("create table personInfo(Name varchar(30),Age smallint unsigned,Color varchar(15),Sport varchar(15),Gender varchar(1),personID int PRIMARY KEY AUTO_INCREMENT)")

mycursor=db1.cursor()
mylist=list()
a=xlrd.open_workbook("Book1.xls")
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,15):
  #print(tuple(sheet.row_values(i)))
  mylist.append(tuple(sheet.row_values(i)))

q="insert into personinfo(Name,Age,Color,Sport,Gender)values(%s,%s,%s,%s,%s)"
mycursor.executemany(q,mylist)

db1.commit()
db1.close()




'''
mycursor=db1.cursor()

mycursor.execute("CREATE TABLE person(name VARCHAR(50),age smallint UNSIGNED,color VARCHAR(25),sport VARCHAR(25),gender VARCHAR(1),personID int PRIMARY KEY AUTO_INCREMENT)")

mycursor.execute("SELECT * FROM testdb.person")

for x in mycursor:
  print(x)

mycursor.close()  '''
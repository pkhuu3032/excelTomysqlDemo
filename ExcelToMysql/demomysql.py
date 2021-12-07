import mysql.connector
import xlrd #excel should save as "Excel 97-2003 workbook" for this to work and not the default setting

db1=mysql.connector.connect(
  host ="localhost",
  user ="############",  #This is the mysql server username
  passwd ="###################", #This is the mysql server password
  database ="#################"  #This is the database name  
  )

#if database doesn't have a tabe yet (use code down below, this can only work once and can't run again)
#mycursor.execute("create table personInfo(Name varchar(30),Age smallint unsigned,Color varchar(15),Sport varchar(15),Gender varchar(1),personID int PRIMARY KEY AUTO_INCREMENT)")


mycursor=db1.cursor()
mylist=list()
#if the file is in the same directory/folder as this ".py" file than enter the file name with ".xls"
#but if it is not in the same folder than you'll have to enter the file path in the parenthesis
#example: open_workbook("C:\\Users\\YourPcName\\Desktop\\Some_Folder\\SomeExcelFileName.xls") 
a=xlrd.open_workbook("Book1.xls")   
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
#Range can be change when data get bigger
for i in range(1,15):
  #print(tuple(sheet.row_values(i)))
  mylist.append(tuple(sheet.row_values(i)))

q="insert into personinfo(Name,Age,Color,Sport,Gender)values(%s,%s,%s,%s,%s)"
mycursor.executemany(q,mylist)

db1.commit() #This is where the data get uploaded to the server and make changes on the server
db1.close()















'''
mycursor=db1.cursor()

mycursor.execute("CREATE TABLE person(name VARCHAR(50),age smallint UNSIGNED,color VARCHAR(25),sport VARCHAR(25),gender VARCHAR(1),personID int PRIMARY KEY AUTO_INCREMENT)")

mycursor.execute("SELECT * FROM testdb.person")

for x in mycursor:
  print(x)

mycursor.close()  '''

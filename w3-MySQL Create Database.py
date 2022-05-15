#https://www.w3schools.com/python/python_mysql_create_db.asp
#Python MySQL Create Database 創建資料庫
#Creating a Database 創建資料庫
#To create a database in MySQL, use the "CREATE DATABASE" statement:
#要在 MySQL 中建立資料庫，請使用「創建資料庫」語句：
#create a database named "mydatabase":
print("----------------------建立名為「我的資料庫」的資料庫")
#建立名為「我的資料庫1」的資料庫：

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase1")


#If the above code was executed with no errors, you have successfully created a database.
#如果執行上述代碼時沒有錯誤，則您已成功創建資料庫。

#Check if Database Exists 檢查資料庫是否存在
#You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:
#您可以使用「顯示資料庫」語句列出系統中的所有資料庫，從而檢查資料庫是否存在：
print("------------------------------返回系統資料庫清單")
#Return a list of your system's databases:
#返回系統資料庫清單
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
#SHOW DATABASES,返回系統資料庫清單
#Or you can try to access the database when making the connection:
#或者，您可以嘗試在進行連接時存取資料庫：

print("--------------或者，您可以嘗試在進行連接時存取資料庫")
#Try connecting to the database "mydatabase":
#或者，您可以嘗試在進行連接時存取資料庫：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
#host="localhost",主機=本地主機
#user="cuter0616",使用者=使用者名稱
#password="Billchen19750616",密碼=
#database="mydatabase"資料庫=資料庫名
#If the database does not exist, you will get an error.
#如果資料庫不存在，您將遇到錯誤。


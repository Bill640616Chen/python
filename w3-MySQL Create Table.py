#https://www.w3schools.com/python/python_mysql_create_table.asp
#Python MySQL Create Table 創建表
#Creating a Table 創建表
#To create a table in MySQL, use the "CREATE TABLE" statement.
#要在 MySQL 中建立表，請使用「創建表」語句。
#Make sure you define the name of the database when you create the connection
#創建連接時，請確保定義資料庫的名稱
#Create a table named "customers":
#建立名為「客戶」的表：
'''
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
'''
#()內是mysql的語法,VARCHAR 的最大長度為65535 Bytes
#cursor()游標只能用於儲存過程和函數,游標的使用，主要包括游標的宣告、開啟、使用和關閉
#If the above code was executed with no errors, you have now successfully created a table.
#如果執行上述代碼時沒有錯誤，則您現在已成功創建了一個表。
#Check if Table Exists 檢查表是否存在
#You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:
#您可以使用「顯示表」聲明列出資料庫中的所有表，從而檢查表是否存在：
#Return a list of your system's databases:
#傳回系統資料庫清單：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
#SHOW TABLES,在檔案顯示表

#Primary Key 主鍵
#When creating a table, you should also create a column with a unique key for each record.
#建立表時，您還應創建一個欄，其中每個記錄都有一個唯一的密鑰。
#This can be done by defining a PRIMARY KEY.
#這可以通過定義主金鑰來完成。
#We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.
#我們使用"INT AUTO_INCREMENT(自動增量)初級密鑰"的陳述，該聲明將為每個記錄插入一個唯一的號碼。從 1 開始，每次記錄增加一個。
#Create primary key when creating the table:
#建立表時建立主金鑰：
'''
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
'''
#If the table already exists, use the ALTER TABLE keyword:
#如果表已經存在，請使用 ALTER 表關鍵字：
#Create primary key on an existing table:
#在現有表上建立主金鑰：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#更改表,在custonmers table 增加欄位id自動增加主鑰匙)
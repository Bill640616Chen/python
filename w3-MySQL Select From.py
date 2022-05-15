#https://www.w3schools.com/python/python_mysql_select.asp
#Python MySQL Select From 創建表
#Select From a Table 從表中選擇
#To select from a table in MySQL, use the "SELECT" statement:
#要從 MySQL 中的表中進行選擇，請使用「選擇」語句：
#Select all records from the "customers" table, and display the result:
#從「客戶」表中選擇所有記錄，並顯示結果：
#Select all records from the "customers" table, and display the result:
#從「客戶」表中選擇所有記錄，並顯示結果：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
#cursor()游標只能用於儲存過程和函數,游標的使用，主要包括游標的宣告、開啟、使用和關閉
mycursor.execute("SELECT * FROM customers")
#從customers
myresult = mycursor.fetchall()
#fetchall()與對象相關的結果集中提取所有列到陣列中,fetch獲取
for x in myresult:
  print(x)
#Note: We use the fetchall() method, which fetches all rows from the last executed statement.
#注意：我們使用獲取全部（）方法，該方法從上次執行的語句中獲取所有行。

print("-------------------------Selecting Columns 選擇欄")
#Selecting Columns 選擇欄
#To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):
#要僅選擇表中的某些列，請使用列名後面的「SELECT」語句：
#Select only the name and address columns:
#只選擇名稱與位址欄：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("--------------------fetchone() Method 獲取一個()方法")
#Using the fetchone() Method 獲取一個()方法
#If you are only interested in one row, you can use the fetchone() method.
#如果您只對一行感興趣，則可以使用fetchone獲取一個()方法。
#The fetchone() method will return the first row of the result:
#fetchone()方法將返回結果的第一行：
#Fetch only one row:
#只取得一行：資料的第一行
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
#*,任何資料
myresult = mycursor.fetchone()
print(myresult)
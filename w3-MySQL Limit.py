#https://www.w3schools.com/python/python_mysql_limit.asp
#Python MySQL Limit 限制
#Limit the Result 限制結果
#You can limit the number of records returned from the query, by using the "LIMIT" statement:
#您可以使用「限制」語句限制從查詢中傳回的記錄數量：
#Select the 5 first records in the "customers" table:
#在「客戶」表中選擇 5 個首記錄：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#查詢前五筆記錄

print("---------OFFSET從第三筆開始,數五筆--從另一個位置開始")
#Start From Another Position 從另一個位置開始
#If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:
#如果您想返回五個記錄，從第三個記錄開始，您可以使用「偏移」關鍵字：
#Start from position 3, and return 5 records:
#從第 3 位開始，返回 5 個記錄：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#OFFSET從第三筆開始,數五筆
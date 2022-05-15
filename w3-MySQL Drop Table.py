#https://www.w3schools.com/python/python_mysql_drop_table.asp
#Python MySQL Drop Table 卸除表
#Delete a Table 刪除表
#You can delete an existing table by using the "DROP TABLE" statement:
#您可以使用「DROP 表」語句刪除現有表：
#Delete the table "customers":
#刪除表「客戶」
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)

#Drop Only if Exist 僅在存在時刪除
#If the the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword to avoid getting an error.
#如果要刪除的表已刪除，或者由於任何其他原因不存在，您可以使用 IF 存在關鍵字以避免出錯。
#Delete the table "customers" if it exists:
#如果存在「客戶」表，請將其刪除：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
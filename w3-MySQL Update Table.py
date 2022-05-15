#https://www.w3schools.com/python/python_mysql_update.asp
#Python MySQL Update Table 修改表
#Update Table修改表
#You can update existing records in a table by using the "UPDATE" statement:
#您可以使用「UPDATE」語句更新表中的現有記錄：
#Overwrite the address column from "Valley 345" to "Canyoun 123":
#覆蓋位址欄從把「Valley 345」改為「Canyoun 123」：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
#重要！： 請注意聲明： mydb.commit()。需要更改，否則不會更改表。
#Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies which record or records that should be updated. If you omit the WHERE clause, all records will be updated!
#請注意更新語法中的「哪裡」條款：「更新」條款指定了應更新的記錄或記錄。如果您省略了「哪裡」條款，則將更新所有記錄！

#Prevent SQL Injection 防止 SQL 注入
#It is considered a good practice to escape the values of any query, also in update statements.
#在更新報表中，逃避任何查詢的值被認為是一種好的做法。
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#這是為了防止 SQL 注入，這是一種常見的網路駭客技術，以破壞或濫用您的資料庫。
#The mysql.connector module uses the placeholder %s to escape values in the delete statement:
#mysql.connector 模組使用佔位符 %s 來逃避刪除語句中的值：
#Escape values by using the placholder %s method:
#使用柏拉圖%的方法逃生值：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
#為了防止注入,就多了一個變數?
#(UPADTE,WHERE),%s="Valley 345", "Canyon 123"
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
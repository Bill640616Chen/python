#https://www.w3schools.com/python/python_mysql_delete.asp
#Python MySQL Delete From By 從哪刪除
#Delete Record 刪除記錄
#You can delete records from an existing table by using the "DELETE FROM" statement:
#您可以使用「從」語句中移除現有表中的記錄：
#Delete any record where the address is "Mountain 21":
#刪除位址為「Mountain 21」的任何記錄：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
#mycursor.rowcount,計算幾列被刪除
#commit()確認交易，在交易結束時確認交易，在確認時資料才會真的寫入資料表。
#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
#重要！： 請注意聲明： mydb.commit()。需要更改，否則不會更改表。
#Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s) that should be deleted. If you omit the WHERE clause, all records will be deleted!
#請注意刪除語法中的「在哪裡」條款：「刪除」條款指定應刪除的記錄。"請注意"其中的條款"。如果您省略了「哪裡」條款，所有記錄將被刪除！

print("--------------------------------------防止 SQL 注入")
#Prevent SQL Injection 防止 SQL 注入
#It is considered a good practice to escape the values of any query, also in delete statements.
#在刪除語句中，逃避任何查詢的值被認為是一種好的做法。
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#這是為了防止 SQL 注射，這是一種常見的網路駭客技術，以破壞或濫用您的資料庫。
#The mysql.connector module uses the placeholder %s to escape values in the delete statement:
#mysql.connector 模組使用佔位符 %s 來逃避刪除語句中的值：
#Escape values by using the placeholder %s method:
#使用佔位元 %s 方法逃逸值：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
#為了防止注入,就多了一個變數?
#(DELETE FROM, ),%s=Yellow Garden 2
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
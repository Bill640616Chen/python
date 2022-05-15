#https://www.w3schools.com/python/python_mysql_orderby.asp
#Python MySQL Order By 按順序排列
#Use the ORDER BY statement to sort the result in ascending or descending order.
#使用訂單按語句對升序或降序的結果進行排序。
#The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.
#按關鍵字排列的訂單預設會對結果進行排序。要按降序對結果進行排序，請使用 DESC 關鍵字。
#Sort the result alphabetically by name: result:
#按名稱按字母順序對結果進行排序：結果：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"
#按name排序,以字母第一佪排序
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("------------------------------------降序(DESC)排序")
#ORDER BY DESC DESC 降序(DESC)排序
#Use the DESC keyword to sort the result in a descending order.
#使用 DESC 關鍵字按降序對結果進行排序。
#Sort the result reverse alphabetically by name:
#依名稱按字母順序對結果進行排序：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
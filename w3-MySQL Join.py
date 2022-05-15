#https://www.w3schools.com/python/python_mysql_join.asp
#Python MySQL Join 連接
#Join Two or More Tables 加入兩個或多個表
#You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.
#您可以使用 JOIN 語句，根據兩個或兩個以上表之間的相關欄組合。
#Consider you have a "users" table and a "products" table:
#考慮您有一個「用戶」表和一個「產品」表：
'''
users
{ id: 1, name: 'John', fav: 154},
{ id: 2, name: 'Peter', fav: 154},
{ id: 3, name: 'Amy', fav: 155},
{ id: 4, name: 'Hannah', fav:},
{ id: 5, name: 'Michael', fav:}
products
{ id: 154, name: 'Chocolate Heaven' },
{ id: 155, name: 'Tasty Lemons' },
{ id: 156, name: 'Vanilla Dreams' }
'''
#These two tables can be combined by using users' fav field and products' id field.
#這兩個表可以通過使用使用者的 fav 字段和產品的id欄位進行組合。
#Join users and products to see the name of the users favorite product:
#加入使用者和產品，查看使用者喜愛的產品的名稱：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="mypassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
'''
mycursor.execute("CREATE TABLE users (name VARCHAR(255), fav VARCHAR(255))")
#為了做一個表users,設定欄名稱及輸入的字元長度
mycursor.execute("CREATE TABLE products (fav VARCHAR(255), id VARCHAR(255)))")
#為了做一個表products,設定欄名稱及輸入的字元長度
mycursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#設定id
mycursor.execute("ALTER TABLE products ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#設定id
#從這裡開始要增加表的內容到61行
#註解掉,是避免一直新增
sql1 = "INSERT INTO users (name, fav) value (%s, %s)"
val1 = [
    ('John', 154),
    ('Peter', 154),
    ('Amy', 155),
    ('Hannah',0 ),
    ('Michael',0)
]
mycursor.executemany(sql1, val1)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
sql2 = "INSERT INTO products (fav,id) value (%s, %s)"
val2 = [
    ('Chocolate Heaven',154),
    ('Tasty Lemons',155),
    ('Vanilla Dreams',156)
]
mycursor.executemany(sql2, val2)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
'''
sql = "SELECT \
  users.name AS user, \
  products.fav AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#出現Access denied for user 'yourusername'@'localhost' (using password: YES)
#錯誤訊息後,yourusername的帳號全部刪掉,重做一個一樣的帳號
#然後主機名稱要選本機,會出現localhost
#Note: You can use JOIN instead of INNER JOIN. They will both give you the same result.
#注意：您可以使用加入而不是內部加入。他們都會給你相同的結果。

print("----------------------------------LEFT JOIN 左加入")
#LEFT JOIN 左加入
#In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.
#在上面的例子中，Hannah和Michael被排除在結果之外，這是因為內聯只顯示有匹配的記錄。
#If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:
#如果您想向所有使用者顯示，即使他們沒有最喜歡的產品，請使用左聯播語句：
#Select all users and their favorite product:
#選擇所有使用者及其喜愛的產品：
sql = "SELECT \
  users.name AS user, \
  products.fav AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("----------------------------------RIGHT JOIN 右加入")
#RIGHT JOIN 右加入
#If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:
#如果您想要退回所有產品，並且使用者將它們作為他們的最愛，即使沒有使用者將它們作為他們的最愛，請使用 RIGHT JOIN 語句：
#Select all products, and the user(s) who have them as their favorite:
#選擇所有產品，以及使用者誰有他們最喜歡的：
sql = "SELECT \
  users.name AS user, \
  products.fav AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#(None, 'Vanilla Dreams')自動補上name=None,沒人喜歡Vanilla Dreams
#Note: Hannah and Michael, who have no favorite product, are not included in the result.
#注意：漢娜和邁克爾，誰沒有最喜歡的產品，不包括在結果中。

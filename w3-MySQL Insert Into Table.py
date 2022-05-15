#https://www.w3schools.com/python/python_mysql_create_table.asp
#Python MySQL Create Table 創建表
#Insert Into Table 插入表(在表內違增資料)
#To fill a table in MySQL, use the "INSERT INTO" statement.
#要填寫 MySQL 中的表，請使用「插入」語句。
#Insert a record in the "customers" table:
#在「客戶」表中插入記錄：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = (2.5, "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
#cursor()游標只能用於儲存過程和函數,游標的使用，主要包括游標的宣告、開啟、使用和關閉
#%s,輸入為字串格式
#val資料內容
#commit()確認交易，在交易結束時確認交易，在確認時資料才會真的寫入資料表。
#rowcount 列的資料
#record inserted 紀錄新增
#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
#重要！： 請注意聲明： mydb.commit()。需要更改，否則不會更改表。
#mycursor.rowcount,計算列的筆數

print("--------------------Insert Multiple Rows 插入多個列")
#Insert Multiple Rows 插入多個列
#To insert multiple rows into a table, use the executemany() method.
#要將多個列插入表中，請使用執行executemany()方法。
#The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:
#執行方法的第二個參數是tuples清單，其中包含要增加的數據：
#Fill the "customers" table with data:
#向「客戶」表填寫資料：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
#cursor()游標只能用於儲存過程和函數,游標的使用，主要包括游標的宣告、開啟、使用和關閉
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#增加到cutomers tab,欄位(name, address),值的格式%s,輸入為字串格式
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
#val(value的縮寫)

print("--------------------------------插入一行，並返回ID")
#Get Inserted ID 獲取增加ID
#You can get the id of the row you just inserted by asking the cursor object.
#您可以通過詢問游標對象來獲得剛插入的行的 ID。
#Note: If you insert more than one row, the id of the last inserted row is returned.
#注意：如果插入多個行，則返回最後插入行的ID。
#Insert one row, and return the ID:
#插入一行，並返回ID：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#先執行增加到資料到表,要設定增加的欄位與值的格式%s任何格式
val = ("Michelle", "Blue Village")
#輸入列的值
mycursor.execute(sql, val)
#執行這兩行變數的指令
mydb.commit()
#把資料寫入表內
print("1 record inserted, ID:", mycursor.lastrowid)
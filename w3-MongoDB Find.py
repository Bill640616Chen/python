#https://www.w3schools.com/python/python_mongodb_find.asp
#Python MongoDB Find MongoDB尋找
#In MongoDB we use the find and findOne methods to find data in a collection.
#在 MongoDB 中，我們使用 find 和 findOne 方法來查找集合中的數據。
#Just like the SELECT statement is used to find data in a table in a MySQL database.
#就像 SELECT 語句用於查找 MySQL 資料庫中的表中的數據一樣。
#Find One 查找一項
#To select data from a collection in MongoDB, we can use the find_one() method.
#如需在 MongoDB 中的集合中選取數據，我們可以使用 find_one（） 方法。
#The find_one() method returns the first occurrence in the selection.
#find_one（） 方法返回選擇中的第一個匹配項。
#Find the first document in the customers collection:
#查找 customers 集合中的首個文檔：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
x = mycol.find_one()
print(x)

print("----------------------------------Find All 查找全部")
#Find All 查找全部
#To select data from a table in MongoDB, we can also use the find() method.
#如需從 MongoDB 中的表中選取數據，我們還可以使用 find（） 方法。
#The find() method returns all occurrences in the selection.
#find（） 方法傳回選擇中的所有匹配項。
#The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.
#find（） 方法的第一個參數是 query 物件。 在這個例子中，我們用了一個空的 query 物件，它會選取集合中的所有文檔。
#No parameters in the find() method gives you the same result as SELECT * in MySQL.
#find（） 方法沒有參數提供與 MySQL 中的 SELECT * 相同的結果。
#Return all documents in the "customers" collection, and print each document:
#返回 「customers」 集合中的所有文件，並列印每個文件：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
for x in mycol.find():
  print(x)

print("----------------Return Only Some Fields 只返回某些欄")
#Return Only Some Fields 只返回某些欄
#The second parameter of the find() method is an object describing which fields to include in the result.
#find（） 方法的第二個參數是描述包含在結果中欄的物件。
#This parameter is optional, and if omitted, all fields will be included in the result.
#此參數是可選的，如果省略，則所有字段都將包含在結果中。
#Return only the names and addresses, not the _ids:
#只返回姓名和位址，而不是 _ids：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
#0代表False,1代表True
#You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). If you specify a field with the value 0, all other fields get the value 1, and vice versa:
#不允許在同一物件中同時指定 0 和 1 值（除非其中一個字段是 _id 欄位）。 如果指定值為 0 的欄位，則所有其他欄位的值為 1，反之亦然：
#This example will exclude "address" from the result:
print("--------------------這個例子從結果中排出 「address」")
#這個例子從結果中排出 「address」：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
for x in mycol.find({},{ "address": 0 ,"_id":0}):
  print(x)
#id若沒指定0,則預設會出現
#0代表False,1代表True

print("----------------------------------------error")
#error
#You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
#如果在同一物件中同時指定 0 和 1 值，則會出現錯誤（除非其中一個字段是 _id 字段）：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
for x in mycol.find({},{ "name": 1, "address": 0 }):
  print(x)
#0和1不能一起出現,如果要多欄查詢,0只能配給id
#或者是單獨出現,又或者每個欄位都是0
#一起出現的例外是_id:0
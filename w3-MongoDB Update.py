#https://www.w3schools.com/python/python_mongodb_update.asp
#Python MongoDB Update MongoDB更新
#Update Collection 更新集合
#You can update a record, or document as it is called in MongoDB, by using the update_one() method.
#您可以使用 update_one（） 方法來更新 MongoDB 中調用的記錄或文件。
#The first parameter of the update_one() method is a query object defining which document to update.
#update_one（） 方法的第一個參數是 query 物件，用於定義要更新的文件(列)。
#Note: If the query finds more than one record, only the first occurrence is updated.
#註釋：如果查詢找到多個記錄，則僅更新第一個匹配項。
#The second parameter is an object defining the new values of the document.
#第二個參數是定義文檔新值的物件。
#Change the address from "Valley 345" to "Canyon 123":
#把位址 "Valley 345" 改為 "Canyon 123"：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"},
  {"ABD":123},{"Boolean" : True},
  {"a":"abc"},{"a":"abc"},{"a":"abc"},{"a":"abc"},{"a":"abc"},{"a":"abc"},{"a":"abc"},{"a":"abc"},
]
x = mycol.insert_many(mylist)
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
#print "customers" after the update:
for x in mycol.find():
  print(x)

print("--------------------------------Update Many更新多個")
#Update Many更新多個
#To update all documents that meets the criteria of the query, use the update_many() method.
#如需更新符合查詢條件的所有文件(列)，請使用 update_many（） 方法。
#Update all documents where the address starts with the letter "S":
#更新位址以字母 「S」 開頭的所有文件(列)：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
#newvalues = { "$set": { "name": "Minnie" } }
#$set操作員用指定值替換欄位值
#{ $set: { <field1>: <value1>, ... } }
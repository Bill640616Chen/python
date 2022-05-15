#https://www.w3schools.com/python/python_mongodb_insert.asp
#Python MongoDB Insert Document MongoDB增加欄
#A document in MongoDB is the same as a record in SQL databases.
#MongoDB 中的文件與 SQL 資料庫中的記錄相同。
#Insert Into Collection 加入集合(表)
#To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
#要在 MongoDB 中把記錄或我們所稱的文件插入集合，我們使用 insert_one（） 方法。
#The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.
#insert_one（） 方法的第一個參數是字典，其中包含希望插入文檔中的每個欄位名稱和值。
#Insert a record in the "customers" collection:
#在 「customers」 集合中插入記錄：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

#Return the _id Field 返回 _id 列
#The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.
#insert_one（） 方法返回 InsertOneResult 物件，該物件擁有屬性 inserted_id，用於保存插入文檔的 id。
#Insert another record in the "customers" collection, and return the value of the _id field:
#在 「customers」 集合中插入另一條記錄，並返回 _id 字段的值：
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id)
#If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
#如果您沒有指定 _id 字段，那麼 MongoDB 將為您添加一個，併為每個文檔分配一個唯一的 ID。
#In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).
#在上例中，沒有指定 _id 欄位，因此 MongoDB 為記錄（文件）分配了唯一的 _id。

#Insert Multiple Documents 插入多個文件
#To insert multiple documents into a collection in MongoDB, we use the insert_many() method.
#要將多個文件插入 MongoDB 中的集合，我們使用 insert_many（） 方法。
#The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:
#insert_many（） 方法的第一個參數是包含字典的清單，其中包含要插入的數據：
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
#print list of the _id values of the inserted documents:
#列印被插入文件的 _id 值清單：
print(x.inserted_ids)
#The insert_many() method returns a InsertManyResult object, which has a property, inserted_ids, that holds the ids of the inserted documents.
#insert_many（） 方法返回 InsertManyResult 物件，該物件擁有屬性 inserted_ids，用於保存被插入文檔的 id。

print("--------------------------插入帶有指定ID的多個文件")
#Insert Multiple Documents, with Specified IDs
#插入帶有指定ID的多個文件
#If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the document(s).
#如果您不希望 MongoDB 為您的文件分配唯一 id，則可以在插入文件時指定 _id 字段。
#Remember that the values has to be unique. Two documents cannot have the same _id.
#請記住，值必須是唯一的。 兩個檔不能有相同的 _id。
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)
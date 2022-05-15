#https://www.w3schools.com/python/python_mongodb_drop_collection.asp
#Python MongoDB Drop Collection MongoDB刪除集合(表)
#Delete Collection 刪除集合(表)
#You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
#您可以使用 drop（） 方法刪除在 MongoDB 中呼叫的表或集合。
#Delete the "customers" collection:
#刪除 「customers」 集合：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mycol.drop()
#The drop() method returns true if the collection was dropped successfully, and false if the collection does not exist.
#如果成功刪除集合，則drop（） 方法返回 true，如果集合不存在則返回 false。
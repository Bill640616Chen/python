#https://www.w3schools.com/python/python_mongodb_delete.asp
#Python MongoDB Delete Document MongoDB排序
#Delete Document 刪除文件(列)
#To delete one document, we use the delete_one() method.
#要刪除一個文檔，我們使用 delete_one（） 方法。
#The first parameter of the delete_one() method is a query object defining which document to delete.
#delete_one（） 方法的第一個參數是 query 物件，用於定義要刪除的文件(列)。
#Note: If the query finds more than one document, only the first occurrence is deleted.
#註釋：如果查詢找到了多個文檔，則僅刪除第一個匹配項。
#Delete the document with the address "Mountain 21":
#刪除位址為 「Mountain 21」 的文件(列)：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)

print("----------------------------------刪除多個文件(列)")
#Delete Many Documents 刪除多個文件(列)
#To delete more than one document, use the delete_many() method.
#要刪除多個文件(列)，請使用 delete_many（） 方法。
#The first parameter of the delete_many() method is a query object defining which documents to delete.
#delete_many（） 方法的第一個參數是一個查詢物件，用於定義要刪除的文檔。
#Delete all documents were the address starts with the letter S:
#刪除位址以字母 S 開頭的所有文件(列)：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

print("-----------------------------刪除集合中的所有文件(列)")
#Delete All Documents in a Collection 刪除集合中的所有文件(列)
#To delete all documents in a collection, pass an empty query object to the delete_many() method:
#要刪除集合中的所有文件(列)，請把空的查詢對象傳遞給 delete_many（） 方法：
#Delete all documents in the "customers" collection:
#刪除 「customers」 集合中的所有文件(列)：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

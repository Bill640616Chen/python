#https://www.w3schools.com/python/python_mongodb_create_collection.asp
#Python MongoDB Create Collection MongoDB創建集合
#A collection in MongoDB is the same as a table in SQL databases.
#MongoDB 中的集合與 SQL 資料庫中的表相同。
#Creating a Collection 創建集合
#To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
#要在 MongoDB 中創建集合，請使用資料庫物件並指定要創建的集合的名稱。
#MongoDB will create the collection if it does not exist.
#如果它不存在，MongoDB 會創建該集合。
#Create a collection called "customers":
#建立名為 「customers」 的集合：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mycol.insert({"mydatabase":"aa","abs":"feeedee","123":"567"})
#數據寫進去之時，庫就會自然被建立,原來最後一行要先寫入,才能出現表跟庫!!
#最後一行要先寫入mycol.insert({"mydatabase":"aa"})
#Important: In MongoDB, a collection is not created until it gets content!
#重要提示：在 MongoDB 中，集合在獲得內容之前不會被創建！
#MongoDB waits until you have inserted a document before it actually creates the collection.
#在實際創建集合之前，MongoDB 會等待直到您已插入文檔。

#Check if Collection Exists檢查集合是否存在
#Remember: In MongoDB, a collection is not created until it gets content, so if this is your first time creating a collection, you should complete the next chapter (create document) before you check if the collection exists!
#請記住：在 MongoDB 中，集合在獲取內容之前不會創建，因此如果這是您第一次創建集合，則應在檢查集合是否存在之前完成下一章（創建文檔）！
#You can check if a collection exist in a database by listing all collections:
#您可以透過欄出所有集合來檢查資料庫中是否存在集合：
#Return a list of all collections in your database:
#傳回資料庫中所有集合的清單：
print(mydb.list_collection_names())
#Or you can check a specific collection by name:
#或者您可以按名稱檢查特定集合：
#Check if the "customers" collection exists:
#檢查 「customers」 集合是否存在：
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
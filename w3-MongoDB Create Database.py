#https://www.w3schools.com/python/python_mongodb_create_db.asp
#Python MongoDB Create Database MongoDB建立資料庫
#Creating a Database 創建資料庫
#To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.
#要在 MongoDB 中建立資料庫，首先要創建 MongoClient 對象，然後使用正確的 IP 位址和要創建的資料庫的名稱指定連接 URL。
#MongoDB will create the database if it does not exist, and make a connection to it.
#如果資料庫不存在，MongoDB 將創建資料庫並建立連接。
#Create a database called "mydatabase":
print("-------------------------建立名為 「mydatabase」 的資料庫：")
#建立名為 「mydatabase」 的資料庫：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mycol.insert({"mydatabase":"aa"})
#數據寫進去之時，庫就會自然被建立,原來最後一行要先寫入,才能出現表跟庫!!
#最後一行要先寫入mycol.insert({"mydatabase":"aa"})
#Important: In MongoDB, a database is not created until it gets content!
#重要說明：在 MongoDB 中，資料庫在獲取內容之前不會創建！
#所以你沒加東西的時候他就是空白的
#MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (and collection).
#在實際創建資料庫（和集合）之前，MongoDB 會一直等待您創建至少有一個文檔（記錄）的集合（表）。

print("-----------------傳回系統中的資料庫清單：")
#Check if Database Exists 檢查資料庫是否存在
#Remember: In MongoDB, a database is not created until it gets content, so if this is your first time creating a database, you should complete the next two chapters (create collection and create document) before you check if the database exists!
#請記住：在 MongoDB 中，資料庫在獲取內容之前不會創建，因此如果這是您第一次創建資料庫，則應在檢查資料庫是否存在之前完成接下來的兩章（創建集合和創建文檔）！
#You can check if a database exist by listing all databases in you system:
#您可以透過列出系統中的所有資料庫來檢查資料庫是否存在：
#Return a list of your system's databases:
#傳回系統中的資料庫清單：
print(myclient.list_database_names())
#Or you can check a specific database by name:
#或者您可以按名稱檢查特定資料庫：Name
#Check if "mydatabase" exists:
print("-----------------檢查 「mydatabase」 是否存在：")
#檢查 「mydatabase」 是否存在：
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

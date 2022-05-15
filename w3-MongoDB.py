#https://www.w3schools.com/python/python_mongodb_getstarted.asp
#Python MongoDB getstarted MongoDB準備開始
#Python can be used in database applications.
#Python 可以在資料庫應用程式中使用。
#One of the most popular NoSQL database is MongoDB.
#最受歡迎的 NoSQL 資料庫之一是 MongoDB。
#MongoDB
#MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable.
#MongoDB 將數據存儲在類似 JSON 的文件中，這使得資料庫非常靈活和可伸縮。
#To be able to experiment with the code examples in this tutorial, you will need access to a MongoDB database.
#為了能夠測試本教程中的代碼範例，您需要訪問 MongoDB 資料庫。
#You can download a free MongoDB database at https://www.mongodb.com.
#您可以在 https://www.mongodb.com 下載免費的 MongoDB 資料庫。
#Or get started right away with a MongoDB cloud service at https://www.mongodb.com/cloud/atlas.
#或者立即開始在 https://www.mongodb.com/cloud/atlas 提供 MongoDB 雲服務。
#PyMongo
#Python needs a MongoDB driver to access the MongoDB database.
#Python 需要 MongoDB 驅動程式來訪問 MongoDB 資料庫。
#In this tutorial we will use the MongoDB driver "PyMongo".
#在本教程中，我們會使用 MongoDB 驅動程式 「PyMongo」。
#We recommend that you use PIP to install "PyMongo".
#我們建議您使用 PIP 安裝 「PyMongo」。
#PIP is most likely already installed in your Python environment.
#PIP 很可能已經安裝在 Python 環境中。
#Navigate your command line to the location of PIP, and type the following:
#將命令行導航到 PIP 的位置，然後鍵入以下內容：
#Download and install "PyMongo":
#下載並安裝 「PyMongo」 python -m pip install pymongo
#Now you have downloaded and installed a mongoDB driver.
#現在您已經下載並安裝了 mongoDB 驅動程式。
#Test PyMongo測試 PyMongo
#To test if the installation was successful, or if you already have "pymongo" installed, create a Python page with the following content:
#如需測試安裝是否成功，或者您是否已安裝 「pymongo」，請創建一張包含以下內容的 Python 頁面：
#demo_mongodb_test.py:
import pymongo
#If the above code was executed with no errors, "pymongo" is installed and ready to be used.
#如果執行上述代碼沒有錯誤，則 「pymongo」 已安裝就緒。

from pymongo import MongoClient
from pymongo import database
from pymongo.database import Database
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase1"]
dblist = myclient.list_database_names()
if "mydatabase1" in dblist:
  print("The database exists.")



#在mongo.exe建立資料庫及表
#use mydatabase 建立資料庫
#db.TableA.save({name:'linroex'}) 建立資料表
#({field(欄):'字串'})
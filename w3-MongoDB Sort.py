#https://www.w3schools.com/python/python_mongodb_sort.asp
#Python MongoDB Sort MongoDB排序
#Sort the Result 結果排序
#Use the sort() method to sort the result in ascending or descending order.
#請使用 sort（） 方法按升序或降序對結果進行排序。
#The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
#sort（） 方法為 "fieldname"（欄位名稱）提供一個參數，為 "direction"（方向）提供一個參數（升序是預設方向）。
#Sort the result alphabetically by name:
#依姓名的字母順序對結果進行排序：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydoc = mycol.find().sort("name",1)
for x in mydoc:
  print(x)
#非name欄位的先排序,再排name欄位的升序(預設)

print("----------------------------Sort Descending 降序排序")
#Sort Descending 降序排序
#Use the value -1 as the second parameter to sort descending.
#使用值 -1 作為第二個參數進行降序排序。
#sort("name", 1) #ascending 升序
#sort("name", -1) #descending 降序
#Sort the result reverse alphabetically by name:
#按名稱的逆向字母順序對結果進行排序：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
  print(x)
#先排name欄位的降序,非name欄位的後排序
#就算參數是1,也是先排非name欄位的順序
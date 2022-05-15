#https://www.w3schools.com/python/python_mongodb_query.asp
#Python MongoDB Query MongoDB查询
#Filter the Result 篩選結果
#When finding documents in a collection, you can filter the result by using a query object.
#在集合中尋找文件時，您能夠使用 query 物件過濾結果。
#The first argument of the find() method is a query object, and is used to limit the search.
#find（） 方法的第一個參數是 query 物件，用於限定搜索。
#Find document(s) with the address "Park Lane 38":
#尋找位址為 「Park Lane 38」 的文件：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

print("--------------------------Advanced Query 高級查詢")
#Advanced Query 高級查詢
#To make advanced queries you can use modifiers as values in the query object.
#如需進行高級查詢，可以使用修飾符作為查詢物件中的值。
#E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:
#例如，要查找 「address」 欄位以字母 「S」 或更高（按字母順序）開頭的文檔，請使用大於修飾符：{"$gt"： "S"}：
#Find documents where the address starts with the letter "S" or higher:
#尋找位址以字母 「S」 或更高開頭的文件：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
#"$gt": "S",大於S,因為字母26個,所以包含S開頭之後英文字母都會顯示

print("------------------------------使用正則表達式來篩選")
#Filter With Regular Expressions 使用正則表達式來篩選
#You can also use regular expressions as a modifier.
#您也可以將正則表示式用作修飾符。
#Regular expressions can only be used to query strings.
#正則表示式只能用於查詢字串。
#To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:
#如果只查找 "address" 字段以字母 "S" 開頭的文檔，請使用正則表達式 {"$regex"： "^S"}：
#Find documents where the address starts with the letter "S":
#查找位址以字母 「S」 開頭的文件
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)
#^：Starts with開始於
#.：Any character (except newline character)任何字元（換行符除外）
#*：Zero or more occurrences零次或多次出现
#$：Ends with結束於
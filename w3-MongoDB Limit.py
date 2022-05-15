#https://www.w3schools.com/python/python_mongodb_limit.asp
#Python MongoDB Limit MongoDB限定
#Limit the Result
#To limit the result in MongoDB, we use the limit() method.
#要限制 MongoDB 中的結果，我們使用 limit（） 方法。
#The limit() method takes one parameter, a number defining how many documents to return.
#limit（） 方法接受一個參數，定義的數位表示返回的文檔數。
#Consider you have a "customers" collection:
#假設你有一個 「customers」 集合：
'''
Customers
{'_id': 1, 'name': 'John', 'address': 'Highway37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
'''
#Limit the result to only return 5 documents:
#把結果限定為只返回 5 個文件：
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
x = mycol.delete_many({})
mylist = [{'_id': 1, 'name': 'John', 'address': 'Highway37'},
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'},
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'},
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'},
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'},
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'},
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'},
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'},
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'},
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'},
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'},
{'_id': 12, 'name': 'William', 'address': 'Central st 954'},
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'},
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
]
x = mycol.insert_many(mylist)
myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
  print(x)

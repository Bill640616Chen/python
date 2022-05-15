#https://www.w3schools.com/python/python_dictionaries_change.asp
#Python Change Dictionary Items 改變字典項目
#Change Values 改值
#You can change the value of a specific item by referring to its key name:
#你可以改變指定項目的值靠著引用它鍵的名稱
#Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

#Update Dictionary 更新字典
#The update() method will update the dictionary with the items from the given argument.
#update() method 將更新字典,從被給予參數的項目
#The argument must be a dictionary, or an iterable object with key:value pairs.
#參數一定要是字典裡,或者一個可迭代物品,只能用key:value一對的樣式
#Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#更新鍵的值
print(thisdict)
thisdict.update({"aaa":222})
#新增鍵值
print(thisdict)
thisdict["bbb"] = 111
#新增鍵值
print(thisdict)
thisdict["bbb"] = 10
#更新鍵的值
print(thisdict)


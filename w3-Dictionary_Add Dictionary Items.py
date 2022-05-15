#https://www.w3schools.com/python/python_dictionaries_add.asp
#Python Add Dictionary Items 增加字典項目
#Adding Items
#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
#增加一個項目到字典,靠著使用一個新的索引鍵,而且指定一個值給它
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
thisdict.update({"aaa":"bb"})
print(thisdict)
#Update Dictionary
#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
#update() method將會更新字典項目會被給予一個參數。如果該項目不存在，該項目會被加入。
#The argument must be a dictionary, or an iterable object with key:value pairs.
#參數必須是字典,或者一個可迭代物品有一對key:value
#Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) #新增和更正
thisdict["222"] = 111 #新增和更正
thisdict["color"] = "blue"
thisdict.update({"222": 11})
print(thisdict)

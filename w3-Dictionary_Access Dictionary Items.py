#https://www.w3schools.com/python/python_dictionaries_access.asp
#Python Access Dictionary Items 訪問字典項目
#Accessing Items
#You can access the items of a dictionary by referring 
# to its key name, inside square brackets:
#你可以訪問字典的項目,靠著引用它的鍵的名稱,書寫方式是["keyname"]
#Get the value of the "model" key:
#用鍵取值,不能用值取鍵,鍵的大小寫一定要一樣,不然會出錯
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(thisdict["model"]) #Mustang,有傳回值
print(x) #Mustang

#There is also a method called get() that will give you the same result:
#Get the value of the "model" key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(thisdict.get("model")) #Mustang,有傳回值
print(x) #Mustang

#Get Keys
#The keys() method will return a list of all the keys in the dictionary.
#Get a list of the keys:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys() #()取鍵不取值
print(thisdict.keys()) #dict_keys(['brand', 'model', 'year'])
print(x) #dict_keys(['brand', 'model', 'year'])
#The list of the keys is a view of the dictionary, meaning 
# that any changes done to the dictionary will be 
# reflected in the keys list.
#鍵的清單是字典的檢視,意思是任何字典的改變將會反應在鍵的清單中
#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys() #key()有傳回值
print(x) #before the change
#dict_keys(['brand', 'model', 'year'])
car["color"] = "white" #新增鍵值和改變鍵的值的方法
print(x) #after the change
#dict_keys(['brand', 'model', 'year', 'color'])
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}
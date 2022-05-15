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
x = thisdict[1]
print(x) #Mustang


#https://www.w3schools.com/python/python_dictionaries_remove.asp
#Python Remove Dictionary Items 移除字典項目
#Removing Items
#There are several methods to remove items from a dictionary:
#有很多方法可以從字典裡移除項目
print("-------------thisdict.pop(參數) #pop(一定要有參數)")
#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #pop(一定要有參數)
print(thisdict)
#The popitem() method removes the last inserted item 
# (in versions before 3.7, a random item is removed instead):
print("-------------thisdict.popitem() #popitem(不用參數)")
#popitem() method移除最後一個項目(在3.7版,是隨意移除)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() #popitem(無需參數)
print(thisdict)
print("----------------------del關鍵字用[],[]裡面要有參數")
#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"] #關鍵字用[]
print(thisdict)
del thisdict #則整個字典刪除,沒有空字典
#name 'thisdict' is not defined

print("----------------clear() #刪除字典裡的鍵值,(不用參數)")
#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #刪除字典裡的鍵值,(不用參數)
print(thisdict) #{}空字典

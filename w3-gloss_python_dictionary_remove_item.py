#https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp
#Removing Items from a Dictionary 在字典中新增項目
#There are several methods to remove items from a dictionary:
#從字典中刪除物品有幾種方法：
#The method removes the item with the specified key name:pop()
#該方法移除具有指定關鍵名稱的專案：pop()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
print('-------------分隔線------------')
#The method removes the last inserted item (in versions before 3.7, a random item is removed instead):popitem()
#該方法刪除最後插入的專案（在 3.7 之前的版本中，隨機專案被刪除）：popitem()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
print('-------------分隔線------------')
#The keyword removes the item with the specified key name:del
#關鍵字移除具有指定關鍵名稱的專案：del
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
print('-------------分隔線------------')
#The keyword can also delete the dictionary completely:del
#關鍵字還可以完全刪除字典：del
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)
#this will cause an error because "thisdict" no longer exists.
'''
print('NameError: name thisdict is not defined')
print('-------------分隔線------------')
#The keyword empties the dictionary:clear()
#關鍵字清空字典：clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#Related Pages 相關頁面
#Python Dictionaries Tutorial Python 詞典教程
#https://www.w3schools.com/python/python_dictionaries.asp
#Dictionary 字典
#https://www.w3schools.com/python/gloss_python_dictionary.asp
#Access Dictionary Items 訪問字典項目
#https://www.w3schools.com/python/gloss_python_access_dictionary_items.asp
#Change Dictionary Item 更改字典項目
#https://www.w3schools.com/python/gloss_python_change_dictionary_item.asp
#Loop Dictionary Items 迴圈字典項目
#https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
#Check if Dictionary Item Exists 檢查字典項目是否存在
#https://www.w3schools.com/python/gloss_python_check_if_dictionary_item_exists.asp
#Dictionary Length 字典長度
#https://www.w3schools.com/python/gloss_python_dictionary_length.asp
#Add Dictionary Item 添加字典項目
#https://www.w3schools.com/python/gloss_python_dictionary_add_item.asp
#Copy Dictionary 複製詞典
#https://www.w3schools.com/python/gloss_python_copy_dictionary.asp
#Nested Dictionaries 嵌套詞典
#https://www.w3schools.com/python/gloss_python_nested_dictionaries.asp

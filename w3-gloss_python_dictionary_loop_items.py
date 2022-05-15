#https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
#Loop Through a Dictionary 迴圈字典
#You can loop through a dictionary by using a loop.for
#您可以使用循環循環瀏覽字典。for
#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#循環通過字典時，傳回值是字典的關鍵，但也有方法傳回值。
#Print all key names in the dictionary, one by one:
#逐個列印字典中的所有關鍵名稱：
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
print('-------------分隔線------------')
#Print all values in the dictionary, one by one:
#逐個列印字典中的所有值：
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
print('-------------分隔線------------')
#You can also use the function to return values of a dictionary:values()
#您還可以使用該函數傳回字典的值：values()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
print('-------------分隔線------------')
#Loop through both keys and values, by using the function:items()
#使用此功能循環通過金鑰與值：items()
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
#Related Pages 相關頁面
#Python Dictionaries Tutorial Python 詞典教程
#https://www.w3schools.com/python/python_dictionaries.asp
#Dictionary 字典
#https://www.w3schools.com/python/gloss_python_dictionary.asp
#Access Dictionary Items 訪問字典項目
#https://www.w3schools.com/python/gloss_python_access_dictionary_items.asp
#Change Dictionary Item 更改字典項目
#https://www.w3schools.com/python/gloss_python_change_dictionary_item.asp
#Check if Dictionary Item Exists 檢查字典項目是否存在
#https://www.w3schools.com/python/gloss_python_check_if_dictionary_item_exists.asp
#Dictionary Length 字典長度
#https://www.w3schools.com/python/gloss_python_dictionary_length.asp
#Add Dictionary Item 添加字典項目
#https://www.w3schools.com/python/gloss_python_dictionary_add_item.asp
#Remove Dictionary Items 刪除字典項目
#https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp
#Copy Dictionary 複製詞典
#https://www.w3schools.com/python/gloss_python_copy_dictionary.asp
#Nested Dictionaries 嵌套詞典
#https://www.w3schools.com/python/gloss_python_nested_dictionaries.asp

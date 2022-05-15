#https://www.w3schools.com/python/gloss_python_nested_dictionaries.asp
#Nested Dictionaries 嵌套詞典
#A dictionary can also contain many dictionaries, this is called nested dictionaries.
#字典也可以包含許多字典，這叫做嵌套詞典。
#Create a dictionary that contain three dictionaries:
#建立包含三個字典的字典：
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print('-------------分隔線------------')
#Or, if you want to nest three dictionaries that already exists as dictionaries:
#或者，如果你想窩三個字典已經存在作為字典：
#Create three dictionaries, than create one dictionary that will contain the other three dictionaries:
#建立三個詞典，而不是創建一個字典，將包含其他三個詞典：
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
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
#Remove Dictionary Items 刪除字典項目
#https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp
#Copy Dictionary 複製詞典
#https://www.w3schools.com/python/gloss_python_copy_dictionary.asp

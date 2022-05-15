#https://www.w3schools.com/python/gloss_python_copy_dictionary.asp
#Copy a Dictionary 複製字典
#You cannot copy a dictionary simply by typing , because: will only be a reference to , and changes made in will automatically also be made in .dict2 = dict1dict2dict1dict1dict2
#你不能簡單地通過打字來複製字典，因為：只會是一個參考，而修改也會自動在。dict2 = dict1dict2dict1dict1dict2
#There are ways to make a copy, one way is to use the built-in Dictionary method . copy()
#有辦法複製，一種方法是使用內置詞典的方法。 copy()
#Make a copy of a dictionary with the method:copy()
#使用該方法製作字典複本：copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
print('-------------分隔線------------')
#Another way to make a copy is to use the built-in method .dict()
#製作副本的另一種方法是使用內置方法。dict()
#Make a copy of a dictionary with the method:dict()
#使用該方法製作字典複本：dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
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
#Nested Dictionaries 嵌套詞典
#https://www.w3schools.com/python/gloss_python_nested_dictionaries.asp

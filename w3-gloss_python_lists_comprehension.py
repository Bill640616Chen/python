#https://www.w3schools.com/python/gloss_python_list_comprehension.asp
#loop_comprehension 清單理解
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#當您想要根據現有清單的值創建新清單時，清單理解提供了更短的語法。
#Example: You want to create a list of all the fruits that has the letter "a" in the name.
#範例：您要建立名稱中字母"a"的所有水果清單。
#Without list comprehension you will have to write a statement with a conditional test inside:for
#如果沒有清單理解，您將不得不在其中編寫帶有條件測試的聲明：for
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
print('-------------分隔線------------')
#With list comprehension you can do all that with only one line of code:
#有了清單理解，您只需一行代碼即可做到這一點：
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#The list comprehension is wrapped around square backets, contains one or more statements, zero or more statements, and returns a new list.forif
#清單理解圍繞方形後背，包含一個或多個語句、零或多個語句，並返回新清單。forif
#Related Pages 相關頁面
#Python Lists Tutorial Python 清單教程
#https://www.w3schools.com/python/python_lists.asp
#Lists 清單
#https://www.w3schools.com/python/gloss_python_lists.asp
#Access List Items 訪問清單項目
#https://www.w3schools.com/python/gloss_python_access_list_items.asp
#Change List Item 更改清單項目
#https://www.w3schools.com/python/gloss_python_change_list_item.asp
#Loop List Items 迴圈清單項目
#https://www.w3schools.com/python/gloss_python_loop_list_items.asp
#Check If List Item Exists 檢查清單項目是否存在
#https://www.w3schools.com/python/gloss_python_check_if_list_item_exists.asp
#List Length 清單長度
#https://www.w3schools.com/python/gloss_python_list_length.asp
#Add List Items 添加清單項目
#https://www.w3schools.com/python/gloss_python_add_list_items.asp
#Remove List Items 刪除清單項目
#https://www.w3schools.com/python/gloss_python_remove_list_items.asp
#Copy a List 複製清單
#https://www.w3schools.com/python/gloss_python_copy_list.asp
#Join Two Lists 加入兩個清單
#https://www.w3schools.com/python/gloss_python_join_lists.asp
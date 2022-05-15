#https://www.w3schools.com/python/gloss_python_join_lists.asp
#Join Two Lists 加入兩個清單
#There are several ways to join, or concatenate, two or more lists in Python.
#在 Python 中加入或串聯兩個或多個清單有幾種方法。
#One of the easiest ways are by using the operator.+
#最簡單的方法之一是使用操作員。+
#Join two list:
#加入兩個清單：
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
print('-------------分隔線------------')
#Another way to join two lists are by appending all the items from list2 into list1, one by one:
#加入兩個清單的另一種方法是將清單 2 中的所有專案逐個附加到清單 1 中：
#Append list2 into list1:
#新增清單2進入清單1：
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
print('-------------分隔線------------')
#Or you can use the method, which purpose is to add elements from one list to another list:extend()
#或者您可以使用該方法，其目的是將一個清單中的元素添加到另一個清單：extend()
#Use the method to add list2 at the end of list1:extend()
#使用該方法在清單末尾新增清單 2：extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
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
#List Comprehension 清單理解
#https://www.w3schools.com/python/gloss_python_list_comprehension.asp
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

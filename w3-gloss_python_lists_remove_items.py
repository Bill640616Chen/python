#https://www.w3schools.com/python/gloss_python_remove_list_items.asp
#remove_items 刪除項目
#There are several methods to remove items from a list:
#從清單中移除項目有幾種方法：
#The method removes the specified item:remove()
#該方法移除指定的專案：remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print('-------------分隔線------------')
#The method removes the specified index, (or the last item if index is not specified):pop()
#該方法刪除指定的索引（或未指定索引的最後一個專案）：pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print('-------------分隔線------------')
#The keyword removes the specified index:del
#關鍵字移除指定的索引：del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print('-------------分隔線------------')
#The keyword can also delete the list completely:del
#關鍵字還可以完全刪除清單：del
thislist = ["apple", "banana", "cherry"]
del thislist
print('-------------分隔線------------')
#The method empties the list:clear()
#該方法清空清單：clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
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
#Copy a List 複製清單
#https://www.w3schools.com/python/gloss_python_copy_list.asp
#Join Two Lists 加入兩個清單
#https://www.w3schools.com/python/gloss_python_join_lists.asp
#https://www.w3schools.com/python/gloss_python_access_list_items.asp
#access_list_items 訪問清單項目
#You access the list items by referring to the index number:
#您透過參考索引號存取清單項目：
#Print the second item of the list:
#列印清單中的第二個專案：
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Negative Indexing 負索引
#Negative indexing means beginning from the end, refers to the last item, refers to the second last item etc.-1-2
#負索引是指從末尾開始，指最後一個專案，指第二個最後一個專案等。-1-2
print('-------------分隔線------------')
#Print the last item of the list:
#列印清單的最後一個專案：
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#Range of Indexes 索引範圍
#You can specify a range of indexes by specifying where to start and where to end the range.
#您可以通過指定開始的位置和結束範圍的位置來指定一系列索引。
#When specifying a range, the return value will be a new list with the specified items.
#指定範圍時，返回值將是帶有指定專案的新清單。
print('-------------分隔線------------')
#Return the third, fourth, and fifth item:
#返回第三、第四和第五項：
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).
#注意：搜索將從索引 2（包括在內）開始，以索引 5 結束（不包括在內）。
#Remember that the first item has index 0.
#請記住，第一個專案有索引 0。
#By leaving out the start value, the range will start at the first item:
#通過排除起始值，範圍將從第一個項目開始：
print('-------------分隔線------------')
#This example returns the items from the beginning to "orange":
#此示例將專案從開始返回到「橙色」：
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#By leaving out the end value, the range will go on to the end of the list:
#通過排除最終值，範圍將進入清單的末尾：
print('-------------分隔線------------')
#This example returns the items from "cherry" and to the end:
#此範例將專案從「櫻桃」返回到最後：
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#Range of Negative Indexes 負指數範圍
#Specify negative indexes if you want to start the search from the end of the list:
#如果要從清單末尾開始搜索，請指定負索引：
print('-------------分隔線------------')
#This example returns the items from index -4 (included) to index -1 (excluded)
#此範例會從索引 -4（包括）傳回到索引 -1（不包括）
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Related Pages 相關頁面
#Python Lists Tutorial Python 清單教程
#https://www.w3schools.com/python/python_lists.asp
#Lists 清單
#https://www.w3schools.com/python/gloss_python_lists.asp
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
#Join Two Lists 加入兩個清單
#https://www.w3schools.com/python/gloss_python_join_lists.asp
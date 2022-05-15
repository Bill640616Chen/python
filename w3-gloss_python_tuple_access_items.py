#https://www.w3schools.com/python/gloss_python_access_tuple_items.asp
#access_tuple_items 訪問tuple項目 
#You can access tuple items by referring to the index number, inside square brackets:
#您可以透過參考指數編號（方括弧內）存取tuple專案：
#Print the second item in the tuple:
#列印tuple的第二個專案：
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Negative Indexing 負索引
#Negative indexing means beginning from the end, refers to the last item, refers to the second last item etc.-1-2
#負索引是指從末尾開始，指最後一個專案，指第二個最後一個專案等。-1-2
print('-------------分隔線------------')
#Print the last item of the tuple:
#列印tuple的末項：
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#Range of Indexes 索引範圍
#You can specify a range of indexes by specifying where to start and where to end the range.
#您可以通過指定開始的位置和結束範圍的位置來指定一系列索引。
#When specifying a range, the return value will be a new tuple with the specified items.
#指定範圍時，返回值將是帶有指定專案的全新tuple。
print('-------------分隔線------------')
#Return the third, fourth, and fifth item:
#返回第三、第四和第五項：
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).
#注意：搜索將從索引 2（包括在內）開始，以索引 5 結束（不包括在內）。
#Remember that the first item has index 0.
#請記住，第一個專案有索引 0。
#Range of Negative Indexes 負指數範圍
#Specify negative indexes if you want to start the search from the end of the tuple:
#如果要從tuple的末尾開始搜索，請指定負索引：
print('-------------分隔線------------')
#This example returns the items from index -4 (included) to index -1 (excluded)
#此範例會從索引 -4（包括）傳回到索引 -1（不包括）
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Related Pages 相關頁面
#Python Tuples Tutorial Python Tuples教程
#https://www.w3schools.com/python/python_tuples.asp
#Tuple
#https://www.w3schools.com/python/gloss_python_tuple.asp
#Change Tuple Item 更改Tuple項目
#https://www.w3schools.com/python/gloss_python_change_tuple_item.asp
#Loop List Items 迴圈清單項目
#https://www.w3schools.com/python/gloss_python_loop_tuple_items.asp
#Check if Tuple Item Exists 檢查是否存在 Tuple 項目
#https://www.w3schools.com/python/gloss_python_check_if_tuple_item_exists.asp
#Tuple Length Tuple長度
#https://www.w3schools.com/python/gloss_python_tuple_length.asp
#Tuple With One Item 帶一個項目的 Tuple
#https://www.w3schools.com/python/gloss_python_tuple_one_item.asp
#Remove Tuple Items 刪除 Tuple 項目
#https://www.w3schools.com/python/gloss_python_remove_tuple_items.asp
#Join Two Tuples 加入兩個Tuples
#https://www.w3schools.com/python/gloss_python_join_tuple.asp
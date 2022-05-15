#https://www.w3schools.com/python/gloss_python_change_tuple_item.asp
#Change Tuple Values 更改Tuple值
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#一旦創建了 Tuple，您就無法更改其值。tuple是不變的，或變的，因為它也被稱為。
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#但有一個解決方法。您可以將tuple換為清單，更改清單，並將清單轉換回tuple。
#Convert the tuple into a list to be able to change it:
#將 Tuple 轉換為清單以便能夠變更它：
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Related Pages 相關頁面
#Python Tuples Tutorial Python Tuples教程
#https://www.w3schools.com/python/python_tuples.asp
#Tuple
#https://www.w3schools.com/python/gloss_python_tuple.asp
#Access Tuple Items 訪問Tuple項目
#https://www.w3schools.com/python/gloss_python_access_tuple_items.asp
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
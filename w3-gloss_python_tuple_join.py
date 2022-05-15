#https://www.w3schools.com/python/gloss_python_remove_tuple_items.asp
#Remove Tuple Items 刪除Tuple項目
#To join two or more tuples you can use the operator:+
#要加入兩個或兩個以上的 Tuple，您可以使用運算符：+
#Join two tuples:
#加入兩個tuples：
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print('-------------分隔線------------')
tuple1 = ["a", "b" , "c"]
tuple2 = [1, 2, 3]
for x in tuple2:
  tuple1.append(x)
print(tuple1)
print('-------------分隔線------------')
#Or you can use the method, which purpose is to add elements from one tuple to another tuple:extend()
#或者您可以使用該方法，其目的是將一個tuple中的元素添加到另一個tuple：extend()
#Use the method to add tuple2 at the end of tuple1:extend()
#使用該方法在tuple末尾新增tuple 2：extend()
tuple1 = ["a", "b" , "c"]
tuple2 = [1, 2, 3]
tuple1.extend(tuple2)
print(tuple1)
#Related Pages 相關頁面
#Python Tuples Tutorial Python Tuples教程
#https://www.w3schools.com/python/python_tuples.asp
#Tuple
#https://www.w3schools.com/python/gloss_python_tuple.asp
#Access Tuple Items 訪問Tuple項目
#https://www.w3schools.com/python/gloss_python_access_tuple_items.asp
#Change Tuple Item 更改Tuple項目
#https://www.w3schools.com/python/gloss_python_change_tuple_item.asp
#Loop tuple Items 迴圈tuple項目
#https://www.w3schools.com/python/gloss_python_loop_tuple_items.asp
#Check if Tuple Item Exists 檢查是否存在 Tuple 項目
#https://www.w3schools.com/python/gloss_python_check_if_tuple_item_exists.asp
#Tuple Length Tuple長度
#https://www.w3schools.com/python/gloss_python_tuple_length.asp
#Tuple With One Item 帶一個項目的 Tuple
#https://www.w3schools.com/python/gloss_python_tuple_one_item.asp
#Remove Tuple Items 刪除 Tuple 項目
#https://www.w3schools.com/python/gloss_python_remove_tuple_items.asp

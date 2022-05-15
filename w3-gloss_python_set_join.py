#https://www.w3schools.com/python/gloss_python_join_sets.asp
#Join Two Sets 合併兩個集合
#There are several ways to join two or more sets in Python.
#有幾種方法可以加入 Python 中的兩個集合或更多集合。
#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
#您可以使用傳回包含兩組所有專案的新集的方法，或將所有項目從一組插入另一組的方法：union()update()
#The union() method returns a new set with all items from both sets:
#該方法返回一個新集合，其中包括兩個集合的所有專案：union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#The update() method inserts the items in set2 into set1:
#該方法將第 2 個集合中的專案插入 set1：update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
print('-------------分隔線------------')
set1 = ["a", "b" , "c"]
set2 = [1, 2, 3]
for x in set2:
  set1.append(x)
print(set1)
print('-------------分隔線------------')
#Or you can use the method, which purpose is to add elements from one set to another set:extend()
#或者您可以使用該方法，其目的是將一個set中的元素添加到另一個set：extend()
#Use the method to add set2 at the end of set1:extend()
#使用該方法在set末尾新增set 2：extend()
set1 = ["a", "b" , "c"]
set2 = [1, 2, 3]
set1.extend(set2)
print(set1)
#Note: Both union() and update() will exclude any duplicate items.
#注意：兩者都不包括任何重複的專案。union()update()
#There are other methods that joins two sets and keeps ONLY the duplicates, or NEVER the duplicates, check all the built-in set methods in Python.
#還有其他方法，加入兩套，並保持只有重複，或從來沒有重複，檢查所有內置設置的方法在Python。
#https://www.w3schools.com/python/python_ref_set.asp
#Related Pages 相關頁面
#Python Sets Tutorial Python 集合教程
#https://www.w3schools.com/python/python_sets.asp
#Set 集合
#https://www.w3schools.com/python/gloss_python_set.asp
#Access Set Items 訪問集合項目
#https://www.w3schools.com/python/gloss_python_access_set_items.asp
#Add Set Items 添加集合項目
#https://www.w3schools.com/python/gloss_python_add_set_items.asp
#Loop Set Items 迴圈集合項目
#https://www.w3schools.com/python/gloss_python_loop_set_items.asp
#Check if Set Item Exists 檢查是否存在集合項目
#https://www.w3schools.com/python/gloss_python_check_if_set_item_exists.asp
#Set Length 集合長度
#https://www.w3schools.com/python/gloss_python_set_length.asp
#Remove Set Items 刪除集合項目
#https://www.w3schools.com/python/gloss_python_remove_set_items.asp

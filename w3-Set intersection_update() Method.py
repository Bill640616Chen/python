#https://www.w3schools.com/python/ref_set_intersection_update.asp
#Python Set intersection_update() Method 集合intersection_update()方法
#Remove the items that is not present in both x and y:
#刪除 x 與 y 中不存在的項目：
#只會保留2個集合共有的值,不會傳回值
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) #{'apple'}
#Definition and Usage
#The intersection_update() method removes the items that is not 
# present in both sets (or in all sets if the comparison is done 
# between more than two sets).
#intersection_update()的方法刪除項目不存在兩個集合中(或者在所有集合中
# 如果在兩個集合上比較)
#The intersection_update() method is different from the intersection()
# method, because the intersection() method returns a new set, without
#  the unwanted items, and the intersection_update() method removes 
#  the unwanted items from the original set.
#intersection_update()與intersection()不同,因為intersection()會傳回一
# 個新的集合,沒有不需要的專案，intersection_update（）方法從原始集合刪除
# 不需要的專案。
#Syntax
#set.intersection_update(set1, set2 ... etc)
#Parameter Values
#Parameter：Description
#set1：Required. The set to search for equal items in
#set2：Optional. The other set to search for equal items in.
#You can compare as many sets you like. 可以比較很多項目
#Separate the sets with a comma 要用逗號分開集合
#Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x.intersection_update(y, z)) #None,並不會傳回新的set
print(x) #{'c'}
#https://www.w3schools.com/python/ref_set_symmetric_difference.asp
#Python Set symmetric_difference_update() Method
#集合symmetric_difference_update() 方法
#inserts the symmetric differences from this set and another
#插入這個set與另一個set的對稱差異
#Remove the items that are present in both sets, AND insert the items that is not present in both sets:
#刪除兩組中存在的項目，並插入兩套中不存在的項目：
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) #無傳回值,但屬性可以執行
print(x) #{'cherry', 'microsoft', 'banana', 'google'}
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update("orange")
print(x) #{'a', 'n', 'o', 'g', 'e', 'banana', 'cherry', 'apple', 'r'}
#把變數換成參數後,參數被拆成一個一個字元
#x.symmetric_difference_update 無傳回值
#Update a set with the symmetric difference of itself and another.
#更新一個集合與自身和另一個集合對稱的差異。
#Definition and Usage
#The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
#symmetric_difference_update()更新原始的集合,靠著移除兩個集合都存在的項目,並插入其他項目
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) #無傳回值
#更新原始的集合(x),在y移除共同的項目,並插入y的項目
print(x) #{'cherry', 'banana', 'google', 'microsoft'}
#Syntax
#set.symmetric_difference_update(set)
#Parameter Values
#Parameter：Description
#set：Required. The set to check for matches in
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z =x.symmetric_difference_update(y) #無傳回值
print(z) #None
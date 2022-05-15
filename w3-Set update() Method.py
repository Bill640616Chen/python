#https://www.w3schools.com/python/ref_set_update.asp
#Python Set update() Method 集合更新方法
#Update the set with another set, or any other iterable
#從現在的集合,用另一個集合來更新,或其他可迭代物件
#Insert the items from set y into set x:
print("-------------------------------集合update集合")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) #aplle在x裡有了,所以不更新
print(x) 
#{'apple', 'banana', 'microsoft', 'cherry', 'google'
print("-------------------------------集合update Tuple")
x = {"apple", "banana", "cherry"}
y = ("google", "microsoft", "apple")
x.update(y)
print(x) 
#{'banana', 'google', 'cherry', 'microsoft', 'apple'}
print("-------------------------------集合update list")
x = {"apple", "banana", "cherry"}
y = ["google", "microsoft", "apple"]
x.update(y)
print(x)
 #{'microsoft', 'google', 'banana', 'cherry', 'apple'}
#Definition and Usage
#The update() method updates the current set, by adding items from another set (or any other iterable).
print("----------------------------集合update list, Tuple")
#If an item is present in both sets, only one appearance 
# of this item will be present in the updated set.
#如果一個項目存在於兩個集合裡,那結果將只有一個項目會出現
# 被更新的集合裡
x = {"apple", "banana", "cherry"}
y = ["google", "microsoft", "apple"]
z = ("1","2","3")
x.update(y,z)
print(x)
#Syntax
print("---------------------------集合update很多可迭代物件")
#set.update(set, iterabe1,...)(裡面可以放很多可迭代物件)
#Parameter Values
#Parameter：Description
#set：Required. The iterable insert into the current set
x = {"apple", "banana", "cherry"}
y = ["google", "microsoft", "apple"]
z = ("1","2","3")
n = ["1","5","6"]
x.update(y,z,n)
print(x)


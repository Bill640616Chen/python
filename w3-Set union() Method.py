#https://www.w3schools.com/python/ref_set_union.asp
#Python Set union() Method 集合聯集方法
#Return a set that contains all items from both sets, duplicates are excluded:
#傳回一個集合包含兩個集合的所有項目,重複的項目只有一個項目會出現
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z) #{'microsoft', 'apple', 'cherry', 'google', 'banana'}
#Definition and Usage
#The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
#union()方法傳回包含原始集合中所有項目以及指定集合的所有項目。
#You can specify as many sets you want, separated by commas.
#你可以指定你想要多少集合,並用逗號分開
#It does not have to be a set, it can be any iterable object.
#它不需要是一個集合,它是可以任何的可迭代物件
#If an item is present in more than one set, the result will contain only one appearance of this item.
#如果一個項目存在於超過一個集合裡,那結果將只有一個項目會出現
#Syntax
#set.union(set1, set2...)
#Parameter Values
#Parameter	Description
#set1：Required. The iterable to unify with
#set2：Optional. The other iterable to unify with.
#You can compare as many iterables as you like.
#Separate each iterable with a comma
#如果一個項目存在於超過一個集合裡,那結果將只有一個項目會出現
#Unify more than 2 sets:
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result) #{'d', 'f', 'c', 'a', 'e', 'b'}
print(x.union(y, z)) #輸出跟32行一樣
x.union(y, z) #有傳回到值,沒有變數,只是一個方法,沒法執行
print(x) #只能輸出28行的值
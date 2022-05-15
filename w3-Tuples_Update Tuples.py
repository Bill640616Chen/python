#https://www.w3schools.com/python/python_tuples_update.asp
#Python Update Tuples 更新Tuple
#Tuples are unchangeable, meaning that you cannot
# change, add, or remove items once the tuple is created.
#But there are some workarounds.但也有一些解決方法。
print("--------------使用轉換list-Change Tuple Values 改變Tuple的值")
#Change Tuple Values 改變Tuple的值
#Once a tuple is created, you cannot change its values. Tuples are
#  unchangeable, or immutable as it also is called.
#一旦創建了 Tuple，您就無法更改其值。tuple是不可改變的，或不變的，
# 因為它也可以被呼叫。
#But there is a workaround. You can convert the tuple into a list, 
# change the list, and convert the list back into a tuple.
#但有一個解決方法。您可以將tuple換為清單，更改清單，並將清單轉換回tuple。
#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x) #轉換成list
y[1] = "kiwi"
x = tuple(y) #轉換成tuple
print(x) #('apple', 'kiwi', 'cherry')

print("------------------------------------Add Items 增加項目")
#Add Items 增加項目
#Since tuples are immutable, they do not have a build-in append()
# method, but there are other ways to add items to a tuple.
#由於 Tuple 是不變的，因此它們沒有內建append()方法，
#但還有其他方法可以將項目添加到 Tuple 中。
#1. Convert into a list: Just like the workaround for changing a tuple,
# you can convert it into a list, add your item(s), 
# and convert it back into a tuple.
#1.轉換為清單：就像更換 Tuple 的變通方法一樣，您可以將其轉換為清單，
#添加您的項目，並將其轉換回tuple。
#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

print("------------------------------------Add tuple to a tuple")
#2. Add tuple to a tuple. You are allowed to add tuples to tuples, 
# so if you want to add one item, (or many), create a new tuple with
#  the item(s), and add it to the existing tuple:
#2.添加tuple到一個tuple中。你被允許添加tuple到一個tuple中，
# 所以如果你想要增加一個項目，（或者很多），創建一個新的含有新項目的tuple，
# 並把它加入一個已存在的tuple裡：
#Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",) #有逗號才被當作tuple
thistuple += y #可以使用運算子+=添加一個新tuple,list也可以使用
print(thistuple) #('apple', 'banana', 'cherry', 'orange')
#Note: When creating a tuple with only one item, remember to include
# a comma after the item, otherwise it will not be identified
# as a tuple.
#當創建一個只有一個項目的 tuple 時，請記住在專案後包含逗號，否則它將不會
# 被識別為 tuple。

print("------------------------------------Remove Items 移除項目")
#Remove Items 移除項目
#Note: You cannot remove items in a tuple.
#Tuples are unchangeable, so you cannot remove items from it, 
# but you can use the same workaround as we used for changing and
# adding tuple items:
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #('banana', 'cherry')

print("--------------------------------del(開鍵字)可以完全刪除tuple")
#Or you can delete the tuple completely: 或者可以完全刪除tuple
#The del keyword can delete the tuple completely:
#del(開鍵字)可以完全刪除tuple
thistuple = ("apple", "banana", "cherry")
del thistuple #del是關鍵字,可以清除None存在記憶體的資料
print(thistuple) #name 'thistuple' is not defined
#this will raise an error because the tuple no longer exists
#這將引發錯誤， 因為tuple不再存在

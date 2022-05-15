#https://www.w3schools.com/python/python_lists.asp
#Python Lists
mylist = ["apple", "banana", "cherry"]
#List 清單(陳列)
#Lists are used to store multiple items in a single variable.
#清單用於在單個變數中存儲多個項目。
#Lists are one of 4 built-in data types in Python used to store 
# collections of data, the other 3 are Tuple, Set, and Dictionary, 
# all with different qualities and usage.
#清單是 Python 中用於儲存資料集合的 4 種內置數據類型之一，其他 3 種是 
# Tuple、Set 和字典，它們具有不同的品質和用法。
#Lists are created using square brackets:
#清單使用方括弧［］創建
#Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist) #['apple', 'banana', 'cherry']
#List Items
#List items are ordered, changeable, and allow duplicate values.
#清單項目是有順序的、可更改並允許重複值。
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#清單項目為索引，第一個項目為索引 [0]，第二個項目為索引 [1] 依此類推。

#Ordered
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#當我們說清單有順序時，這意味著項目具有定義的順序，並且該順序不會改變。
#If you add new items to a list, the new items will be placed at the end of the list.
#如果將新項目添加到清單中，則新項目將放在清單的末尾。
#Note: There are some list methods that will change the order, but in general: the order of the items will not change.
#注意:有一些清單方法將更改順序，但一般來說：項目的順序不會改變。

#Changeable可更改的
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#清單是可更改的，這意味著我們可以在創建清單后更改、添加和刪除清單中的項目。
#Allow Duplicates允許重複
#Since lists are indexed, lists can have items with the same value:
#由於清單已編入索引，清單可以具有相同值的項目：
#Lists allow duplicate values:清單允許重複值
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) #['apple', 'banana', 'cherry', 'apple', 'cherry']

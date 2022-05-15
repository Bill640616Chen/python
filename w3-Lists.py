#https://www.w3schools.com/python/python_lists.asp
#Python Lists
#mylist = ["apple", "banana", "cherry"]
#List
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets: 使用[]
print("-------------------------------------用[]書寫Create a List")
#Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist) #['apple', 'banana', 'cherry']

#List Items
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#Tuple項目可以被索引，第一項為索引 [0]，第二項為索引 [1] 等。

#Ordered 有序的
#When we say that List are ordered, it means that the items have a defined order, and that order will not change.
#當我們說Tuple是有序時，這意味著項目有一個明確的順序，並且該順序不會改變。
#Note: There are some list methods that will change the order, but in general: the order of the items will not change.
#list裡有些方法可以改變順序,但一般來說順序是不會改變的

#Changeable 可改變的
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#清單是可更改的，這意味著我們可以在創建清單后更改、添加和刪除清單中的項目。

print("----------------------lists allow duplicate values")
#Allow Duplicates允許重複
#Since lists are indexed, they can have items with the same value:
#從list被索引化,他們可以有相同值的項目
#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) #["apple", "banana", "cherry", "apple", "cherry"]

print("------------------決定lists有多少項目，要使用len()功能")
#list Length list長度
#To determine how many items a list has, use the len() function:
#決定list有多少項目，要使用len()功能
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #3

print("------------------List items can be of any data type:")
#List items can be of any data type:
#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

print("-------------A list can contain different data types:")
#A list can contain different data types:
#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1) #('abc', 34, True, 40, 'male')

print("-----------------------------------------------type()")
#type()
#From Python's perspective, lists are defined as objects with the data type 'list':
#從 Python 的角度來看，清單被定義為具有數據類型「清單」的物件：
#<class 'list'>
#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #<class 'list'>

print("----------------------------The list() Constructor構造")
#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thislist) #['apple', 'banana', 'cherry']

#Python Collections (Arrays) Python的集合(陣列) 
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. 
# Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. 
# Allows duplicate members.
#Set is a collection which is unordered ,unindexed and unchangeable. 
# No duplicate members.
#Dictionary is a collection which is ordered* and changeable. 
# No duplicate members.

#*As of Python version 3.7, dictionaries are ordered. 
# In Python 3.6 and earlier, dictionaries are unordered.

#When choosing a collection type, it is useful to understand 
# the properties of that type. Choosing the right type for a 
# particular data set could mean retention of meaning, and, 
# it could mean an increase in efficiency or security.
#在選擇集合類型時，瞭解該類型的屬性是有用的。為特定數據集選擇正確的類型
# 可能意味著保留意義，並且，它可能意味著效率或安全性的提高。
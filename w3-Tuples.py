#https://www.w3schools.com/python/python_tuples.asp
#Python Tuples 元組
#Tuple
#Tuples are used to store multiple items in a single variable.
#Tuples 用於在單個變數中存儲多個項目。
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#Tuple 是 Python 中用於存儲數據集合的 4 種內建數據類型之一，
# 其他 3 種是清單、集合和字典，所有類型和用途都不同。
#A tuple is a collection which is ordered and unchangeable.
#tuple是有序和不變的集合。
#Tuples are written with round brackets.
print("----------------------Tuples用圓形括號書寫")
#Tuples用圓形括號書寫。
#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple) #('apple', 'banana', 'cherry')

#Tuple Items
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple項目是有序的,不可改變的,允許重複值
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Tuple項目可以被索引，第一項為索引 [0]，第二項為索引 [1] 等。

#Ordered有序的
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#當我們說Tuple是有序時，這意味著項目有一個明確的順序，並且該順序不會改變。

#Unchangeable不可改變
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Tuples都是不可改變的,意思是在tuple創建後我們不能改變,增加或移除項目

#Allow Duplicates允許重複
#Since tuples are indexed, they can have items with the same value:
#從tuples被索引化,他們可以有相同值的項目
#Tuples allow duplicate values:
print("----------------------Tuples allow duplicate values")
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #('apple', 'banana', 'cherry', 'apple', 'cherry')

print("------------------決定tuple有多少項目，要使用len()功能")
#Tuple Length tupe長度
#To determine how many items a tuple has, use the len() function:
#決定tuple有多少項目，要使用len()功能
#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #3

print("------------------------認可Tuple的規則,必須要有逗號")
#Create Tuple With One Item 創建一個項目為一個tuple
#To create a tuple with only one item, you have to add a comma 
# after the item, otherwise Python will not recognize it as a tuple.
#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>
#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #<class 'str'>
#用type(變數)來檢查()內是哪一種資料類型

print("------------------tuple裡的項目可以是任何數據類型")
#Tuple Items - Data Types 數據類型
#Tuple items can be of any data type:
#tuple裡的項目可以是任何資料類型
#String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry") #字串
tuple2 = (1, 5, 7, 9, 3) #int
tuple3 = (True, False, False) #boolean
print(tuple1)
print(tuple2)
print(tuple3)

print("---------------A tuple can contain different data types")
#A tuple can contain different data types:
#A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

print("------------------------------------------------type()")
#type()
#From Python's perspective, tuples are defined as objects with the data type 'tuple':
#從 Python 的角度來看，tuples被定義為具有數據類型「tuples」的物件：
#<class 'tuple'>
#What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #<class 'tuple'>

print("-----------------------The tuple() Constructor tuple()構造")
#The tuple() Constructor tuple()構造
#It is also possible to use the tuple() constructor to make a tuple.
#也可能使用the tuple()構造器製作the tuple。
#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #('apple', 'banana', 'cherry')
list = list(("apple", "banana", "cherry"))
print(list) #['apple', 'banana', 'cherry']
mytuple = ("apple", "banana", "cherry")

#Python Collections (Arrays) Python的集合(陣列) 
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. 
# Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. 
# Allows duplicate members.
#Set is a collection which is unordered and unindexed. 
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
#https://www.w3schools.com/python/python_sets.asp
#Python Sets 集合
#myset = {"apple", "banana", "cherry"}
#set是用{}的
#Set
#Sets are used to store multiple items in a single variable.
#Sets於在單個變數中存儲多個項目。
#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#Set與list,tuple,dictionary,它們的品質和使用方式都各不相同
#A set is a collection which is both unordered and unindexed.
#set既無序又無索引
#Sets are written with curly brackets.
#set是用{}書寫的
print("---------------------------------------------Create a Set")
#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset) #{'cherry', 'banana', 'apple'}
#因為set是無序的,輸出順序跟原來的不同
#Note: Sets are unordered, so you cannot be sure in which order the items will appear.

#Set Items
#Set items are unordered, unchangeable, unindexed and do not allow duplicate values.

#Unordered無序
#Unordered means that the items in a set do not have a defined order.
#無序意味著集中的項目沒有定義的順序。
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#每次你使用Set item時都會顯示不同的順序,並不能指定索引或key

#Unchangeable不可改變
#Sets are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can add new items.

print("--------------------------Duplicate values will be ignored")
#項目不可改變但可以加項目
#Duplicates Not Allowed 重複值是不被允許的
#Sets cannot have two items with the same value.

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #{'cherry', 'apple', 'banana'}